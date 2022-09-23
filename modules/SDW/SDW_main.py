from SDW_query import get_datas
from SDW_paint import draw, ColorMaker
import math
import pandas as pd

def get_value_range(values: list, div: int) -> list:
    mx, mn = math.ceil(max(values)), int(min(values))
    span = max(mx - mn, 1)
    step = span // div
    if span % div != 0: step += 1
    return list(range(mn, mx + step, step))

def draw_temperature(df: pd.DataFrame) -> str:
    values = df['temperature'].values
    value_range = get_value_range(values, 6)
    colors = ColorMaker.generate('blue', 8, 5)[ : : 4]
    if len(colors) < len(value_range): colors += ColorMaker.generate('green', 8, 5, True)[ : : 4]
    if len(colors) < len(value_range): colors += ColorMaker.generate('red', 8, 3, True)[ : : 3]
    return draw(
        '山东温度图', 
        list(zip(df['location'].values, df['temperature'].values)), 
        value_range, 
        colors,
        '℃',
    )
    
def draw_humidity(df: pd.DataFrame) -> str:
    values = df['humidity'].values
    value_range = get_value_range(values, 6)
    colors = ColorMaker.generate('orangeyellow', 8, 3, True)[ : : 4]
    if len(colors) < len(value_range): colors += ColorMaker.generate('bluecyan', 8, 5)[ : : 4]
    if len(colors) < len(value_range): colors += ColorMaker.generate('green', 8, 3, True)[ : : 3]
    return draw(
        '山东湿度图', 
        list(zip(df['location'].values, df['humidity'].values)), 
        value_range, 
        colors,
        '%',
    )


def draw_pressure(df: pd.DataFrame) -> str:
    values = df['pressure'].values
    value_range = get_value_range(values, 6)
    colors = ColorMaker.generate('greencyan', 8, 5)[ : : 4]
    if len(colors) < len(value_range): colors += ColorMaker.generate('yellow', 8, 3, True)[ : : 4]
    if len(colors) < len(value_range): colors += ColorMaker.generate('bluepurple', 8, 3, True)[ : : 3]
    return draw(
        '山东气压图', 
        list(zip(df['location'].values, df['pressure'].values)), 
        value_range, 
        colors,
        'hPa',
    )
    
    
def draw_precipitation(df: pd.DataFrame) -> str:
    values = df['precipitation'].values
    values[values == 9999] = 0
    value_range = get_value_range(values, 6)
    if len(value_range) == 1: value_range.append(value_range[0] + 0.01)
    colors = ColorMaker.generate('greenyellow', 8, 3, True)[ : : 4]
    if len(colors) < len(value_range): colors += ColorMaker.generate('bluecyan', 8, 5)[ : : 4]
    if len(colors) < len(value_range): colors += ColorMaker.generate('redpurple', 8, 3, True)[ : : 3]
    return draw(
        '山东降水图', 
        list(zip(df['location'].values, df['precipitation'].values)), 
        value_range, 
        colors,
        'mm',
    )

def SDW_draw():
    print(1)
    df = get_datas()
    print(2)
    draw_temperature(df)
    draw_humidity(df)
    draw_pressure(df)
    draw_precipitation(df)
    print('SDWdraw end')
