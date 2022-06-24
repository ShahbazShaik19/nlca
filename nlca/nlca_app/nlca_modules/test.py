from ascii import atoh
from bin_to_hex import b2h

def padd(pt):
    pt2=''
    pad_bits=bin((32-len(pt))//2)[2:]
    for i in range(4-len(pad_bits)):
        pad_bits='0'+pad_bits
    #print(b2h("0110", False))
    for i in range((32-len(pt))//2):
        pt2+= '0'+b2h(pad_bits, False)

    return pt2

pt="abcdefghprswqsaea"
pt=atoh(pt)
pt2=''
if len(pt)<32:
    pt2=padd(pt)
    print(pt+' '+pt2)

elif len(pt)>32:
    for i in range(len(pt)//32):
        print(pt[32*i:32*(i+1)])


    left_out=pt[len(pt)-len(pt)%32:]
    pt2= padd(left_out)

    print(left_out+' '+pt2)

else:
    print(pt)