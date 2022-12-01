from random import randint
# import time 
# start = time.time()

if __name__ == '__main__':

    def DH():

        # Both the persons will be agreed upon the
        # public keys G and P
        # A prime number P is taken
        P = 23

        # A primitive root for P, G is taken
        G = 9

        # print('The Value of P is :%d'%(P))
        # print('The Value of G is :%d'%(G))

        # Alice will choose the private key a
        a = 4
        # print('The Private Key a for Alice is :%d'%(a))

        # gets the generated key
        x = int(pow(G, a, P))

        # Bob will choose the private key b
        b = 3
        # print('The Private Key b for Bob is :%d'%(b))

        # gets the generated key
        y = int(pow(G, b, P))

        # Secret key for Alice
        ka = int(pow(y, a, P))

        # Secret key for Bob
        kb = int(pow(x, b, P))

        # print('Secret key for the Alice is : %d'%(ka))
        # print('Secret Key for the Bob is : %d'%(kb))

        return ka

    def xnor_ing(plaintext:str, key:str, len):
        ans = ""
     
        # Loop to iterate over the
        # Binary Strings
        for i in range(len):
            
            # If the Character matches
            if (plaintext[i] == key[i]):
                ans += "1"
            else:
                ans += "0"
        # print(ans)
        # print(len(ans))
        return ans

    def left_shift1(bin_valued_str):

        # print(bin_valued_str)
        bin_valued_list = list(bin_valued_str.strip())
        # print(bin_valued_list)
        for i in range(len(bin_valued_list)-1):
            bin_valued_list[i] = bin_valued_list[i+1]
        bin_valued_list[len(bin_valued_list)-1] = '0'
        # print(bin_valued_list)
        rightShiftedBinaryString = ''.join(map(str,bin_valued_list))
        # print(rightShiftedBinaryString)
        return rightShiftedBinaryString

    def flip(c):
        return '1' if (c == '0') else '0'

    def onesCompliment(binString):
        # print(binString)
        binList = list(binString.strip())
        # print(binList)
        length = len(binList)
        ones = ""

        for i in range(length):
            ones += flip(binList[i])
        # print(ones)
        return ones

    def swap(bitString):
        x = len(bitString)
        set1 = bitString[slice(0, len(bitString)//2)]
        set2 = bitString[slice(len(bitString)//2, len(bitString))]
        swappedString = set2 + set1
        return swappedString

    key = DH()

    # print(bin_key)

    plaintext = "Networking"

    # ascii_num = list(map(ord,plaintext))
    # print(ascii_num)

    ascii_str = ' '.join(list(map(str, map(ord, plaintext))))
    ascii_str_list = ascii_str.split()
    ascii_int_list = list(map(int, ascii_str_list))
    ascii_bin_list = [bin(num)[2:] for num in ascii_int_list]

    for element in ascii_bin_list:
        if len(element) < 8:
            ascii_bin_list[ascii_bin_list.index(element)] = (8-len(element))*'0'+element

    bin_plaintext = ''.join(ascii_bin_list)

    bin_text_length = len(bin_plaintext)

    """
    mam jodi key algorithm theke change kore na ane tahole eta use kora jabe,
    otherwise ekhane key length hisab korar akta logical error ashte pare
    """
    bin_key = (bin_text_length-len(str(bin(key)[2:])))*'0' + str(bin(key)[2:])

    xnored_text = xnor_ing(bin_plaintext, bin_key, bin_text_length)
    oneBitShiftedBinaryString = left_shift1(xnored_text)
    # print(oneBitShiftedBinaryString)
    oneComplimentedString = onesCompliment(oneBitShiftedBinaryString)
    swappedString = swap(oneComplimentedString)
    # print(swappedString)
    # print(len(bin_key))
    # print(bin_text_length)
    # print(type(bin_plaintext))

# end = time.time()
# print("The time of execution of above program is :",(end-start) * 10**3, "ms")