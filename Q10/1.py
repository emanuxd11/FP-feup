def square_odds(values):
    values = values.split(',')
    values = list(map(lambda x : int(x), values))
    values = [n**2 for n in values if n**2 % 2 != 0]
    values = list(map(lambda x : str(x), values))
    return ','.join(values)
    
print(square_odds("1,2,3,4,5,6,7,8,9"))