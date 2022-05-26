from keyword import kwlist

def keyWords():
    fileOpen = open("sevenDigits.py", encoding="utf-8")
    fileTxt = fileOpen.read()
    fileOpen.close()
    text = list(fileTxt)
    str2 = "!'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
    kw = kwlist
    number = 0
    dict1 = dict()

    for each in text: 
        if each in str2:
            text[number]=" "
        number+=1

    word = fileTxt.split(" ")

    for i in range(35):
        dict1[kw[i]] = dict1.get(kw[i], 0)

    for each in word:
        for i in range(35):
            if each == kw[i]:
                dict1[each] = dict1.get(each, 0)+1

    items = list(dict1.items())
    items.sort(key=lambda x:x[1], reverse=True)

    for i in range(35):
        print(items[i])

if __name__ == '__main__':
    keyWords()

