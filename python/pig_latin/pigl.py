def instruction():
    import time
    time.sleep(1)
    print "".join(["\nPig latin game:\n",
        "Give me a sentence, and I will give you its encrypted\n",
        "pig-latin form.\n",
        "What is your sentence?\n",
        '(To quit this game, simply press the "Enter" key)'])

def checkDictionary(word, lang = "en-US"):
    # To install enchant on raspberry pi:
    # $ sudo apt-get install enchant
    # $ sudo apt-get install python-pip
    # $ pip install pyenchant
    import enchant
    d = enchant.Dict(lang)
    if not d.check(word):
        raise ValueError(
            "{} is not a valid word.".format(word))

def isVowel(letter):
    return letter in "aeiouAEIOU"

# Give me a word, and I will give you its encrypted
# pig-latin form
def piglWord(word):
    if len(word) == 0:
        return ""

    punc = ''
    if not word[-1].isalpha():
        punc = word[-1]
        word = word[:-1]

    checkDictionary(word)

    isCapital = word[0].isupper()
    word = word.lower()
    if isVowel(word[0]):
        pigl =  word + "way"
    else:
        pigl = word[1:] + word[0] + "ay"

    if isCapital:
        pigl = pigl[0].upper() + pigl[1:]

    pigl += punc
    return pigl

# Get the first word of a sentence,
# or the first letter of a word
def first(sentence):
    if len(sentence) == 0:
        return ""
    elif " " not in sentence:
        return sentence[0]
    else:
        return sentence.split(" ")[0]

def butFirst(sentence):
    if len(sentence) == 0:
        return ""
    elif " " not in sentence:
        return sentence[1:]
    else:
        return " ".join(sentence.split(" ")[1:])

# Give me a sentence, and I will give you its encrypted
# pig-latin form
def piglSentence(sentence):
    if " " not in sentence:
        return piglWord(sentence)
    else:
        return ' '.join([piglWord(first(sentence)),
            piglSentence(butFirst(sentence))])

def pigLatinGame(shouldEchoInput = True):
    while True:
        instruction()
        if shouldEchoInput:
            sentence = raw_input()
        else:
            import getpass
            sentence = getpass.getpass('')
        if sentence == "":
            break
        try:
            print(piglSentence(sentence))
        except ValueError as e:
            print(e)


def main():
    pigLatinGame(shouldEchoInput = True)

if __name__ == "__main__":
    main()
