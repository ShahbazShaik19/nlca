#this function takes binary input and returns corresponding hex value
def b2h(data):
    itr= len(data)//4
    ret_val=''
    for i in range(itr):
        ret_val+=hex(int(data[4*i:4*i+4],2))[2:]
        if((i+1)%2==0 and i!=0):
            ret_val+=' '
    return ret_val.upper()

#print(b2h('10101011'))