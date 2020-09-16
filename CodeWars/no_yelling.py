def filter_words(st):
    str= st[0].upper()+st[1:].lower()
    return " ".join(str.split())
