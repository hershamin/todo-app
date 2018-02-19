import cjson as json
from django.http import HttpResponse
from Crypto.Cipher import AES
import base64
from django.utils.crypto import get_random_string


# Respond in json with status code
def json_response(response, status_code=200):
    return HttpResponse(json.encode(response), status=status_code, content_type='application/json')


# Respond in json with bad request
def bad_request(response):
    res = { 'error' : str(response) }
    return HttpResponse(json.encode(res), status=400, content_type='application/json')


# Get random generated string
def get_rand_key():
    return get_random_string(length=48)


# Validate existing Token in headers
def get_headers_token(request):
    """Return token or nothing"""
    token = str(request.META.get('HTTP_AUTHORIZATION'))
    if 'Token' == token.split(' ')[0]:
        if token.split(' ').__len__() > 1:
            return token.split(' ')[1]
        else:
            return
    else:
        return


# Encrypt Decrypt strings
class AESCipher(object):

    def __init__(self):
        self.key = '6KZA7VUndkPdmpAf'
        self.iv = 'j6CMKSV5gz4hGkmR'
        BS = 16
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]

    def encrypt(self, raw):
        raw = self.pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.unpad(cipher.decrypt(enc))
