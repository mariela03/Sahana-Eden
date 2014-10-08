import math

'''
Created on Oct 8, 2014

@author: Jie
'''

'''Takes in a file with the 1st word in each line as a
abbreviation, the words after are full length words.
Creates a dictionary with the 1st word in each line '''

def abbr(lstdict,lsttext):
    dict = {}
    for part in lstdict:
        for other in range(1,len(part)):
            dict[part[other]] = part[0]
    #print dict
    for word in range(len(lsttext)):
        for x in dict.keys():
            if x == lsttext[word]:
                lsttext[word] = dict[x]
    finalstr = ""
    for part in lsttext:
        finalstr += part + " "
    #print finalstr.strip()
    return finalstr.strip()

#unintelligent string parsing, split into chunks regardless of spaces
def generate_list(text, chunklength):
    slist = []
    num_chunks = int(math.ceil(len(text)/chunklength))
    for i in range(num_chunks):
        index = i * chunklength
        if index + chunklength >= len(text): slist.append( text[index:] )
        else: slist.append( text[index:index+chunklength])
    return slist

if __name__ == '__main__':
    lstdict = []
    with open("abbtest.txt", "r") as f:
        for line in f:
            lstdict.append(line.split())
    lsttext = []
    with open("textfile.txt", "r") as f:
        for line in f:
            lsttext.append(line.split())
    abbrtext = abbr(lstdict,lsttext[0])
    print generate_list(abbrtext, 10)


