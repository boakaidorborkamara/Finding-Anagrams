# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    
    # convert to dictionary 
    word1 = list(word1)
    word2 = list(word2)


    # sort both words
    word1.sort()
    word2.sort()


    # check if both words have the same lenght
    if len(word1) == len(word2):
       
        #check if all letters are similar
        for letter in word1:

            # compare letters in word1 and word2 letter by letter 
            similar_letters = letter in word2
            if similar_letters == False:
                return False #return False if a letter is different
        
        # return true if all letters are similar 
        return True

    else:
        #return False if one word has more characher than the other
        return False

      


print(find_anagrams("stop", "tops"))

