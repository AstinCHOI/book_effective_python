
class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = "_" + self.name
    
    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')
    
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer(object):
    # class property
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')

foo = Customer()
print('Before:', repr(foo.first_name), foo.__dict__)
foo.first_name = 'Astin'
print('After:', repr(foo.first_name), foo.__dict__)
# >>>
# Before: '' {}
# After: 'Astin' {'_first_name': 'Astin'}


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        
        return cls


class DatabaseRow(object, metaclass=Meta):
    pass


class Field(object):
    def __init__(self):
        # These will be assigned by the metaclass.
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()

foo = BetterCustomer()
print('Before:', repr(foo.first_name), foo.__dict__)
foo.first_name = 'Astin'
print('After:', repr(foo.first_name), foo.__dict__)
# >>>
# Before: '' {}
# After: 'Astin' {'_first_name': 'Astin'}
# Before: '' {}
# After: 'Astin' {'_first_name': 'Astin'}