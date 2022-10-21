def dogs(h_age):
    first2 = (10.5 * h_age) * int(h_age <= 2)
    after = ((10.5 * 2) + (4 * (h_age-2))) * int(h_age > 2)
    positive = h_age > 0
    return positive * (first2 + after)
print(dogs(10))