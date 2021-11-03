def revword(num):
    ty=["","", "Twenty",'Thirty', 'Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    ones=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen', 'Seventeen','Eighteen','Nineteen']

    result=""
    
    if num>=1000:
        result+=ones[int(num/1000)]+" Thousand "
        num%=1000
    if num>=100:
        result+=ones[int(num/100)]+" Hundred "
        num%=100
    if num>=20:
        result+=ty[int(num/10)]+" "
        num%=10
    if num>=1:
        result+=ones[num]
    return result


