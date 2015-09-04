# Python case insensitive dictionary
### Example

```python
from CaseInsensitiveDict import CaseInsensitiveDict

cid = CaseInsensitiveDict({"A": {"A": 1}, "B": 2, "c": 3})

print cid["A"] # >>> {'a': 1}
print cid["a"] # >>> {'a': 1}
print cid["A"]["a"] # >>> 1
print cid["b"] # >>> 2
print cid["C"] # >>> 3
```
### Development

Feel free to contribute.

### Copyright and License

&copy; 2015 [Vít Listík](http://tivvit.cz)

Released under [MIT licence](https://github.com/tivvit/python-case-insensitive-dict/blob/master/LICENSE)