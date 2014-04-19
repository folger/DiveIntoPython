import chardet
from urllib.request import urlopen


TestData = urlopen('http://www.163.com').read()
print(chardet.detect(TestData))
