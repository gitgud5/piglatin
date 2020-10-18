"""
Python code to Convert English Sentences to Pig Latin
"""
import sys


def main():
    sentence = input("What secret message you want to give?\n")
    lis = sentence.split()
    for i in range(len(lis)):
        if any(j.isdigit() for j in lis[i]):
            continue
        elif (lis[i].lower().startswith('a')) or (lis[i].lower().startswith('e')) or (
                lis[i].lower().startswith('i')) or (
                lis[i].lower().startswith('o')) or (lis[i].lower().startswith('u')):
            lis[i] = changeWithVowel(lis[i])
        else:
            lis[i] = changeWithConsonant(lis[i])
    print(" ".join(lis), file=sys.stderr)


def changeWithVowel(sentence):
    """
    Takes word which starts with Vowel and converts it to pig latin
    and returns it

    :rtype: String object
    """
    return sentence.lower() + "way"


def changeWithConsonant(sentence):
    """
    Take word which starts with a consonant and converts it to pig latin
    and returns it

    :rtype: object
    """
    a = sentence[0].lower() + "ay"
    return sentence[1:].lower() + a


if __name__ == '__main__':
    main()
