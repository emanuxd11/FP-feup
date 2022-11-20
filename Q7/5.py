def check_results(bet, results):

    def get_result(result):
        if result[2] > result[3]:
            return '1'
        elif result[2] < result[3]:
            return '2'
        else:
             return 'X'

    hits = 0
    for i in range(13):
        if bet[i] == get_result(results[i]):
            hits += 1
    
    return hits

print(check_results("XX121X221X122", [("Team A","Team B",0,0),
    ("Team C","Team D",2,1), ("Team E","Team F",0,4), 
    ("Team G","Team H",1,1), ("Team I","Team J",2,2), 
    ("Team K","Team L",2,0), ("Team M","Team N",1,0), 
    ("Team O","Team P",0,1), ("Team Q","Team R",0,0), 
    ("Team S","Team T",3,1), ("Team U","Team V",2,3), 
    ("Team X","Team Z",2,2), ("Team W","Team Y",1,5)]))