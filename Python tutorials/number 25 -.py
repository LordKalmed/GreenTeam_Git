def find(message,word):
    found=0
    wo=len(word)
    i=0
    while i<len(message):
        if message[i]==word[0]:
            if message[i:i+wo]==word:
                found+=1
                i+=wo-1

        i+=1
    print(found)
message=input("User message:")
word=input("Word to find:")
find(message,word)