def rm_letter_rev(ch, s):
    s = s[::-1]
    s = [char for char in s if char != ch]
    s = "".join(s)
    return s
    
print(rm_letter_rev("a", "hallo"))