"""
    dict with case insensitive keys
"""
class CaseInsensitiveDict():
    def __init__(self, dictionary={}):
        self._data = self.__create(dictionary)

    def __create(self, value):
        if isinstance(value, dict):
            data = {}
            for k, v in value.items():
                if isinstance(v, dict):
                    data[k.lower()] = CaseInsensitiveDict(self.__create(v))
                else:
                    data[k.lower()] = v
            return data
        else:
            return value

    def __getitem__(self, item):
        return self._data[item.lower()]

    def __contains__(self, item):
        return item.lower() in self._data

    def __setitem__(self, key, value):
        self._data[key.lower()] = self.__create(value)

    def __delitem__(self, key):
        del self._data[key.lower()]

    def __iter__(self):
        return (k for k in self._data.keys())

    def __len__(self):
        return len(self._data)

    def __eq__(self, other):
        if isinstance(other, dict):
            other = CaseInsensitiveDict(other)
        else:
            raise NotImplementedError

        # Compare insensitively
        return dict(self.items()) == dict(other.items())

    def __repr__(self):
        return str(self._data)

    def get(self, key, default=None):
        if not key.lower() in self:
            return default
        else:
            return self[key]

    def has_key(self, key):
        return key.lower() in self

    def items(self):
        return [(k, v) for k, v in self.iteritems()]

    def keys(self):
        return [k for k in self.iterkeys()]

    def values(self):
        return [v for v in self.itervalues()]

    def iteritems(self):
        for k, v in self._data.iteritems():
            yield k, v

    def iterkeys(self):
        for v in self._data.iterkeys():
            yield v

    def itervalues(self):
        for v in self._data.itervalues():
            yield v

    def update(self, dictionary):
        if not (isinstance(dictionary, dict) or
                isinstance(dictionary, CaseInsensitiveDict)):
            raise TypeError

        for k, v in dictionary.items():
            self[k] = v
