def replace_rec(old_ch, new_ch, astring):
    if astring == "":
        return ""
    if astring[0] == old_ch:
        return new_ch + replace_rec(old_ch, new_ch, astring[1:])
    return astring[0] + replace_rec(old_ch, new_ch, astring[1:])

    

print(replace_rec("e", "_", "these are the best days"))
