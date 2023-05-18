def levenshtein(string1, string2):
    if len(string1)==0:
        return len(string2)
    if len(string2)==0:
        return len(string1)
    firstHead=string1[0]
    secondHead=string2[0]
    firstTail=string1[1:]
    secondTail=string2[1:]
    firstLargerTail=string1[1:]
    if firstHead==secondHead:
        
        return levenshtein(firstTail,secondTail)
        
    else:
        firstOption=levenshtein(firstTail, string2)
        secondOption=levenshtein(firstTail,secondTail)
        thirdOption=levenshtein(string1,secondTail)
        fourthOption=1000000
        if len(string1)>1 and len(string2)>1 and string1[0]==string2[1] and string1[1]==string2[0] and string1[0]!=string2[0]:
            firstSmallerTail=string1[2:]
            secondSmallerTail=string2[2:]
            fourthOption=levenshtein(firstSmallerTail, secondSmallerTail)

        
        return min(firstOption, secondOption, thirdOption,fourthOption)+1
    
        
print(levenshtein("kitten", "kittne"))
    
    
