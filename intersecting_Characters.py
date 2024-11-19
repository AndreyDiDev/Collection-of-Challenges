# Given a string array words, 
# return an array of all characters that show up in all 
# strings within the words (including duplicates). You may return the answer in any order.
def IntersectionOfLetters(array_words):
    output = []
    
    # edge cases:
    if(len(array_words)== 0):
        return output
    
    firstWord = array_words[0]
    
    for character in firstWord:
        # print(character)
        counterCharacterFound = 0
        # iterate through every word
        for word in array_words:
            found = False
            # for every character in that word as long we find one matching we continue 
            # print(word)
            for characterOther in word:
                if(found != True):
                    if(character == characterOther):
                        found = True
                        # print(word)
                        counterCharacterFound += 1
        
        if(counterCharacterFound == len(array_words)):
            output.append(character)
            i = 0
            for word in array_words:
                index = array_words[i].index(character)
                # index = stringWord.index(character)
                newWord = word[:index] + word[index + 1:]
                array_words[i] = newWord
                i += 1
                
                
    return output

# def characterToCheck(character):
#     #

# test
words = ["bella","label","roller"]
expectedOutput = ["e","l","l"]
output = IntersectionOfLetters(words)
assert output == expectedOutput, "wrong output"

words = ["cool","lock","cook"]
expectedOutput = ["c","o"]
output = IntersectionOfLetters(words)
assert output == expectedOutput, "wrong output"

words = ["sdlskdfkl","skdlfksdf","ewrioweri"]
expectedOutput = []
output = IntersectionOfLetters(words)
assert output == expectedOutput, "wrong output"

words = []
expectedOutput = []
output = IntersectionOfLetters(words)
assert output == expectedOutput, "wrong output"

words = ["", "sd", "ta"]
expectedOutput = []
output = IntersectionOfLetters(words)
assert output == expectedOutput, "wrong output"

words = ["@", "@", "@"]
expectedOutput = ["@"]
output = IntersectionOfLetters(words)
assert output == expectedOutput, "wrong output"

words = ["1", "1", "1"]
expectedOutput = ["1"]
output = IntersectionOfLetters(words)
assert output == expectedOutput, "wrong output"

print("All tests passed")