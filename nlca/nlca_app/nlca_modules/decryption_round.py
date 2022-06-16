from nlca_app.nlca_modules.logicop import xnor,xor
from nlca_app.nlca_modules.f_fun import f_fun

def decr_round(key, p1_16, p17_32, p33_48, p49_64):
    er1_4= xnor(p49_64,key)
    er1_1= xnor(p1_16,key)
    temp=''
    temp1=f_fun(p49_64[:16])+f_fun(p49_64[16:])
    for i in range(8):
        temp+= temp1[i]
    er1_2=xor(p33_48, temp)    

    temp=''
    temp1=f_fun(p1_16[:16])+f_fun(p1_16[16:])
    for i in range(8):
        temp+= temp1[i]
    er1_3=xor(p17_32,temp)
    return er1_1,er1_2,er1_3,er1_4