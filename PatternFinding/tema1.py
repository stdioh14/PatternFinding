alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def make_sets(pattern):
    sets = []
    for i in range(0, len(pattern) + 1):
        set_crt = {}
        crt = pattern[0:i]  
        for ch in alpha:
            next_state = 0
            aux = crt + ch
            if(aux == pattern[0:i+1]):
                next_state = i + 1
            else:
                for j in range(0, i + 1):
                    if pattern[0:j] == aux[i + 1 - j : i + 1]:
                        next_state = j
                        
            set_crt[ch] = next_state
        sets.append(set_crt)
    return sets

def find_pats(pattern, text):
    sets = make_sets(pattern)
    crt_state = 0
    n = len(pat)
    rez = []
    for i in range(0, len(text)):
        crt_set = sets[crt_state]
        crt_state = crt_set[text[i]]
        if crt_state == n:
            rez.append(i - n + 1)
    return rez
           

pat = input()
text = input()
indexes = find_pats(pat,text)

for i in range(0, len(indexes) - 1):
    print(indexes[i], end = " ")
print(indexes[len(indexes)-1])


        

