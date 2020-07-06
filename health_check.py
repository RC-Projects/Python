#This scripts inputs a URL and provides the status code of the provided endpoint. 

import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

#Input URL
webst = input('Enter an endpoint to check on: (eg: https://mysite.com/status)\n')

#Catch errors
req = Request(webst)
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
	#Get status code
	req = urllib.request.urlopen(webst)
	req_code = req.getcode()							 

	#Output result
	print('Reply code: ', req_code)


