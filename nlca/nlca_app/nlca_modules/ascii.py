def atoh(string):
    #string= hex(int(string,base=16))
    string= string.encode('utf-8')
    return string.hex().upper()

# print(atoh("hello"))
#print(ascii())

def btoa(bitstring):
    # binary_int = int(bin, 2)
    
    # # Getting the byte number
    # byte_number = binary_int.bit_length() + 7 // 8
    
    # # Getting an array of bytes
    # binary_array = binary_int.to_bytes(byte_number, "big")
    
    # # Converting the array into ASCII text
    # ascii_text = binary_array.decode()
    
    # # Getting the ASCII value
    # return ascii_text

    bitstring = -len(bitstring) % 8 * '0' + bitstring
    string_blocks = (bitstring[i:i+8] for i in range(0, len(bitstring), 8))
    string = ''.join(chr(int(char, 2)) for char in string_blocks)  
    return string

#print(btoa("11000010110001001110011011000010110001001110011"))