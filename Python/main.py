####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1])  True
# arrayCheck([1, 1, 2, 4, 1]) False
# arrayCheck([1, 1, 2, 1, 2, 3]) True

def arrayCheck(nums):
    for i in range(len(nums) - 2):
        if(nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
            return True
    return False

print("ArrayCheck: ", arrayCheck([1, 1, 2, 1, 2, 3]))


#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') 'Hlo'
# stringBits('Hi') 'H'
# stringBits('Heeololeo') 'Hello'

def stringBits(str):
    x = ""
    for i in range(0, len(str), 2):
        x += str[i]
    print("String Bits: ", x)

stringBits('Heeololeo')


#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') True
# end_other('AbC', 'HiaBc') True
# end_other('abc', 'abXabc') True


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if(len(a) <= len(b)):
        return b[len(b)-len(a):] == a
    else:
        return a[len(a)-len(b):] == b


print("End_Other: ", end_other('AbCD', 'HiaBc'))



#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') 'TThhee'
# doubleChar('AAbb') 'AAAAbbbb'
# doubleChar('Hi-There') 'HHii--TThheerree'

def doubleChar(str):
    ans = ''
    for c in str:
        ans += c*2
    return ans

print("Double Char:", doubleChar('Hi-There'))



#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) 6
# no_teen_sum(2, 13, 1) 3
# no_teen_sum(2, 1, 14) 3

def no_teen_sum(a, b, c):
    sum = 0
    if(not fix_teen(a)):
        sum += a
    if(not fix_teen(b)):
        sum += b
    if(not fix_teen(c)):
        sum += c
    return sum


def fix_teen(n):
    return n != 15 and n != 16 and n >= 13 and n <= 19

print("Prob 5", no_teen_sum(1, 2, 15))


#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) 3
# count_evens([2, 2, 0]) 3
# count_evens([1, 3, 5]) 0

def count_evens(nums):
    ans = len(list(filter(lambda num: num%2 == 0, nums)))
    return ans

print("Count Evens", count_evens([1, 3, 5]))
