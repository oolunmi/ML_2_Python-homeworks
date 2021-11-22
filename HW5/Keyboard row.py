row1="qwertyuiop"
row2="asdfghjkl"
row3="zxcvbnm"
words=["Hello","Alaska","Dad","Peace"]

def check(word, row):
    for i in word:
        if i not in row:
            return False
    return True

def final(words, rows=[row1, row2, row3]):
    res = []
    for w in words:
        for r in rows:
            if check(w.lower(), r) is True:
                res.append(w)
                continue
    return res

print(final(words))