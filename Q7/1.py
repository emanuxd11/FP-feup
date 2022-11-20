def switch_dict(adict):
    new_dict = {}
    for k, v in adict.items():
        if v not in new_dict:
            new_dict[v] = []
        new_dict[v].append(k)

    return new_dict

print(switch_dict({"jan": "winter", "feb": "winter", "may": "spring", "july": "summer", "august": "summer"}))