from urllib.request import urlopen
import urllib

urlopen = urllib.request.urlopen('https://en.wikipedia.org/wiki/Lorem_ipsum')
webpage = urlopen.read().decode('utf-8')
print(webpage)