# def solver(a, b, c):
#     d = b**2 - 4*a*c
#     if d < 0:
#         return []
#     if d == 0:
#         if a == 0:
#             return []
#         return [-b / (2*a)]
#     solutions = [(-b + d**0.5) / (2*a), (-b - d**0.5) / (2*a)]
#     solutions.sort()
#     return solutions
        
#Trying to use lambdas
def solver(a, b, c):
    boolean = {True : lambda a, b : [], False : lambda a, b : [-b / (2*a)]}
    d = b**2 - 4*a*c
    x = lambda *_ : [] * int(d < 0) + boolean[a == 0](a, b) * int(d == 0) + z() * int(d > 0)
    z = lambda *_ : [(-b + d**0.5) / (2*a), (-b - d**0.5) / (2*a)]
    solutions = x()
    solutions.sort()
    return solutions

print(solver(1, 2, 0))