myfile = open('myfile.txt')
text = myfile.read()

numSentences = 0
numWords = 0
numSyllables = 0

alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
consonants = ("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ")
char = (".;:?!")
char2 = (".;:?! ")
vowels = ("aeiouyAEIOUY")
             
inSentence = False
inWord = False
inSyllable = False

for x in text: 
    if inSentence == True:        
        if x in alphabet:    
            inSentence == True
    else:
        if x in char:   
            inSentence == False
            numSentences += 1
            
for x in text: 
    if inWord == True:
        if x in alphabet:
            inWord == True
    else:
        if x in char2:   
            inWord == False
            numWords += 1

for x in text: 
    if inSyllable == True:
        if x in consonants or x in char2:
            inSyllable == True
    else:
        if x in vowels:   
            inSyllable == False
            numSyllables += 1

readability = 206.835 - 1.015 * (numWords / numSentences) - 84.6 * (numSyllables / numWords)

print("Syllables:     ", numSyllables)
print("Words:         ", numWords)
print("Sentences:     ", numSentences)
print("Readability:   ", readability)
