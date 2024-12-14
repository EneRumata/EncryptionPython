import random
INT_BITS = 32
ROUNDS=16

# разрядность блока данных для криптографии, менять нельзя т.к. определяет
# тип int функции фейстеля
DATA_BLOCK_WIDE = 32

# разрядность S-блока (4)
S_BLOCK_WIDE=4
MAGIC_ROTATE=11

# разрядность ключа шифрования (128)
KEY_SIZE=int(ROUNDS*DATA_BLOCK_WIDE/S_BLOCK_WIDE)

# количество S-блоков в раунде (16)
S_BLOCKS=int(2*DATA_BLOCK_WIDE/S_BLOCK_WIDE)

# -- блоки сети фейстеля
s = [[[x for x in range(int(2**S_BLOCK_WIDE))] for y in range(S_BLOCKS)] for z in range(ROUNDS)]
#s = [ROUNDS][S_BLOCKS][int(2**S_BLOCK_WIDE)] # 16,16,16

# print(s)

def generate(studentNum):
    random.seed(1)
    for r in range(0, len(s)):
        print("ROUND: {}".format(r))
        for i in range(0, len(s[r])):
            print(" {", end='')

            for j in range(0, len(s[r][i])):
                s[r][i][j] = random.randint(0, len(s[r][i]) - 1)
                print(" {},".format(s[r][i][j]), end='')
            print("},")

def str2int(s):
    rez=0
    for i in range (0,4):
        rez|=(ord(s[i])&255)<<(i*8)
    return rez

def int2str(l):
    rez=""
    for i in range (0,4):
        rez+=chr(l&255)
        l>>=8
    return rez


def leftRotate(n, d):
    return (n << d)|(n >> (INT_BITS - d))


def rightRotate(n, d):
    return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF


def s_block(block, key, round):
    y = 0
    res = block
    # print(key)
    # block = block ^ key
    for i in range(16):
        for j in range(16):
        #     t = (block << i * 4) & 0xFF000000
        #     r = t >> 28

            tk1 = (key << 0)
            rk1 = tk1 >> 4
            tk2 = (key << 4)
            rk2 = tk2 >> 4

        # print(str(s[round][rk1][rk2]))
        # res = s[round][rk1][rk2] ^ block
            res = s[round][i][j] * res + key
            # print(res)
            y |= res
            if j != 4:
             y <<= 4
        # temp1 = r << 1 & 0xF
        # temp2 = r << 2 & 0xF
        # temp3 = r << 3 & 0xF
        # temp4 = r << 4 & 0xF
        # one = temp1 >> 3
        # two = temp2 >> 3
        # three = temp3 >> 3
        # four = temp4 >> 3

    return res


def f(block, key, round):
    s = s_block(block, key, round)
    return s | leftRotate(s, MAGIC_ROTATE)


    # y = 0
    # print(round)
    # return leftRotate(key, MAGIC_ROTATE) | block
    # return leftRotate(s, MAGIC_ROTATE)
    # return s | leftRotate(key, MAGIC_ROTATE)
    # return block ^ leftRotate(key, MAGIC_ROTATE)
    # print("PRINTED S "+ str(s[round][]))
    # for i in round:
        # res = round[i] * block
        # pass
    # for i in round:
    #     res = block * i
    #     print(res)
    #
    #
    #
    # return y



def crypt(message, pass_key):
    left = str2int(message[:4])
    right = str2int(message[4:])
    for i in range(ROUNDS):

        key = (ord(pass_key[i]))
        # print("CHAR IN KEY: " + pass_key[i])
        temp = right ^ f(left, key, i)

        if i != ROUNDS-1:
            right = left
            left = temp

    msg = int2str(left) + int2str(right)
    return msg

# def crypt(message,pass_key):
#     left = str2int(message[:4])
#     right = str2int(message[4:])
#     for i in range(ROUNDS):
#         for j in range(ROUNDS):
#
#
#             round = s[i][j]
#             print("JIJA    "+ str(round))
#             print(pass_key[i])
#             key = ord(pass_key[i])
#             print(key)
#             temp = right ^ f(left, key, round)
#
#             if i != ROUNDS-1:
#                 right = left
#                 left = temp
#
#     msg = int2str(left) + int2str(right)
#     return msg


def decrypt(message,pass_key):
    left = str2int(message[:4])
    right = str2int(message[4:])
    for i in range(ROUNDS):
        key = (ord(pass_key[ROUNDS-1 - i]))
        temp = left ^ f(right, key, ROUNDS-1-i)

        if i != 0:
            left = right
            right = temp

    msg = int2str(left) + int2str(right)
    return msg


def main():
    generate(100)
    str="baracuda"
    pass_key="feistel cipher 1"
    print("==========\nисходные данные(2x32бит): \"{}\"".format(str))
    print("ключ шифрования(128 бит): \"{}\"".format(pass_key))
    rez=crypt(str,pass_key)
    print("зашифрованные данные: "+rez)
    rez=decrypt(rez,pass_key)
    print("расшифрованные данные: "+rez)

main()
# q = 3027188589
# print("{:032b}".format(q))
# y = 0
# for i in range(8):
#     t = (q << i*4) & 0xFF000000 # тут откидываем 4 * i бита от начала
#     # print("T")
#     # print("{:032b}".format(t))
#     r = t >> 28 # а тут оставляем каждую  i-тую пару из 4 битов в 32битовой последовательности
#     # print("R")
#     # print("{:032b}".format(r))
#     y |= r
#     if (i != 7):
#         y = y << 4
#     print(r)
# print(y)
# print("{:032b}".format(y))
# print(int2str(q))
