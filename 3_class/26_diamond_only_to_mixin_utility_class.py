
# mix-in means a small class which provides additional methods
#     no definition of attribute and __init__
# python supports dynamic inspection regardless of types

class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__) # instance dictionary
    
    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output
    
    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin): # dynamic inspection
            return value.to_dict()
        elif isinstance(value, dict):
            print('dict')
            return self._traverse_dict(value)
        elif isinstance(value, list):
            print('list')
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'): # dynamic attribute access
            print('__dict__')
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
tree = BinaryTree(10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)))
print(tree.to_dict())
# >>>
# {'right': {'right': None,
#            'value': 13, 
#            'left': {'right': None, 
#                     'value': 11, 
#                     'left': None}},
#  'value': 10, 
#  'left': {'right': {'right': None, 
#                     'value': 9, 
#                     'left': None}, 
#           'value': 7, 
#           'left': None}}


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent
    
    def _traverse(self, key, value):
        if (isinstance(value, BinaryTreeWithParent) and key == 'parent'):
            print('parent', value.value)
            return value.value # prevent recursion
        else:
            return super()._traverse(key, value)

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
print(root.to_dict())
# >>>
# {'right': None, 
#  'parent': None,
#  'left': {'right': {'right': None, 
#                     'parent': 7, 
#                     'left': None, 
#                     'value': 9}, 
#           'parent': 10, 
#           'left': None, 
#           'value': 7}, 
#  'value': 10}


class NamedSubTree(ToDictMixin):
    def __init__(self, name, tree_with_parent):
        self.name = name
        self.tree_with_parent = tree_with_parent

my_tree = NamedSubTree('foobar', root.left.right)
print(my_tree.to_dict())
# >>>
# {'tree_with_parent': {'right': None, 
#                       'parent': 7, 
#                       'left': None, 
#                       'value': 9}, 
#  'name': 'foobar'}


import json
class JsonMixin(object):
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)
    
    def to_json(self):
        return json.dumps(self.to_dict())


class DatacenterRack(ToDictMixin, JsonMixin):
    def __init__(self, switch=None, machines=None):
        self.switch = Switch(**switch)
        self.machines = [
            Machine(**kwargs) for kwargs in machines]


class Switch(ToDictMixin, JsonMixin):
    def __init__(self, ports=None, speed=None):
        self.ports = ports
        self.speed = speed


class Machine(ToDictMixin, JsonMixin):
    def __init__(self, cores=None, ram=None, disk=None):
        self.cores = cores
        self.ram = ram
        self.disk = disk


serialized = """{
    "switch": {"ports": 5, "speed": 1e9},
    "machines": [
        {"cores": 8, "ram": 32e9, "disk": 5e12},
        {"cores": 4, "ram": 16e9, "disk": 1e12},
        {"cores": 2, "ram": 4e9, "disk": 500e9}
    ]
}"""

deserialized = DatacenterRack.from_json(serialized)
roundtrip = deserialized.to_json()
assert json.loads(serialized) == json.loads(roundtrip)