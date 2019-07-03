words="how much wood would a woodchuck chuck if the woodchuck could chuck wood"
print(words)
wordsList=list()

def displayWords(data):
    for word in data:
        print(word,end=" ")
    print()    


for word in words.split(" "):
    wordsList.append(word)

uniqueWords=set()

for word in wordsList:
    uniqueWords.add(word)


wordsCount=dict()

for word in wordsList:
    wordsCount[word]=wordsCount.get(word,0)+1

print("*"*60)
print("Unique Words in given sentence :-")
displayWords(uniqueWords)
print("*"*60)
print("Each word Count")
print(wordsCount)
