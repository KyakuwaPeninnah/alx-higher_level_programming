#!/usr/bin/python3
'''Python script that takes in a URL and an email'''


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
