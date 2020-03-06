#find whether an integer is palindrome, without converting it to string
def isPalindrome(x):
    new_list = list()
    while x:
        new_list.append(int(x % 10))
        x = x // 10

    x = new_list
    last = len(x) - 1
    first = 0
    while first <= last:
        if x[first] != x[last]: return False
        first += 1
        last -= 1

    return True


print('is palindrome:', isPalindrome(1234321))



