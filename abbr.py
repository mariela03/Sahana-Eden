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

def generate_list(text, chunklength):
    slist=[]
    #split text into words
    len_chunk = 0
    chunk = ""
    words = text.split()
    for word in words:
        if len_chunk == 0:
            if len_chunk + len(word) >= chunklength: #word is too long, have to split it
                pass #finish this logic later
            else:
                chunk = word
                len_chunk = len(word)
                continue
        if len_chunk + len(word) + 1 >= chunklength:
            slist.append(chunk)
            chunk=word
            len_chunk = len(word)
        else:
            chunk+= " "+word
            len_chunk = len(word)+1
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


