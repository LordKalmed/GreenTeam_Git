def revword(word):
    newword=""
    for alpha in word:
        newword=alpha+newword
    return newword

def revwords(message):
    newmsg=""
    word= ""
    for x in message:
        if x == "":
            newmsg=revword(word)+" "
            word=" "
        else:
            word+=x
    newmsg=revword(word)
    print(newmsg)

message=input("Your chosen sentence?:")
revwords(message)

