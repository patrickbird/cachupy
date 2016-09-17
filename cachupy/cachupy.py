import datetime

class Cache:
    EXPIRE_IN = 'expire_in'
    VALUE = 'value'

    def __init__(self):
        self.lock = False
        self.store = {}

    def get(self, key):
        """Gets a value based upon a key.""" 
        self._check_expiry(key)        
        return self.store[key][Cache.VALUE]

    def set(self, expire_in, *args):
        """Sets a dictionary to the cache with a timedelta expiration."""
        for arg in args:
            if isinstance(arg, dict):
                for k,v in arg.items():
                    self._set(k, v, expire_in)
            else: 
                for v in arg:
                    self._set(v[0], v[1], expire_in)

    def has(self, key):
        """Returns whether a key is in the cache."""
        self._check_expiry(key)
        return key in self.store

    def _set(self, key, value, expire_in):
        self.store[key] = {
            Cache.EXPIRE_IN: datetime.datetime.now() + expire_in,
            Cache.VALUE: value
        }
    
    def _check_expiry(self, key):
        """Removes a key/value pair if it's expired."""
        if not self.lock and key in self.store and datetime.datetime.now() > self.store[key][Cache.EXPIRE_IN]:
            self.store.pop(key, None)
        
