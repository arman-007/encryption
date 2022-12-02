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

    def swap(bitString):
        x = len(bitString)
        set1 = bitString[slice(0, len(bitString)//2)]
        set2 = bitString[slice(len(bitString)//2, len(bitString))]
        swappedString = set2 + set1
        return swappedString

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

    def splitIntoChunks (cipher):
        n = 8 #length of chunk
        chunks = [cipher[i:i+n] for i in range(0, len(cipher), n)]
        return chunks

    def binaryToDecimal(n):
        return int(n,2)

    def binCipherToPlaintext (cipher):
        msg = ""
        for bin_num in cipher:
            asciiChar = binaryToDecimal(bin_num)
            msg += chr(asciiChar)
        return msg

    cipherText = "1100000111010000"
    cipherLength = len(cipherText)

    key = DH()
    bin_key = (cipherLength-len(str(bin(key)[2:])))*'0' + str(bin(key)[2:])


    swappedCipherText = swap(cipherText)
    onesComplimented = onesCompliment(swappedCipherText)
    leftShiftedCipher = left_shift1(onesComplimented)
    xnoredCipher = xnor_ing(leftShiftedCipher, bin_key, cipherLength)
    chunksOfCipher = splitIntoChunks(xnoredCipher)
    plainText = binCipherToPlaintext (chunksOfCipher)
    print(plainText)

    # print(chunksOfCipher)

    #0110100001101001
    #1101001011011000
