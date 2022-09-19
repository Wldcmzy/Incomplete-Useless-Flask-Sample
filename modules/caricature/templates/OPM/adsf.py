path = './一拳超人ONE原作版HTMLS'
import os
ls = os.listdir(path)
x = 'OPM/一拳超人ONE原作版HTMLS/'
import re

ssss = '''

<!DOCTYPE html>
<html>
<head>
	<title>INDEX</title>
	<meta charset="utf-8">

    
</head>
<body>

{dsf}

</body>
</html>
'''
zzz = '<a target="_blank"  href="/caricature/OPM{idx}">{arg}</a> <br><br>\n'

vvv = ''

for each in ls:
    a = re.search('\[(.+?)\]', each).group(1)[1 : ]
    b = a[ : 3] + ': ' + a[3 : ]

    vvv += zzz.format(arg = b, idx = a)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(ssss.format(dsf = vvv))