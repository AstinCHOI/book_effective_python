
class LazyDB(object):
    def __init__(self):
        self.exists = 5
    
    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value

data = LazyDB()
print('Before:', data.__dict__)
print('foo:', data.foo)
print('After:', data.__dict__)
# >>>
# Before: {'exists': 5}
# foo: Value for foo
# After: {'foo': 'Value for foo', 'exists': 5}


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)

data = LoggingLazyDB()
print('exists:', data.exists)
print('foo:   ', data.foo)
print('foo:   ', data.foo)
# >>>
# exists: 5
# Called __getattr__(foo)
# foo:    Value for foo
# foo:    Value for foo


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5
    
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

data = ValidatingDB()
print('exists:', data.exists)
print('foo   :', data.foo)
print('foo   :', data.foo)

# >>>
# Called __getattribute__(exists)
# exists: 5
# Called __getattribute__(foo)
# foo   : Value for foo
# Called __getattribute__(foo)
# foo   : Value for foo


class MissingPropertyDB(object):
    def __getattr__(self, name):
        if name == 'bad_name':
            raise AttributeError('%s is missing' % name)
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value

data = MissingPropertyDB()
# data.bad_name
# >>>
# AttributeError: bad_name is missing


data = LoggingLazyDB()
print('Before:     ', data.__dict__)
print('foo exists: ', hasattr(data, 'foo'))
print('After:      ', data.__dict__)
print('foo exists: ', hasattr(data, 'foo'))
# >>>
# Before:      {'exists': 5}
# Called __getattr__(foo)
# foo exists:  True
# After:       {'foo': 'Value for foo', 'exists': 5}
# foo exists:  True


data = ValidatingDB()
print('foo exists: ', hasattr(data, 'foo'))
print('foo exists: ', hasattr(data, 'foo'))
# >>>
# Called __getattribute__(foo)
# foo exists:  True
# Called __getattribute__(foo)
# foo exists:  True


class SavingDB(object):
    def __setattr__(self, name, value):
        # Save some data to the DB log
        super().__setattr__(name, value)

class LoggingSavingDB(SavingDB):
    def __setattr__(self, name, value):
        print('Called __setattr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)

data = LoggingSavingDB()
print('Before: ', data.__dict__)
data.foo = 5
print('After: ', data.__dict__)
data.foo = 7
print('Finally: ', data.__dict__)
# >>>
# Before:  {}
# Called __setattr__(foo, 5)
# After:  {'foo': 5}
# Called __setattr__(foo, 7)
# Finally:  {'foo': 7}


class BrokenDictionaryDB(object):
    def __init__(self, data):
        self._data = {}
    
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        return self._data[name]

data = BrokenDictionaryDB({'foo': 3})
# data.foo
# >>>
# RecursionError: maximum recursion depth exceeded while calling a Python object


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data
    
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        data_dict = super().__getattribute__('_data') # prevent loop
        return data_dict[name]
    
    # Also __setattr__ should use super().__setattr__

data = DictionaryDB({'foo': 3})
data.foo
# >>>
# Called __getattribute__(foo)