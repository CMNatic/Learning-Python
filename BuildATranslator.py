# Our Own Languge
# vowels -> g
# e.g. dog -> dgg
# cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        # if there is a vowel, add "g" to translation
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        # if no vowel, add the letter to translation
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase to translate: ")))
