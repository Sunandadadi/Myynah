import requests
import json

class SuccessResponse(object):
    def __init__(self, obj):
        self.status_code = obj.status_code
        self.content = json.loads(obj.content)

class FailureResponse(object):
    def __init__(self, obj):
        self.status_code = obj.status_code
        self.content = obj.content

    def __str__(self):
        return 'Failed with error code: {} and message as {}'.format(self.status_code, self.content)

class BaseClient(object):

    def __init__(self, url, arg=None):
        self.url = url
        self.arg = arg

    def raise_error(self, err):
        raise Exception(str(FailureResponse(err)))

    def get(self):
        response = requests.get(self.url)
        return SuccessResponse(response) if response.status_code == 200 else self.raise_error(response)
