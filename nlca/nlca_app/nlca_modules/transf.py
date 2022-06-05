

def transf1(lst):
    strr=''
    for i in range(4):
        if (i+1)%2==0:
            j=3
            while j>=0:
                strr+=lst[i][j]
                j-=1
        else:
            j=0
            while j<4:
                strr+=lst[i][j]
                j+=1
    return strr


def transf2(lst):
    strr=''
    for i in range(4):
        if (i+1)%2==0:
            j=3
            while j>=0:
                strr+=lst[j][i]
                j-=1
        else:
            j=0
            while j<4:
                strr+=lst[j][i]
                j+=1
    return strr


def transf3(lst):
    strr=''
    for i in range(4):
        if (i+1)%2!=0:
            j=3
            while j>=0:
                strr+=lst[i][j]
                j-=1
        else:
            j=0
            while j<4:
                strr+=lst[i][j]
                j+=1
    return strr

def transf4(lst):
    strr=''
    for i in range(4):
        if (i+1)%2!=0:
            j=3
            while j>=0:
                strr+=lst[j][i]
                j-=1
        else:
            j=0
            while j<4:
                strr+=lst[j][i]
                j+=1
    return strr
