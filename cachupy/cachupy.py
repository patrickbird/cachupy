import datetime

class Cache:
    EXPIRE_IN = 'expire_in'

    def __init__(self):
        self.store = {}

    def get(self, key):
        """Gets a value based upon a key.""" 
        self._check_expiry(key)        
        return self.store[key]['value']

    def set(self, dictionary, expire_in):
        """Sets a dictionary to the cache with a timedelta expiration."""
        for key in dictionary.keys():
            self.store[key] = {
                Cache.EXPIRE_IN: datetime.datetime.now() + expire_in,
                'value': dictionary[key]
            }

    def has(self, key):
        """Returns whether a key is in the cache."""
        self._check_expiry(key)
        return key in self.store
    
    def _check_expiry(self, key):
        """Removes a key/value pair if it's expired."""
        if key in self.store and datetime.datetime.now() > self.store[key][Cache.EXPIRE_IN]:
            self.store.pop(key, None)
        
