# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
    # +++your code here+++
    return_value = s
    if(len(s) >= 3):
        if(s[-3:] == 'ing'):
            return_value = s + 'ly'
        else:
            return_value = s + 'ing'
    return return_value


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):
    # +++your code here+++
    import re
    old = 'not.*bad'
    new = 'good'
    return_value = re.sub(old, new, s, flags=re.IGNORECASE)
    return return_value


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a, b):
    # +++your code here+++
    def is_even(s):
        num = len(s)
        return_val = num % 2 == 0
        return return_val
    
    def split_string(s):
        s_front = ''
        s_back = ''
        front_length = 0
        back_length = 0
        if(is_even(s)):
            front_length = int(len(s) / 2)
            back_length = front_length            
        else:
            front_length = int((len(s) // 2) + 1)
            back_length = front_length - 1

        s_front = s[0:front_length]
        s_back = s[-back_length:]
        
        return s_front, s_back

    a_vals = split_string(a)
    b_vals = split_string(b)

    return_value = a_vals[0] + b_vals[0] + a_vals[1] + b_vals[1]

    return return_value


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
