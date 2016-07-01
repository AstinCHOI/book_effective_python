
class FrequencyList(list):
    def __init__(self, members):
        super(FrequencyList, self).__init__(members)
    
    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts

foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print('Length is', len(foo))
foo.pop()
print('After pop:', repr(foo))
print('Frequency:', foo.frequency())
# >>>
# ('Length is', 7)
# ('After pop:', "['a', 'b', 'a', 'c', 'b', 'a']")
# ('Frequency:', {'a': 3, 'c': 1, 'b': 2})


class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

bar = [1, 2, 3]
bar[0] # == bar.__getitem__(0)


class IndexableNode(BinaryNode):
    def _search(self, count, index):
        found = None
        if self.left:
            found, count = self.left._search(count, index)
        if not found and count == index:
            found = self
        else:
            count += 1
        if not found and self.right:
            found, count = self.right._search(count, index)
        return found, count
    
    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError('Index out of range')
        return found.value

tree = IndexableNode(
    10,
    left=IndexableNode(
        5,
        left=IndexableNode(2),
        right=IndexableNode(
            6,
            right=IndexableNode(7))),
    right=IndexableNode(
        15,
        left=IndexableNode(11)))

print('LRR =', tree.left.right.right.value)
print('Index 0 = ', tree[0])
print('Index 1 = ', tree[1])
print('11 in the tree', 11 in tree)
print('17 in the tree', 17 in tree)
print('Tree is', list(tree))
# >>>
# ('LRR =', 7)
# ('Index 0 = ', 2)
# ('Index 1 = ', 5)
# ('11 in the tree', True)
# ('17 in the tree', False)
# ('Tree is', [2, 5, 6, 7, 10, 11, 15])


# len(tree)
# TypeError: object of type 'IndexableNode' has no len()

class SequenceNode(IndexableNode):
    def __len__(self):
        _, count = self._search(0, None)
        return count

tree = SequenceNode(
    10,
    left=SequenceNode(
        5,
        left=SequenceNode(2),
        right=SequenceNode(
            6,
            right=SequenceNode(7))),
    right=SequenceNode(
        15,
        left=SequenceNode(11)))

print('Tree has %d nodes' % len(tree))
# >>>
# Tree has 7 nodes


# python3
# alert for not implementing methods
# in order to implement methods rightly.
from collections.abc import Sequence

class BadType(Sequence):
    pass

# foo = BadType()
# TypeError: Can't instantiate abstract class BadType with abstract methods __getitem__, __len__


class BetterNode(SequenceNode, Sequence):
    pass

tree = BetterNode(
    10,
    left=BetterNode(
        5,
        left=BetterNode(2),
        right=BetterNode(
            6,
            right=BetterNode(7))),
    right=BetterNode(
        15,
        left=BetterNode(11)))

print('Index of 7 is', tree.index(7))
print('Count of 10 is', tree.count(10))
# >>>
# Index of 7 is 3
# Count of 10 is 1