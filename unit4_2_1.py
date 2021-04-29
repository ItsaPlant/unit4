def is_palin(word):
    word_ = []
    invert = []
    for i in range(1, len(word) + 1):
        word_ += word[i - 1]
        invert += word[(i - (2 * i))]
    
    if word_ == invert:
        return True
    else:
        return False
    

check = is_palin("kajak")
print(check)

