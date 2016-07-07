
import json

class Serializable(object):
    def __init__(self, *args):
        self.args = args
    
    def serialize(self):
        return json.dumps({'args': self.args})
    
class Point2D(Serializable):
    def __init__(self, x, y):
        super(Point2D, self).__init__(x, y)
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Point2D(%d, %d)' % (self.x, self.y)

point = Point2D(5, 3)
print('Object:     ', point)
print('Serialized: ', point.serialize())
# >>>
# ('Object:     ', Point2D(5, 3))
# ('Serialized: ', '{"args": [5, 3]}')


class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])

class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super(BetterPoint2D, self).__init__(x, y)
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'BetterPoint2D(%d, %d)' % (self.x, self.y)

point = BetterPoint2D(5, 3)
print('Before:     ', point)
data = point.serialize()
print('Serialized: ', data)
after = BetterPoint2D.deserialize(data)
print('After:      ', after)
# >>>
# ('Before:     ', BetterPoint2D(5, 3))
# ('Serialized: ', '{"args": [5, 3]}')
# ('After:      ', BetterPoint2D(5, 3))


class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args
    
    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args
        })
    
    def __repr__(self):
        return '%s(%s)' % (
            self.__class__.__name__,
            ', '.join(str(x) for x in self.args))

registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])

class EvenBetterPoint2D(BetterSerializable):
    def __init__(self, x, y):
        super(EvenBetterPoint2D, self).__init__(x, y)
        self.x = x
        self.y = y

register_class(EvenBetterPoint2D)

point = EvenBetterPoint2D(5, 3)
print('Before:     ', point)
data = point.serialize()
print('Serialized: ', data)
after = BetterPoint2D.deserialize(data)
print('After:      ', after)
# >>>
# ('Before:     ', EvenBetterPoint2D(5, 3))
# ('Serialized: ', '{"args": [5, 3], "class": "EvenBetterPoint2D"}')
# ('After:      ', BetterPoint2D(5, 3))


class Point3D(BetterSerializable):
    def __init__(self, x, y, z):
        super(Point3D, self).__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z

# Gosh, forgot to call register_class
point = Point3D(5, 9, -4)
data = point.serialize()
# deserialize(data)
# >>>
# KeyError: 'Point3D'


# + best solution with 33_item
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls

class RegisteredSerializable(BetterSerializable,
                             metaclass=Meta):
    pass


class Vector3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super(Vector3D, self).__init__(x, y, z)
        self.x, self.y, self.z = x, y, z

v3 = Vector3D(10, -7, 3)
print('Before:       ', v3)
data = v3.serialize()
print('Serialized:   ', data)
print('After:        ', deserialize(data))
# >>>
# Before:        Vector3D(10, -7, 3)
# Serialized:    {"class": "Vector3D", "args": [10, -7, 3]}
# After:         Vector3D(10, -7, 3)
