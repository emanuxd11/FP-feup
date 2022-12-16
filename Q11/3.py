def search_tree(key, tree):
    searched_list = []

    def aux(aux_tree):
        if aux_tree == None:
            return None

        left = aux_tree[2]
        right = aux_tree[3]

        searched_list.append(aux_tree[0])
        if aux_tree[0] == key:
            return (aux_tree[1], searched_list)

        if left == None and right == None:
            return None
        
        if left and left[0] == key:
            searched_list.append(left[0])
            return (left[1], searched_list) 
        elif right and right[0] == key:
            searched_list.append(right[0])
            return (right[1], searched_list)
        else:
            if left and left[0] < key:
                return aux(right)
            elif right and right[0] > key:
                return aux(left)
            else:
                return None
    
    return aux(tree)

	
tree = ('c', 3, ('b', 2, ('a', 1, None, None), None), ('e', 5, ('d', 4, None, None), None))
print(search_tree('a', tree)) # 1, c , b, a para o 'a'
# com f devia dar None
