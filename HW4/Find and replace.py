def find_and_replace(words,pattern):
    matches=[]
    for string in words:
        if len(string)==len(pattern):
            dict={}
            pattern_chars=[]
            dict_possible=True
            for index, char in enumerate(string):
                if char not in dict:
                    if pattern[index] in pattern_chars:
                        dict_possible=False
                        break
                    else:
                        dict[char]=pattern[index]
                        pattern_chars.append(pattern[index])
            if dict_possible is True:
                new_string = ''.join(dict[c] for c in string)
                if new_string == pattern:
                    matches.append(string)
    return matches

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"

print(find_and_replace(words,pattern))
