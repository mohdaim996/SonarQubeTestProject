import json

#import Hex to Binary table for conversion
with open('data.json') as f:
  data = json.load(f)

class keyGen:
    def __init__(self, PK, PT):#Pk = Plain Key, PT = Plain Text
        #all of our constants
        self.pChoice = [57, 49, 41, 33, 25, 17, 9,
                        1, 58, 50, 42, 34, 26, 18,
                        10, 2, 59, 51, 43, 35, 27,
                        19, 11, 3, 60, 52, 44, 36,
                        63, 55, 47, 39, 31, 23, 15,
                        7, 62, 54, 46, 38, 30, 22,
                        14, 6, 61, 53, 45, 37, 29,
                        21, 13, 5, 28, 20, 12, 4]
        self.pChoice2 = [14, 17, 11, 24, 1, 5,
                         3, 28, 15, 6, 21, 10,
                         23, 19, 12, 4, 26, 8,
                         16, 7, 27, 20, 13, 2,
                         41, 52, 31, 37, 47, 55,
                         30, 40, 51, 45, 33, 48,
                         44, 49, 39, 56, 34, 53,
                         46, 42, 50, 36, 29, 32]
        self.initPermute = [58, 50, 42, 34, 26, 18, 10, 2,
                            60, 52, 44, 36, 28, 20, 12, 4,
                            62, 54, 46, 38, 30, 22, 14, 6,
                            64, 56, 48, 40, 32, 24, 16, 8,
                            57, 49, 41, 33, 25, 17, 9, 1,
                            59, 51, 43, 35, 27, 19, 11, 3,
                            61, 53, 45, 37, 29, 21, 13, 5,
                            63, 55, 47, 39, 31, 23, 15, 7]
        self.expansionTable = [32, 1, 2, 3, 4, 5,
                               4, 5, 6, 7, 8, 9,
                               8, 9, 10, 11, 12, 13,
                               12, 13, 14, 15, 16, 17,
                               16, 17, 18, 19, 20, 21,
                               20, 21, 22, 23, 24, 25,
                               24, 25, 26, 27, 28, 29,
                               28, 29, 30, 31, 32, 1]
        self.sBox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
                      ],

                     [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
                      ],

                     [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
                      ],

                     [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
                      ],

                     [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
                      ],

                     [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
                      ],

                     [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
                      ],

                     [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11], ]]
        self.sbPermutation = [16, 7, 20, 21, 29, 12, 28, 17,
                              1, 15, 23, 26, 5, 18, 31, 10,
                              2, 8, 24, 14, 32, 27, 3, 9,
                              19, 13, 30, 6, 22, 11, 4, 25]
        self.IP = [40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41, 9, 49, 17, 57, 25]

        self.shiftCount = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        #end of constants

        self.plainKey = [i for i in PK]#loop through the parameter to make a list
        #self.binaryKey = self.conBinary(self.plainKey)#convert the plain key(STRING) to binary, uncomment to use STRING key
        self.binaryKey = self.hextobin(self.plainKey)#conver the plain key(HEX) to binary,uncomment to use HEX key
        self.keyPermuted = self.permute(self.binaryKey, self.pChoice)#perform first permutation on key

        #create C and D
        self.C = [self.keyPermuted[:len(self.keyPermuted)//2]]
        self.D = [self.keyPermuted[len(self.keyPermuted)//2:]]
        #shifing
        self.C = self.shifter(self.C)
        self.D = self.shifter(self.D)
        #Join C and D to make K
        self.K = self.joinKey(self.C, self.D)
        
        #Perform permuted choice 2 on 16 keys
        self.K = self.secondPermute(self.K, self.pChoice2)

        #plain text section
        self.plainText = [j for j in PT]
        self.binaryText = self.conBinary(self.plainText)
        #self.binaryText = self.hextobin(self.plainText)
        self.textPermuted = self.permute(self.binaryText, self.initPermute)
        
        self.L = self.textPermuted[:len(self.textPermuted)//2]
        self.R = self.textPermuted[len(self.textPermuted)//2:]

        self.output = self.bintohex(self.sboxloop())

    def hextobin(self,hex):
        #convert hex input to binary
        i=0
        j=1
        z=[]
        temp = []
        while len(z)<=(len(hex)//2):
            #error handling for IndexErrors
            try:
                #append hex blocks of 2
                z.append(hex[i]+hex[j])
            except IndexError:
                break
            i += 2
            j += 2
        for x in z:   
            #convert based on data from data.json
            temp.extend(data['{}'.format(x)])
        return temp
    def bintohex(self,bin):
        #convert bin to hex
        i = 0
        j = 8
        z = []
        temp = ''
        while len(z)<=7:
            try:
                #strcture the list into blocks of 8
                z.append(bin[i:j])
            except IndexError:
                break
            i += 8
            j += 8
        for i in z:#iterate through 8 blocks
            x=''  
            for n in i:#iterate through each block
                x+=str(n)#convert to string for comparison
            for key, value in data.items():#iterate throught json data
                if x == value:#compare data item with current block if matched then retrieve Key
                    temp += key   
        return temp
    def sboxloop(self):
        #Expansion followed by it's XOR operation the substitution
        R=self.R#R0
        L=self.L#L0
        for k in self.K:#iterate 16 keys
            Re = self.permute(R, self.expansionTable)#expansion
            RXOR = self.XOR(Re, k)#XOR operation
            SBF = self.subBox(RXOR)#sustitution
            R1 = self.XOR(L, SBF[-1])#create R1 by (L(n) XOR f)
            L = R#assign R(0)to L
            R = R1 #assign R(1) to R(-1)
        return self.permute(R+L, self.IP)#join and return inverse permutation
    def subBox(self, RXOR):
        blockE = 6#point to block end
        temp = []
        round = 0
        
        while blockE-1 <= len(RXOR):
            blockS = blockE - 6#point to start of block 6 behind blockS
            #determine row vlaue then column
            row = str(RXOR[blockS])+str(RXOR[blockE-1]) #convert to string then concatnate to be converted to decimal
            column = ''.join([str(i) for i in RXOR[blockS+1:blockE-1]])#get item from X to Y of K1 XOR E(R) and convert each to value to string then join
            #converting to decimal
            column = self.toDecimal(column)
            row = self.toDecimal(row)

            sValue = self.sBox[round][row][column]#get values from sBox 
            
           
            temp.extend(self.secondBin(sValue))#convert to binary
            
            
            blockE += 6
            round += 1
        
        temp = self.permute(temp, self.sbPermutation)#perumtation
        
        return [temp]

    def toDecimal(self, binary):  # from geeksforgeeks.org/binary-decimal-vice-versa-python/
        return int(binary, 2)

    def joinKey(self, c, d):#joining of two lists
        temp = []
        for i in range(16):
            temp.append(c[i]+d[i])
        return temp

    def conBinary(self, string):#convert a string to binary
        temp = []
        for i in [bin(ord(c))[2:] for c in string]:
            while len(i) < 8:
                i = str(0)+i
            temp.extend(i)
        return temp

    def secondBin(self, n):  # from geeksforgeeks.org/binary-decimal-vice-versa-python/
        x = bin(n).replace("0b", "")
        while len(x) < 4:
            x = str(0)+x
        return x

    def permute(self, binary, permutedChoice):#perform a permutation
        return [binary[i-1] for i in permutedChoice]

    def secondPermute(self, key, permutedChoice):#perform a larger permutatrion for 16 list
        temp = []
      
        for k in key:
            
            temp1 = []
            
            for i in permutedChoice:
                temp1.extend(k[i-1])
            temp.append(temp1)
           
        return temp

    def shifter(self, vlaue): #shift value
        temp = vlaue[0]
        temp1=[]
        for i in self.shiftCount:
            temp = temp[i:]+temp[:i]
            temp1.append(temp)
        return temp1

    def XOR(self, List1, List2):#xor operation
        temp = []
        counter = 0
        for i in List1:
            temp.append(int(i) ^ int(List2[counter]))
            counter += 1
        return temp


Key = keyGen('133457799BBCDFF1', '0123456789ABCDEF')#plain Key, Plain Text

print('C = '+Key.output)