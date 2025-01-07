class Solution:       
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        def reverse_num(x):
            rev_num = 0

            while x != 0:
                last_digit = x % 10
                rev_num = (rev_num * 10) + last_digit
                x = x // 10
            
            return rev_num

        if reverse_num(x) == x:
            return True
        else:
            return False