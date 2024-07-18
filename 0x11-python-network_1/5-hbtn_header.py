#!/usr/bin/python3
'''displays the value of the variable X-Request-Id in the response'''

if __name__ == '__main__':
    import requests
    import sys

    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
