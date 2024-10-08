# import whole pacakages
import requests
import base64
import hashlib
import json
import binascii

# import frequently usings
from os import urandom, system, getenv
from sys import argv

requests.packages.urllib3.disable_warnings()

# some string helpers
def s2b(t, encoding = "utf-8"):
    if type(t) == bytes:
        return t
    elif type(t) == str:
        return t.encode(encoding)
    else:
        raise Exception("s2b: Type is not either `bytes` or `str`")

def b2s(t, encoding = "utf-8"):
    if type(t) == str:
        return t
    elif type(t) == bytes:
        return t.decode(encoding)
    else:
        raise Exception("b2s: Type is not either `bytes` or `str`")

def b64e(t, encoding = "utf-8"):
    _buf = s2b(t, encoding)
    return base64.b64encode(_buf)

def b64d(t, encoding = False):
    _buf = base64.b64decode(t)
    if type(encoding) == bool:
        if not encoding:
            return _buf
        else:
            return b2s(_buf)
    else:
        return b2s(_buf, encoding)

def bin2hex(t, encoding = "utf-8"):
    return s2b(t, encoding).hex()

def hex2bin(t, encoding = False):
    _buf = binascii.unhexlify(t)
    if type(encoding) == bool:
        if encoding == False:
            return b2s(_buf)
        else:
            return _buf
    else:
        return b2s(_buf, encoding)

hc = hex2bin

def str_xor(x, y, encoding = "utf-8"):
    if len(x) < len(y):
        return str_xor(y, x, encoding = encoding)
    
    assert(len(x) >= len(y))
    
    _x = s2b(x, encoding = encoding)
    _y = s2b(y, encoding = encoding)
    res =[]

    for i in range(len(_x)):
        res.append(_x[i] ^ _y[i % len(_y)])
    
    return b2s(bytes(res), encoding = encoding)

# some cryptographic helpers
def rand_hex(length):
    return os.urandom(length // 2 + 1).hex()[:length]

def md5(t, raw = False, encoding = "utf-8"):
    _buf = s2b(t, encoding)
    if raw:
        return hashlib.md5(_buf).digest()
    return hashlib.md5(_buf).hexdigest()

def sha1(t, raw = False, encoding = "utf-8"):
    _buf = s2b(t, encoding)
    if raw:
        return hashlib.sha1(_buf).digest()
    return hashlib.sha1(_buf).hexdigest()

def sha256(t, raw = False, encoding = "utf-8"):
    _buf = s2b(t, encoding)
    if raw:
        return hashlib.sha256(_buf).digest()
    return hashlib.sha256(_buf).hexdigest()

# some file helpers
def file_get_contents(filename, encoding = 'utf-8'):
    if encoding == 'bin':
        f = open(filename, mode = 'rb')
    else:
        f = open(filename, mode = 'r', encoding = encoding)
    d = f.read()
    f.close()
    return d

def _readlines(filename, encoding = 'utf-8', strip = True):
    f = open(filename, mode = 'r', encoding = encoding)
    d = [x.rstrip('\n') for x in  f.readlines()]
    f.close()
    return d

def file_put_contents(filename, data, append = False, encoding = 'utf-8'):
    f = None
    if type(data) == bytes:
        if not append:
            f = open(filename, mode = 'wb')
        else:
            f = open(filename, mod = 'ab')
    else:
        if not append:
            f = open(filename, mode = 'w', encoding = encoding)
        else:
            f = open(filename, mod = 'a', encoding = encoding)

    f.write(data)
    f.close()


# Some HTTP helpers
'''
_P_REQ_HOST = None
_P_REQ_HEADER = None
_P_REQ_PROXY = None


class Req():
    def __init__(self, host = "", headers = {}, proxy = {}):
        self.host = host
        self.heades = dict(header)
        self.proxy = proxy
    
    def set_proxy(host = "127.0.0.1", port = 8080):
        proxy_url = "http://{}:{}".format(host, port)
        self.proxy['http'] = proxy_url
        self.proxy['https'] = proxy_url
    

def set_host(host):
    global _P_REQ_HOST
    _P_REQ_HOST = host

def set_header(header_obj):
    global _P_REQ_HEADER
    _P_REQ_HEADER = dict(header_obj)

def set_proxy(proxy_obj = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}):
    global _P_REQ_PROXY
    _P_REQ_PROXY = dict(proxy_obj)
'''

BURP = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
UA = {
    "CHROME_W": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "CHROME_M": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "FIREFOX_W": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "FIREFOX_M": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:130.0) Gecko/20100101 Firefox/130.0",
    "SAFARI_M": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15",
    "SAFARI_I": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1",
}

get = requests.get
post = requests.post
