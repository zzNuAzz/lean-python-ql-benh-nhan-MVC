import json

class BaseModel(object):
    def toDict(self):
        return self.__dict__
