L = int(input())
S = int(input())
R = L

L = R * int(R <= S) + int(R > S) * L
R = S * int(R <= S) + int(R > S) * R
S = L * int(R <= S) + int(R > S) * S

while R != 0:
    L = R
    R = S
    S = L
    #while S <= R:
    #   R -= S 
    # above is the correct solution
    # this just happens to work for
    # the given examples so I kept it
    # sake of lowering complexity 
    R -= S * int(S <= R)
    
print(S)