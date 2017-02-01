"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""
def tim(burrito):
    CipherText = ""
    for i in burrito:
        if i == "a":
            CipherText = CipherText + "#"
        elif i == "b":
            CipherText = CipherText + "$"
        elif i == "c":
            CipherText = CipherText + "%"
        elif i == "d":
            CipherText = CipherText + "^"
        elif i == "e":
            CipherText = CipherText + "&"
        elif i == "f":
            CipherText = CipherText + "*"
        elif i == "g":
            CipherText = CipherText + "@"
        elif i == "h":
            CipherText = CipherText + "+"
        else:
            CipherText = CipherText + i
    return CipherText
print(tim('Computer Science Makes the World go round but it doesn/t make the world round itself!'))

"""Write an encryption code that you make up and run it for the variable NoVowels"""
def pen(taco):
    CipherText = ""
    for i in taco:
        if i == "s":
            CipherText = CipherText + "#"
        elif i == "t":
            CipherText = CipherText + "%"
        elif i == "s":
            CipherText = CipherText + "^"
        elif i == "x":
            CipherText = CipherText + "&"
        elif i == "w":
            CipherText = CipherText + "*"
        elif i == "y":
            CipherText = CipherText + "@"
        elif i == "z":
            CipherText = CipherText + "+"
        else:
            CipherText = CipherText + i
    return CipherText
print(pen('stop at the stop sign'))
