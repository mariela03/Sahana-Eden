def parse_text(txt, source, hashtag=""):
    if source=="SMS" and hashtag=="":
        return generate_list(text, smslength)
    else if source=="TWITTER":
        tweetlen = 140-len(hashtag+1)--one char for #
        tweetlist = generate_list(text, tweetlen)
        return tweetlist
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
