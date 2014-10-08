
import nltk.data

"""
Created October 8th, 2014 by Brandy Dettmer
Takes a string without any new line characters, with english sentences delimited by periods and
removes sentences that contain URLs
"""
def removeSentencesWithURLs(text):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    text = tokenizer.tokenize(text)

    output = ""
    for line in text:
        if "http" in line:
            continue
        output += line + ' '

    return output


# driver to test emoveSentencesWithURLs(text)
fname = "dummyTextFile3"
with open(fname) as f:
    content = f.readlines()

text = ""
# strips out new line characters
for line in content:
    text += line.rstrip()
print removeSentencesWithURLs(text)