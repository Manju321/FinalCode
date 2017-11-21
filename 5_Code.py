
"""Using Python 3.6

Ans for 4th Program
Write a simple routine that makes a call to the REST end point (http://www.thomas-bayer.com/sqlrest/CUSTOMER/) and prints the response status code and response body"""


from urllib.request import urlopen

url = 'http://www.thomas-bayer.com/sqlrest/CUSTOMER/'
with urlopen(url) as response:
    html = response.read()
    print('response Status:', response.status)
    print('response code:', response.code)
    print('response body:', html)

