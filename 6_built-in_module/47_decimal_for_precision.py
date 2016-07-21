
rate = 1.45
seconds = 3*60 + 42
cost = rate * seconds / 60
print(cost)
# >>>
# 5.364999999999999

print(round(cost, 2))
# >>>
# 5.36

rate = 0.05
seconds = 5
cost = rate * seconds / 60
print(cost)
# >>>
# 0.004166666666666667

print(round(cost, 2))
# >>>
# 0.0


from decimal import Decimal, ROUND_UP
rate = Decimal('1.45')
seconds = Decimal('222') #3*60 + 42
cost = rate * seconds / Decimal('60')
print(cost)
# >>>
# 5.365

rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)
# >>>
# 5.37


rate = Decimal('0.05')
seconds = Decimal('5')
cost = rate * seconds / Decimal('60')
print(cost)
# >>>
# 0.004166666666666666666666666667

rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)
# >>>
# 0.01


# Decimal calculates 1/3 for an approximate value
from fractions import Fraction # for precise fractions