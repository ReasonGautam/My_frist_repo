# ===================== PYTHON OPERATORS (NOTES) =====================

# Operator = symbol that does something on values
# Operand  = the value the operator works on
# Example: 10 + 5  ->  10 and 5 are operands, + is the operator
#
# Unary  = 1 operand   -> -5, not True
# Binary = 2 operands  -> 3 + 4, x == y


# ---------------------- 1. Arithmetic operator ----------------------
# + = add (also joins strings: "a" + "b" -> "ab")
# - = minus
# * = multiply (also repeats strings: "ab" * 2 -> "abab")
# / = divide, ALWAYS gives a float -> 4 / 2 = 2.0
# // = floor divide, divides and rounds DOWN to the nearest whole number
# % = modulus, gives the remainder
# ** = power

print(7 / 2)     # 3.5
print(7 // 2)    # 3
print(-7 // 2)   # -4  (rounds DOWN, not towards zero)
print(7 % 3)     # 1
print(2 ** 10)   # 1024
print(64 ** 0.5) # 8.0 (square root)

# % is useful for even/odd: 10 % 2 -> 0 (even), 7 % 2 -> 1 (odd)


# ---------------------- 2. Comparison operator ----------------------
# Always gives True or False
# == equal, != not equal, > greater, < less, >= greater or equal, <= less or equal

print(5 == 5)    # True
print(5 != 3)    # True
print(7 > 3)     # True

# Chaining works in Python
x = 5
print(1 < x < 10)  # True

# Strings are compared letter by letter, and case matters
print("apple" < "banana")    # True
print("Python" == "python")  # False


# ---------------------- 3. Assignment operator ----------------------
# = stores a value in a variable
# Short forms: x += 3 means x = x + 3
# Same for -=  *=  /=  //=  %=  **=

score = 50
score += 10   # 60
score *= 2    # 120
print(score)  # 120

# Multiple assignment
a, b = 10, 20
a, b = b, a   # swap values, no extra variable needed
print(a, b)   # 20 10


# ---------------------- 4. Logical operator ----------------------
# and = True only if BOTH are True
# or  = True if AT LEAST ONE is True
# not = flips True/False

age = 20
has_id = True
print(age >= 18 and has_id)  # True
print(True or False)         # True
print(not True)              # False

# Short-circuit: Python stops early if the answer is already known
print(False and 1/0)  # False (right side never runs, so no error)
print(True or 1/0)    # True


# ---------------------- 5. Bitwise operator ----------------------
# Works on the binary (0 and 1) form of numbers
# 5 = 0101, 3 = 0011
# & = AND, 1 only where both bits are 1  -> 5 & 3 = 1
# | = OR, 1 where either bit is 1        -> 5 | 3 = 7
# ^ = XOR, 1 where bits are different    -> 5 ^ 3 = 6
# ~ = NOT, flips bits                    -> ~5 = -6
# << = left shift, x2 each shift         -> 5 << 1 = 10
# >> = right shift, /2 each shift        -> 20 >> 1 = 10

print(bin(5))   # 0b101  (bin() shows the binary form)
print(5 & 3)    # 1
print(5 | 3)    # 7
print(5 ^ 3)    # 6
print(5 << 1)   # 10
print(20 >> 2)  # 5


# ---------------------- 6. Membership operator ----------------------
# It is: in, and not in
# in checks if the value is present or not, and vice versa for not in
# for example: "a" in "apple" -> True

print("py" in "python")     # True
print("Java" in "python")   # False
print("z" not in "hello")   # True


# ---------------------- 7. Identity operator ----------------------
# It is: is, and is not
# is checks if both are the exact same object in memory, and vice versa for is not
# == checks if VALUES are equal, is checks if it is the SAME object

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)  # True  (same values)
print(a is b)  # False (different objects)
print(a is c)  # True  (c points to a)

# Always use "is" to check None
x = None
print(x is None)      # True
print(x is not None)  # False


# ---------------------- 8. Operator precedence ----------------------
# Which operator runs first (high to low):
# 1. ( )                        brackets
# 2. **                         power (runs right to left: 2 ** 3 ** 2 = 512)
# 3. +x -x ~x                   unary
# 4. * / // %
# 5. + -
# 6. << >>
# 7. &
# 8. ^
# 9. |
# 10. == != > < >= <= is in     comparison, identity, membership
# 11. not
# 12. and
# 13. or                        lowest
#
# Same level -> runs left to right
# Not sure? Use brackets ( )

print(2 + 3 * 4)    # 14 (* first)
print((2 + 3) * 4)  # 20 (brackets first)
print(2 ** 3 ** 2)  # 512
print(not True or True)  # True (not before or)