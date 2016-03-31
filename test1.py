import urllib2
response = urllib2.urlopen('www.hao123.com')
html = response.read()
print html
