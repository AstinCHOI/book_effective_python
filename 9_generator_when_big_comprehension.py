
value = [len(x) for x in open('9_generator_expression_when_big_comprehension.py')]
print(value)
# >>>
# [1, 83, 13, 6, 14, 1, 80, 10, 16, 16, 6, 46, 4, 5, 1, 34, 18]

it = (len(x) for x in open('9_generator_expression_when_big_comprehension.py'))
print(it)
print(next(it))
print(next(it))
# >>>
# <generator object <genexpr> at 0x1006ef140>
# 1
# 83

roots = ((x, x**0.5) for x in it)
print(next(roots))
# >>>
# (13, 3.605551275463989)
