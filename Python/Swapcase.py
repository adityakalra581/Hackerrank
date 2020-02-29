
# SWAPCASE:
# Swapping Uppercase and Lowercase characters.

def swap_case(s):
    c = s.swapcase() 
    return c

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
