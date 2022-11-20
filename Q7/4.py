def isomorphic(astring1, astring2):
    mapping1 = {}
    mapping2 = {}

    for i in range(len(astring1)):
        if astring1[i] in mapping1:
            if mapping1[astring1[i]] != astring2[i]:
                return f"\'{astring1}\' and \'{astring2}\' are not isomorphic"
        if astring2[i] in mapping2:
            if mapping2[astring2[i]] != astring1[i]:
                return f"\'{astring1}\' and \'{astring2}\' are not isomorphic"
        
        mapping1[astring1[i]] = astring2[i]
        mapping2[astring2[i]] = astring1[i]

    return f"\'{astring1}\' and \'{astring2}\' are isomorphic because we can map: {list(tuple(mapping1.items()))}"
        
print(isomorphic('turtle', 'tletur'))