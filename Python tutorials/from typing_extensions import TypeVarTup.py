uniquewords=[]

def isunique(word):
    for w in uniquewords:
        if w==word:
            return False
    uniquewords.append(word)
    return True

def removeduplicate(message):
    newmessage=""
    word=""
    for char in message:
        if char==" ":
            if isunique(word)==True:
                newmessage+=word+" "
            word=""
        else:
            word+=char
    if isunique(word)==True:
        newmessage+=word
    print(newmessage)

message=input("please enter message here:")
removeduplicate(message)