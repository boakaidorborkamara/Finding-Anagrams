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

    print(word1)
    print(word2)

    # check if both words have the same lenght
    if len(word1) == len(word2):
        print("equal")
    # for letter in word1:
    #     print(letter)
       
    #     similar_text = letter in word2
    #     print(similar_text)

    #     if validator == False:
    #         print("not anagram")

  

    # return True 

find_anagrams("rat", "cat")

