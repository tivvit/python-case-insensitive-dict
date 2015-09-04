"""
    dict with case insensitive keys
"""
class CaseInsensitiveDict():
    def  __init__(self, dictionary):
        self.data = self.__create(dictionary)

    def __create(self, dictionary):
        data = {}
        for k, v in dictionary.items():
            if isinstance(v, dict):
                data[k.lower()] = CaseInsensitiveDict(self.__create(v))
            else:
                data[k.lower()] = v
        return data

    def __getitem__(self, item):
        return self.data[item.lower()]

    def __contains__(self, item):
        return item.lower() in self.data

    def __repr__(self):
        return str(self.data)