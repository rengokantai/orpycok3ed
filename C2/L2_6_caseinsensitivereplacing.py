__author__ = 'Hernan Y.Ke'
import re

# basic flags=re.IGNORECASE
sen = "Dog DOG dog"
print(re.findall('dog', sen, flags=re.IGNORECASE))
print(re.sub('dog', 'cat', sen, flags=re.IGNORECASE))    #oldpattern, newpattern, word, flag


# passing callback

def subcat(word):           # word -> word want to substitute
    def replace(m):         # m -> all matched words (array)
        text = m.group()        # text-> single matched word
        if text.isupper():
            return word.upper()
        else:
            return word
    return replace

print(re.sub('dog', subcat('cat'), sen, flags=re.IGNORECASE))