def palindrome_index(s, i = 0):
    def palindrome(s):
        return s[::-1] == s
    def ind(s, i):
        return list(s).index(s[i - 1])
    def nvr_alr(a, b):
        return -1
    removed = list(s)
    del removed[i]
    return [[[palindrome_index, ind][palindrome(removed)], 
    nvr_alr][bool(i + 1 == len(s) * (not palindrome(removed)))], 
    nvr_alr][palindrome(s)](s, i + 1)
    
print(palindrome_index('tattarrattat'))