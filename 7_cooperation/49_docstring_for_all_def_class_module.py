
# http://ipython.org
# http://sphinxdoc.org
# https://readthedocs.org
# http://www.python.org/dev/peps/pep-0257
def palindrome(word):
    """Return True if the given word is a palindrome."""
    return word == word[::-1]

print(repr(palindrome.__doc__))


# 1) module documentation
# words.py
#!/usr/bin/env python3
"""Library for testing words for various linguistic patterns.
Testing how words relate to each other can be tricky sometimes!
This module provides easy ways to determine when words you've
found have special properties.
Available functions:
- palindrome: Determine if a word is a palindrome.
- check_anagram: Determine if two words are anagrams.
...
"""

# ...


# 2) class documentation
class Player(object):
    """Represents a player of the game.

    Subclasses may override the 'tick' method to provide
    custom animations for the player's movement depending
    on their power level, etc.
    
    Public attributes:
    - power: Unused power-ups (float between 0 and 1).
    - coins: Coins found during the level (integer).
    """

    # ...


# 3) function documentation
import itertools
def find_anagrams(word, dictionary):
    """Find all anagrams for a word.

    This function only runs as fast as the test for
    membership in the 'dictionary' container. It will
    be slow if the dictionary is a list and fast if
    it's a set.

    Args:
        word: String of the target word.
        dictionary: Container with all strings that
            are known to be actual words.
    Returns:
        List of anagrams that were found. Empty if
        none were found.
    """
    permutations = itertools.permutations(word, len(word))
    possible = (''.join(x) for x in permutations)
    found = {word for word in possible if word in dictionary}
    return list(found)

assert find_anagrams('pancakes', ['scanpeak']) == ['scanpeak']


# need them to describe ..
# Module: important class and function
# Class: class behavior, important attribute, subclass behavior, etc..
# Function and Method: args, return, exception and other behaviors