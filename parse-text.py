smslength = 160
#this function has not been tested
def parse_text(txt, source, hashtag=""):
    if source=="SMS" and hashtag=="": # source is SMS
        return generate_list(text, smslength)
    else if source=="TWITTER":
        if hashtag[0] == '#': tweetlen = 140-(len(hashtag)+2)--one char for #, one for space
        else: tweetlen=140-(len(hashtag)+1)
        tweetlist = generate_list(text, tweetlen)
        hashedtweets=[]
        for element in tweetlist:
            if hashtag[0]=='#': hashedtweets.append(element+" "+hashtag)
            else hashedtweets.append(element+" #" + hashtag)
        return hashedtweets
    else:
        return "ERROR"

#unintelligent string parsing, split into chunks regardless of spaces
def generate_list(text, chunklength):
    slist = []
    num_chunks = int(math.ceil(len(text)/chunklength))
    for i in range(num_chunks):
        index = i * chunklength
        if index + chunklength >= len(text): slist.append( text[index:] )
        else: slist.append( text[index:index+chunklength])
    return slist
#a little smarter string parser, using spaces    
def generate_list2(text, chunklength):
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
