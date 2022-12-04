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

    def cipherTextToBinary (cipherText):
        ascii_str = ' '.join(list(map(str, map(ord, cipherText))))
        ascii_str_list = ascii_str.split()
        ascii_int_list = list(map(int, ascii_str_list))
        ascii_bin_list = [bin(num)[2:] for num in ascii_int_list]

        for element in ascii_bin_list:
            if len(element) < 8:
                ascii_bin_list[ascii_bin_list.index(element)] = (8-len(element))*'0'+element

        bin_ciphertext = ''.join(ascii_bin_list)
        return bin_ciphertext

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

    def right_shift1(bin_valued_str):
        # print(bin_valued_str)
        bin_valued_list = list(bin_valued_str.strip())
        # print(bin_valued_list)
        i = len(bin_valued_list) - 2
        # print(i)
        while i >= 1:
            bin_valued_list[i+1] = bin_valued_list[i]
            i -= 1
        bin_valued_list[0] = '1'
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

    cipherText = "¬,ü.M"
    binCipherText = cipherTextToBinary(cipherText)
    # 1101000011000001
    # 0010111100111110
    # 0101111001111100
    # 0000000000001001 - key
    # 1010000110001010 - XNOR

    binCipherLength = len(binCipherText)

    key = DH() #9 - 0000000000001001
    bin_key = (binCipherLength-len(str(bin(key)[2:])))*'0' + str(bin(key)[2:])
    # print (bin_key)


    swappedCipherText = swap(binCipherText)
    # print(swappedCipherText)
    onesComplimented = onesCompliment(swappedCipherText)
    # print(onesComplimented)
    rightShiftedCipher = right_shift1(onesComplimented)
    # print(rightShiftedCipher)
    xnoredCipher = xnor_ing(rightShiftedCipher, bin_key, binCipherLength)
    # print(xnoredCipher)
    chunksOfCipher = splitIntoChunks(xnoredCipher)
    # print(chunksOfCipher)
    plainText = binCipherToPlaintext (chunksOfCipher)
    print(plainText)

    # print(chunksOfCipher)

    #0110100001101001
    #1101001011011000
