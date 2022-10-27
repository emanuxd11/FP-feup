def mask_data(data, n_characters, position):
    if n_characters == 0:
        return data

    result = ""
    if position == "end":
        data = data[::-1]    
    for i in range(len(data)):
        if i < n_characters:
            result += '*'
        else:
            result += data[i]
    if position == "end":
        result = result[::-1]
    
    return result