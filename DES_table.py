
PC1 = "57   49    41   33    25    17    9  1   58    50   42    34    26   18  10    2    59   51    43    35   27 19   11     3   60    52    44   36 63   55    47   39    31    23   15 7   62    54   46    38    30   22  14    6    61   53    45    37   29 21   13     5   28    20    12    4"
PC2 = "14    17   11    24     1    5   3    28   15     6    21   10   23    19   12     4    26    8  16     7   27    20    13    2  41    52   31    37    47   55  30    40   51    45    33   48  44    49   39    56    34   53  46    42   50    36    29   32"
shiftStr = "1 1 2 2 2 2 2 2 1 2 2 2 2 2 2 1"
IP = "58    50   42    34    26   18    10    2 60    52   44    36    28   20    12    4   62    54   46    38    30   22    14    6   64    56   48    40    32   24    16    8    57    49   41    33    25   17     9    1  59    51   43    35    27   19    11    3    61    53   45    37    29   21    13    5  63    55   47    39    31   23    15    7"
expand = "32     1    2     3     4    5   4     5    6     7     8    9   8     9   10    11    12   13   12    13   14    15    16   17  16    17   18    19    20   21  20    21   22    23    24   25  24    25   26    27    28   29  28    29   30    31    32    1"
S1 = "14  4  13  1   2 15  11  8   3 10   6 12   5  9   0  7  0 15   7  4  14  2  13  1  10  6  12 11   9  5   3  8   4  1  14  8  13  6   2 11  15 12   9  7   3 10   5  0   15 12   8  2   4  9   1  7   5 11   3 14  10  0   6 13"
S2 = "15  1   8 14   6 11   3  4   9  7   2 13  12  0   5 10    3 13   4  7  15  2   8 14  12  0   1 10   6  9  11  5   0 14   7 11  10  4  13  1   5  8  12  6   9  3   2 15   13  8  10  1   3 15   4  2  11  6   7 12   0  5  14  9"
S3 = "10  0   9 14   6  3  15  5   1 13  12  7  11  4   2  8 13  7   0  9   3  4   6 10   2  8   5 14  12 11  15  1  13  6   4  9   8 15   3  0  11  1   2 12   5 10  14  7    1 10  13  0   6  9   8  7   4 15  14  3  11  5   2 12"
S4 = "7 13  14  3   0  6   9 10   1  2   8  5  11 12   4 15  13  8  11  5   6 15   0  3   4  7   2 12   1 10  14  9  10  6   9  0  12 11   7 13  15  1   3 14   5  2   8  4   3 15   0  6  10  1  13  8   9  4   5 11  12  7   2 14"
S5 = "2 12   4  1   7 10  11  6   8  5   3 15  13  0  14  9   14 11   2 12   4  7  13  1   5  0  15 10   3  9   8  6    4  2   1 11  10 13   7  8  15  9  12  5   6  3   0 14   11  8  12  7   1 14   2 13   6 15   0  9  10  4   5  3"
S6 = "12  1  10 15   9  2   6  8   0 13   3  4  14  7   5 11  10 15   4  2   7 12   9  5   6  1  13 14   0 11   3  8   9 14  15  5   2  8  12  3   7  0   4 10   1 13  11  6   4  3   2 12   9  5  15 10  11 14   1  7   6  0   8 13"
S7 = "4 11   2 14  15  0   8 13   3 12   9  7   5 10   6  1  13  0  11  7   4  9   1 10  14  3   5 12   2 15   8  6   1  4  11 13  12  3   7 14  10 15   6  8   0  5   9  2   6 11  13  8   1  4  10  7   9  5   0 15  14  2   3 12"
S8 = "13  2   8  4   6 15  11  1  10  9   3 14   5  0  12  7    1 15  13  8  10  3   7  4  12  5   6 11   0 14   9  2    7 11   4  1   9 12  14  2   0  6  10 13  15  3   5  8    2  1  14  7   4 10   8 13  15 12   9  0   3  5   6 11"
P = "16   7  20  21 29  12  28  17          1  15  23  26          5  18  31  10      2   8  24  14   32  27   3   9     19  13  30   6     22  11   4  25"
FP = "40     8   48    16    56   24    64   32    39     7   47    15    55   23    63   31    38     6   46    14    54   22    62   30    37     5   45    13    53   21    61   29    36     4   44    12    52   20    60   28       35     3   43    11    51   19    59   27       34     2   42    10    50   18    58   26     33     1   41     9    49   17    57   25"

def dec2bistr(dec):
    b = bin(dec)[2:]
    while(len(b)<4):
        b = "0"+b
    return b

def myPrint(header, string):
    printList = []
    padding = int(len(string)/8)
    startPoint = 0
    while(startPoint < len(string)):
        printList.append(string[startPoint:startPoint+padding])
        startPoint += padding
    print(header + " ".join(printList))

def strXOR(str1, str2):
    result = ""
    for i, j in zip(str1, str2):
        if int(i) + int(j) == 1:
            result += "1"
        else:
            result += "0"
    return result

def shift(before, num):
    C = before[num:28] + before[0:num]
    D = before[28+num:56] + before[28:28+num]
    return C+D

def tableShift(before, table):
    after = ""
    for i in table:
        after += before[i-1]
    return after

def int2hex(string):
    integer = 0
    index = 0
    while(index < len(string)):
        integer += int(string[-index-1])*(pow(2, index))
        print(int(string[-index-1])*(2^index))
        index += 1
    print(integer)
    return hex(integer)[2:]

PC1Table = [int(x) for x in PC1.split()]
PC2Table = [int(x) for x in PC2.split()]
shiftTable = [int(x) for x in shiftStr.split()]
IPTable = [int(x) for x in IP.split()]
expandTable = [int(x) for x in expand.split()]
S1Table = [int(x) for x in S1.split()]
S2Table = [int(x) for x in S2.split()]
S3Table = [int(x) for x in S3.split()]
S4Table = [int(x) for x in S4.split()]
S5Table = [int(x) for x in S5.split()]
S6Table = [int(x) for x in S6.split()]
S7Table = [int(x) for x in S7.split()]
S8Table = [int(x) for x in S8.split()]
Sboxes = [S1Table, S2Table, S3Table, S4Table, S5Table, S6Table, S7Table, S8Table]
PTable = [int(x) for x in P.split()]
FPTable = [int(x) for x in FP.split()]
str2decDic_col = {}
str2decDic_row = {
    "00":0,
    "01":1,
    "10":2,
    "11":3
}

for i in list(range(16)):
    str2decDic_col[dec2bistr(i)] = i

def getSubkey(K, round):
    shiftNum = 0
    K_pc1 = tableShift(K, PC1Table)
    myPrint("PC-1: ", K_pc1)
    for i in list(range(round)):
        shiftNum += shiftTable[i]
    K_shift = shift(K_pc1, shiftNum)
    K_pc2 = tableShift(K_shift, PC2Table)
    myPrint("PC-2: ", K_pc2)
    return K_pc2

def DES(P, K, rounds=16):
    result = tableShift(P, IPTable)
    print("L0: " + result[0:32])
    print("R0: " + result[32:64])
    for i in list(range(rounds)):
        result = DES_base(result, K, i+1)
        # myPrint(result)
    myPrint("R1L1: ", result[32:64] + result[0:32])
    return tableShift(result[32:64] + result[0:32], FPTable)

def DES_base(P_IP, K, round):
    # myPrint(getSubkey(K, round))
    # myPrint(P_IP)
    return P_IP[32:64] + DES_f(P_IP[0:32], P_IP[32:64], getSubkey(K, round))

def DES_f(L, R, K):
    R_expanded = tableShift(R, expandTable)
    myPrint("E[R0]: ", R_expanded)
    # myPrint(R_expanded)
    # myPrint(K)
    SboxStr = strXOR(R_expanded, K)
    myPrint("A: ", SboxStr)
    Sboxed = ""
    for i in list(range(8)):
        Sboxed += S_calculate(SboxStr[i*6:i*6+6], i)
        print("S" + str(i+1) + "_box: " + S_calculate(SboxStr[i*6:i*6+6], i))
    # myPrint(Sboxed)
    myPrint("f: ", Sboxed)
    Sboxed_shift = tableShift(Sboxed, PTable)
    myPrint("g: ", Sboxed_shift)
    myPrint("h: ", strXOR(L, Sboxed_shift))
    return strXOR(L, Sboxed_shift)

def S_calculate(before, index):
    row = str2decDic_row[before[0] + before[5]]
    col = str2decDic_col[before[1:5]]
    return dec2bistr(Sboxes[index][row*16+col])

if __name__ == "__main__":
    P = "0000000100100011010001010110011110001001101010111100110111101111"
    # P = "0100100010111100011100010011100000001001010111011011010011011011"
    K = "0000000100100011010001010110011110001001101010111100110111101111"
    # K = "0001001100110100010101110111100110011011101111001101111111110001"
    myPrint("IP-1: ",DES(P, K, 1))