# text file random words
# returns counts of all unique words

# returns count of all words
def countUniqueWords(filename):
    file = open(filename, "r")
    outputDictionary = {}
    
    # keep track of key (word), value (count)
    # loop every line and separate by space
    for line in file:
        arrayOfWords = line.split()
        
        for word in arrayOfWords:
            lowercaseWord = word.lower()
            # checking if key exists
            # if not, then initialize with 1
            if lowercaseWord not in outputDictionary.keys():
                outputDictionary[lowercaseWord] = 1
                
            elif lowercaseWord in outputDictionary.keys():
                outputDictionary[lowercaseWord] = outputDictionary[lowercaseWord] + 1
    
    return outputDictionary

def countOfWord(word, filename):
    localDictionary = countUniqueWords(filename)
    
    count = localDictionary[word]
    
    return count
            
            
def test_countUniqueWords():
    # empty should return 0
    dictionary = {}
    output = countUniqueWords("empty.txt")
    assert dictionary == output, "empty case not passed"
    
    # special characters
    dictionary = {"@": 1}
    output = countUniqueWords("specialChar.txt")
    assert dictionary == output, "special character case not passed"
    
    print("Passed all tests")
    
# print(countUniqueWords("test.txt"))

# print(countOfWord("grape", "test.txt")) # 3

test_countUniqueWords()

