def parse_text(txt, source, hashtag=""):
    if source=="SMS" and hashtag=="":
        return generate_list(text, smslength)
    else if source=="TWITTER":
        tweetlen = 140-len(hashtag+1)--one char for #
        tweetlist = generate_list(text, tweetlen)
        return tweetlist
    else:
        return "ERROR"
        
def generate_list(text, chunk_len):
    textlist=[]
    
    return textlist

