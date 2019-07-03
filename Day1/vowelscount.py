word = input("Enter a word").lower()
lst = list(word)
vowels = list('aeiou')
vowelsCount = 0
for letter in lst:
    if letter in vowels:
        vowelsCount += 1

print(f"vowelsCount is {vowelsCount}")
