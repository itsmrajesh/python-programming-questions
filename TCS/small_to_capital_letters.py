def make_upper_case(word):
    """Converts the given word to upper without using ''.upper() method """
    word_upper = ""
    for ch in word:
        if ord("a") <= ord(ch) <= ord("z"):
            word_upper += chr(ord(ch) - 32)
            # chr(ASCII) takes ASCII as a argument returns that character example for 99 it returns c
            # ord(character) takes character as a argument return ASCII value example for ord("A") returns 65
        else:
            word_upper += ch

    return word_upper


data = input()
res = make_upper_case(data)

print(res)
