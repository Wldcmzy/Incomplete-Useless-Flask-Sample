import aiohttp
import asyncio
import json
import re
from typing import Any, Optional, Union
import requests
from bs4 import BeautifulSoup
import pandas as pd

class MeasureItem:
    def __init__(self, value: Any, measure: str) -> None:
        self.value = value
        self.measure = measure
    
    def reset(self, value: Optional[str], measure: Optional[str]) -> None:
        if value: self.value = value
        if measure: self.measure  = measure

    def __str__(self) -> str:
        return f'{self.value}({self.measure})'
    
    def getValue(self) -> Any:
        return self.value

class WeatherData:
    def __init__(self, data: Union[dict, str]) -> None:
        if type(data) == str: data = json.loads(data)
        data = data['data']
        self.location: str = data['location']['name'] + '市'
        self.precipitation: MeasureItem = MeasureItem(data['now']['precipitation'], 'mm')
        self.temperature: MeasureItem = MeasureItem(data['now']['temperature'], '℃')
        self.pressure: MeasureItem = MeasureItem(data['now']['pressure'], 'hPa')
        self.humidity: MeasureItem = MeasureItem(data['now']['humidity'], '%')
    

def index() -> list[str]:
    res = requests.get('https://weather.cma.cn/web/weather/54823.html')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    lst = soup.find('ul', 'dropdown-menu station-select').findAll('li')
    urls = []
    for each in lst[ : 17]:
        id = re.search('/([0-9]+?)\.html', each.a['href']).group(1)
        urls.append('https://weather.cma.cn/api/now/' + id)
    return urls

async def requestONE(url: str) -> str:
    async with session.get(url) as res:
        return await res.text()

async def parseDATA(text: str) -> WeatherData:
    return WeatherData(text)

async def work(url: str) -> None:
    async with semaphore:
        soup = await requestONE(url)
        data = await parseDATA(soup)
        datas.append(data)

def get_datas(to_DataFrame = True) -> Optional[pd.DataFrame]:
    global datas, session, semaphore
    datas = []
    session = aiohttp.ClientSession()
    semaphore = asyncio.Semaphore(6)

    urls = index()

    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(work(each)) for each in urls]
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)

    if to_DataFrame:
        df = pd.DataFrame()
        for each in datas:
            tmp = pd.DataFrame(
                [[
                    each.location,
                    each.temperature.getValue(),
                    each.humidity.getValue(),
                    each.pressure.getValue(),
                    each.precipitation.getValue(),
                ]], 
                columns = [
                    'location',
                    'temperature',
                    'humidity',
                    'pressure',
                    'precipitation',
                ],
            )
            df = pd.concat([df, tmp], ignore_index = True)

        return df
