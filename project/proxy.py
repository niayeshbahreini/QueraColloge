class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invok = ""
        self.calls = {}

    def get(self):
        return dir(self._obj)

    def __getattr__(self, item):
        if item in dir(self._obj):
            self.last_invok = item
            if item not in self.calls:
                self.calls[item] = 1
            else:
                self.calls[item] += 1
            return getattr(self._obj, item)
        else:
            raise Exception('No Such Method')

    def last_invoked_method(self):
        if self.last_invok not in self.calls:
            raise Exception('No Method Is Invoked')
        else:
            return self.last_invok

    def count_of_calls(self, method_name):
        if method_name not in self.calls:
            return 0
        else:
            return self.calls[method_name]

    def was_called(self, method_name):
        if method_name in self.calls:
            return True
        else:
            return False


class Radio():
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel

    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on

'''
class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invok = ""
        self.calls = {}

    def __getattr__(self, attr):
        try:
            value = getattr(self._obj, attr)
        except Exception:
            raise Exception('No Such Method')
        
        else:
            self.last_invok = attr
            if not attr in self.calls:
                self.calls[attr] = 1
            else:
                self.calls[attr] +=1
            return value
    def last_invoked_method(self):
        if self.last_invok:
            return self.last_invok
        raise Exception('No Method Is Invoked')

    def count_of_calls(self, method_name):
        if method_name in self.calls:
            return self.calls[method_name]
        return 0

    def was_called(self, method_name):
        return method_name in self.calls


'''