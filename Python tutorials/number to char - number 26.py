def ty(num):
    word=""
    if num==20: word="Twenty"
    elif num==30: word="Thirty"
    elif num==40: word="Fourty"
    elif num==50: word="Fifty"
    elif num==60: word="Sixty"
    elif num==70: word="Seventy"
    elif num==80: word="Eighty"
    elif num==90: word="Ninety"
    return word

def ones(num):
    word=""
    if num==1: words="One"
    elif num==2: words="Two"
    elif num==3: words="Three"
    elif num==4: words="Four"
    elif num==5: words="Five"
    elif num==6: words="Six"
    elif num==7: words="Seven"
    elif num==8: words="Eight"
    elif num==9: words="Nine"
    elif num==10: words="Ten"
    elif num==11: words="Eleven"
    elif num==12: words="Twelve"
    elif num==13: words="Thrirteen"
    elif num==14: words="Fourteen"
    elif num==15: words="Fifteen"
    elif num==16: words="Sixteen"
    elif num==17: words="Seventeen"
    elif num==18: words="Eightteen"
    elif num==19: words="Nineteen"
    return words

result=""
num=int(input("Enter your number here:"))
if num>=1000:
    result+= ones(int(num/1000)) + " Thousand "
    num=num%1000
if num >=100:
    result+= ones(int(num/100)) + " Hundred "
    num=num%100
if num >=20:
    result+= ty(int(num/10)*10)
    num=num%10
if num>=1:
    result+=ones(num)

print(result)