'''
Created on Oct 8, 2014

@author: Jie
'''

'''Takes in a file with the 1st word in each line as a
abbreviation, the words after are full length words.
Creates a dictionary with the 1st word in each line 

def abbr(lstdict,lsttext):
    dict = {}
    for part in lstdict:
        for other in range(1,len(part)):
            dict[part[other]] = part[0]
    print dict
    for word in range(len(lsttext)):
        for x in dict.keys():
            if x == lsttext[word]:
                lsttext[word] = dict[x]
    finalstr = ""
    for part in lsttext:
        finalstr += part + " "
    print finalstr.strip()
    return finalstr.strip()

if __name__ == '__main__':
    lstdict = []
    with open("abbtest.txt", "r") as f:
        for line in f:
            lstdict.append(line.split())
    lsttext = []
    with open("textfile.txt", "r") as f:
        for line in f:
            lsttext.append(line.split())
    abbr(lstdict,lsttext[0])