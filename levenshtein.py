def levenshtein(string1, string2):
    if len(string1)==0:
        return len(string2)
    if len(string2)==0:
        return len(string1)
    firstHead=string1[0]
    secondHead=string2[0]
    firstTail=string1[1:]
    secondTail=string2[1:]
    if firstHead==secondHead:
        
        return levenshtein(firstTail,secondTail)
        
    else:
        firstOption=levenshtein(firstTail, string2)
        secondOption=levenshtein(firstTail,secondTail)
        thirdOption=levenshtein(string1,secondTail)
        return min(firstOption, secondOption, thirdOption)+1
    
print(levenshtein("kitten", "sitting"))
