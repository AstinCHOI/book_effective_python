
# python3
# class Meta(type):
#     def __new__(meta, name, bases, class_dict):
#         print((meta, name, bases, class_dict))
#         return type.__new__(meta, name, bases, class_dict)

# class MyClass(object, metaclass=Meta):
#     stuff = 123

#     def foo(self):
#         pass

# >>>
# (<class '__main__.Meta'>, 
#  'MyClass', 
#  (<class 'object'>,), 
#  {'__module__': '__main__', 
#  'stuff': 123, 
#  'foo': <function MyClass.foo at 0x10147b268>, 
#  '__qualname__': 'MyClass'})


# python2
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)

class MyClassInPython2(object):
    __metaclass__ = Meta
    stuff = 123

    def foo(self):
        pass
# >>>
# (<class '__main__.Meta'>, 
#  'MyClassInPython2', 
#  (<type 'object'>,), 
#  {'__module__': '__main__', 
#  'stuff': 123, 
#  '__metaclass__': <class '__main__.Meta'>, 
#  'foo': <function foo at 0x101801ed8>})


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # not to verify for abstract Polygon class
        if bases != (object, ):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(object, metaclass=ValidatePolygon):
    sides = None # set to subclass

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Triangle(Polygon):
    sides = 3

print('Before class')
class Line(Polygon):
    print('Before sides')
    sides = 1
    print('After sides')
print('After class')
# >>>
# Before class
# Before sides
# After sides
# ValueError: Polygons need 3+ sides

# Meta.__new__() runs after runing entire body 