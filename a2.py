from typing import List

#the goal of this assignment is to create a function(match) that matches words in the source
#with words in the pattern

#_ can match any single word
#% can match a sequence of zero or more words

#match should return either None or a list of substitutions if the source doesn't match the
#pattern

def match(pattern: List[str], source: List[str]) -> List[str]:
    #pattern is a list of strings
    #source is ALSO a list of strings
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE A list of matched words
        (words in the source corresponding to _'s or %'s, in the pattern, if any)
    """
    sind = 0  # current index we are looking at in source list
    pind = 0  # current index we are looking at in pattern list
    result: List[str] = []  # to store substitutions we will return if matched
    accumulator = ""
    accumulating = False
    
    # keep checking as long as we haven't hit the end of either pattern or source while
    # pind is still a valid index OR sind is still a valid index (valid index means that
    # the index is != to the length of the list)
    while sind < len(source) or pind < len(pattern):
        
            
        #1)if we reached the end of the pattern but not source
        #if the source is longer than the pattern
        if pind >= len(pattern):
            print('you have reached the end of the pattern but not the source')
            return None
        
        #2)if the current thing in the pattern is a %       
        elif pattern[pind] == '%':
            if pind == (len(pattern)-1):
                result = result + [" ".join(source[sind:])]
                return result
                
            else:
               accumulator = ""
               pind = pind + 1
               while pattern[pind] != source[sind]:
                   accumulator += " " + source[sind]
                   sind = sind + 1
                   if sind >= len(source):
                       return None
               result.append(accumulator.strip())        
            
        
        #3)if we reached the end of the source but not the pattern
        #if the pattern is longer than the source
        elif sind >= len(source):
            print('you have reached end of the source but not the pattern')
            return None
        
        #4)if the current thing in the pattern is an _
        elif pattern[pind] == "_":
            result.append(source[sind])
            #you must advance sind and pind
            sind = sind + 1
            pind = pind + 1

##        elif pattern[pind] == "_":
##            result.append(source[sind])
##            #you must advance sind and pind
##            sind = sind + 1
##            pind = pind + 1                      
        
        
        #assert 2
        
        #5)if the current thing in the pattern is the same as the current thing in the source
        elif source[sind] == pattern[pind]:
            sind = sind + 1
            pind = pind + 1
                        
            print('#5 works')
            
        #6)else this will happen if none of the other conditions are met it indicates the current thing it pattern doesn't match the current thing
        #in source
        else: 
            return None
    return result
        
        

    

        
        
        # 1) if we reached the end of the pattern but not source

        # 2) if the current thing in the pattern is a %
        # WARNING: this condition contains the bulk of the code for the assignment
        # If you get stuck on this one, we encourage you to attempt the other conditions
        #   and come back to this one afterwards

        # 3) if we reached the end of the source but not the pattern

        # 4) if the current thing in the pattern is an _

        # 5) if the current thing in the pattern is the same as the current thing in the
        # source

        # 6) else : this will happen if none of the other conditions are met it
        # indicates the current thing it pattern doesn't match the current thing in
        # source

##    if accumulating == True:
##        result.append(accumulator)
##    return result


##if __name__ == "__main__":
##    assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"
##    assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"
##    assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"
##    assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"
##    print("passed 4")
##    assert match(["x", "_", "z"], ["x", "y", "z"]) == ["y"], "test 5 failed"
##    print("passed 5")
##    assert match(["x", "_", "_"], ["x", "y", "z"]) == ["y", "z"], "test 6 failed"
##    print("passed 6")
##    assert match(["%"], ["x", "y", "z"]) == ["x y z"], "test 7 failed"
##    print("passed 7")
##    assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "test 8 failed"
##    print("passed 8")
##    assert match(["%", "z"], ["x", "y", "z"]) == ["x y"], "test 9 failed"
##    print("passed 9")
##    assert match(["x", "%", "y"], ["x", "y", "z"]) == None, "test 10 failed"
##    print("passed 10")
##    assert match(["x", "%", "y", "z"], ["x", "y", "z"]) == [""], "test 11 failed"
##    print("passed 11")
##    assert match(["x", "y", "z", "%"], ["x", "y", "z"]) == [""], "test 12 failed"
##    print("passed 12")
##    assert match(["_", "%"], ["x", "y", "z"]) == ["x", "y z"], "test 13 failed"
##    print("passed 13")
##    assert match(["_", "_", "_", "%"], ["x", "y", "z"]) == ["x","y","z","",], "test 14 failed"
##    print("passed 14")
##
##    # this last case is a strange one, but it exposes an issue with the way we've
##    # written our match function
##    assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"
##    print("passed 15")
##
##    assert match(["x", "%", "z", "%"], ["x", "a", "a", "z", "a", "a"]) == ["a a", "a a"], "test 16 failed"
##    print("passed 16")
##
##
##    print("All tests passed!")

    ##        elif pattern[pind] == '%':
##            if result [-1][0] != "~":
##                result.append("~")
##        else:
##            result.append("~")
##
##            if sind < len(source):
##                result[-1] += " " + source[sind]
##
##            if (pind + 1 < len(pattern)) & (sind + 1 < len(source)):
##                result[-1] = result[-1][2:]
##                pind = pind + 1
##            elif (pind + 1 < len(pattern)) and (sind + 1 == len(source)):
##                pattern.pop(pind)
##                if pattern == scource:
##                    result = [""]
##                    break
##                else:
##                    return None
##                    break
##            elif (pind + 1 >= len(pattern)) & (sind + 1 >= len(source)):
##                result[-1] = result [-1][2:]
##                break
##            sind = sind + 1

                    
##        elif pattern[pind] == '%':
##            accumulator = ""
##            pind = pind + 1
##            accumulating = True
##            if pind >= len(pattern):
##                if accumulating == True:
##                    for index in source:                        
##                        if sind >= pind:
##                            accumulator = accumulator + " " + source[sind]
##                            sind = sind + 1
##                           sind = sind + 1
##                        else:
##                            accumulator = source[sind]
##                            sind = sind + 1
####                            
####                   accumulator = source[sind] + accumulator
####                   sind = sind + 1
##                                    
##            else:
##                accumulator = accumulator + source[sind]
##                sind = sind + 1
##                
####                        
##                
##                return None
            
           
        
