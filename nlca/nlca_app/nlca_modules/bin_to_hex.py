#this function takes binary input and returns corresponding hex value
def b2h(data, gap):
    itr= len(data)//4
    ret_val=''
    for i in range(itr):
        ret_val+=hex(int(data[4*i:4*i+4],2))[2:]
        if gap:
            if((i+1)%2==0 and i!=0):
                ret_val+=' '
        if ret_val=="00" or ret_val=="00 ":
         ret_val=''
    return ret_val.upper()

#print(b2h('10101011'))