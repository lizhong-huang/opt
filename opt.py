#!/home/lizhong/.virtualenvs/opt/bin/python3

import sys
import getopt
import requests

baseurl="https://omnipoints-api-dev.azurewebsites.net"

def help(error):
     print(error)
     print("Example:")
     print("  createmember -d <devide-id> -nickname <nick-name>")
     print("  add -m <merchant-id> -d <device-id> -p <num-of-points>")
     print("  redeem -m <merchant-id> -d <devide-id> -p <num-of-points>")

def createmember(did, nickname):
    _payload = {
            "did" : did,
            "dtype" : "iPhone",
            "Nickname" : nickname
            }
    _headers = {
            "x-default-appkey" : "default-appkey",
            "Content-Type": "text/json; charset=utf-8"
            }

    try:
        _url = baseurl + "/api/members"
        print(_payload)
        _response = requests.post(_url, headers=_headers,  json=_payload)
    except:
        print("talking to remote svc failed")
        sys.exit(2)

    if (not _response.ok):
        print("Failed with HTTP status code: ", _response.status_code)
        print("Failed reason: ", _response.reason)
        print("Failed details: ", _response.text)
        sys.exit(2)

    print(_response.text)
    return

def createmerchant():
    _payload = {
            "did" : did,
            "dtype" : "iPhone",
            "Nickname" : nickname
            }
    _headers = {
            "x-default-appkey" : "default-appkey",
            "Content-Type": "text/json; charset=utf-8"
            }

    try:
        _url = baseurl + "/api/members"
        print(_payload)
        _response = requests.post(_url, headers=_headers,  json=_payload)
    except:
        print("talking to remote svc failed")
        sys.exit(2)
    if (not _response.ok):
        print("Failed with HTTP status code: ", _response.status_code)
        print("Failed reason: ", _response.reason)
        print("Failed details: ", _response.text)
        sys.exit(2)
    print(_response.text)
    return

def addpoints(mid, did, points):
    print("add points...", mid, did, points)
    _payload = {
            "mid" : mid,
            "tt" : 3,
            "fp" : 1 
            }
    _headers = {
            "Authorization" : "Bearer xxxxxxxxxxxx",
            "Content-Type": "application/json; charset=utf-8"
            }

    try
        _url = baseurl + "/api/merchants/me"
        _response = requests.post(_url, headers=_headers, json= _payload)
    except:
        print("talking to remote svc failed")
        sys.exit(2)

    if (not _response.ok):
        print("Failed with HTTP status code: ", _response.status_code)
        print("Failed reason: ", _response.reason)
        print("Failed details: ", _response.text)
        sys.exit(2)

    return

def redeempoints():
    print("redeem points...")
    return

def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], "m:d:p:")
        print("opts: ", opts)
        print("args: ", args)
    except getopt.GetoptError:
        help()
        sys.exit(2)
    for opt, arg in opts:
        if (opt == "-m"):
            _mid = arg
        elif (opt == "-d"):
            _did = arg
        elif (opt == "-p"):
            _points = arg

    try:
       if (argv[0] == "createmember"):
           createmember(_did)
       elif (argv[0] == "add"):
           addpoints(_mid, _did, _points)
       elif (argv[0] == "redeem"):
           redeempoints()
       else:
           help("unknown command " + argv[0])
    except IndexError:
        help("missing command")
    except NameError:
        help("missing one or more options")

if (__name__ == "__main__"):
    main(sys.argv[1:])

