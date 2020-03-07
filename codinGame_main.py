import sys
import math
import time

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# s = [bool(int(char)) for char in input()]
# t = [bool(int(char)) for char in input()]
s = [False, False, False, True, False, False, False, False]
t = [True, True, True, False, True, True, True, True]

s = [True, True, False, False, True, False, False, True, False, False, False]
t = [True, False, False, False, False, True, True, False, False, True, True]
N = len(s)

print(s, file=sys.stderr)
print(t, file=sys.stderr)

# print("----FIRST_ENDED\n", file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def getIndex(input1, input2, N):
    for x in range(N):
        if input1[x] != input2[x]:
            return x


def checkReq(bitNo, array, N):
    if bitNo == N - 1:
        return True
    if not array[bitNo + 1]:
        return False
    for x in range(2, N - bitNo):
        # print("Loopcheck", file=sys.stderr)
        # print(bitNo+x, file=sys.stderr)
        if (array[bitNo + x]):
            return False
    return True

def getIndexByPattern(bitNo, array, N):
    if bitNo == N - 1:  # lastElement
        return N - 1
    if not array[bitNo + 1]:
        return bitNo + 1
    for x in range(2, N - bitNo):
        if array[bitNo + x]:
            return bitNo + x


def changeBit(bitNo, array, N):
    changes = 0
    if (checkReq(bitNo, array, N)):
        array[bitNo] = not array[bitNo]
        changes += 1
    else:
        x = getIndexByPattern(bitNo, array, N)
        print("bitNo (bit to change): " + str(bitNo), file=sys.stderr)
        print("x (next bit which need to be changed): " + str(x), file=sys.stderr)
        array, changes = changeBit(x, array, N)
    return array, changes


def changesNeeded(bitNo):
    return pow(2, bitNo)


def getTrueIndexes(array, bitNo):
    trueIndexes = []
    for bulbNo in reversed(range(bitNo, len(array) - 1)):
        if (array[bulbNo]):
            trueIndexes.append(bulbNo)
    return trueIndexes


def getFirstTrueIndex(array, bitNo):
    for bulbNo in reversed(range(bitNo, len(array) - 1)):
        if (array[bulbNo]):
            return bulbNo


sumchanges = 0
firstPassage = True

# if(s[N-1]):
# s[N-1]=False
# sumchanges = 1

start_time = time.time()
end_time_1 = end_time_2 = end_time_3 = 0

while s != t:
    # print("beginning of the loop", file=sys.stderr)
    # print(s, file=sys.stderr)
    # print(t, file=sys.stderr)
    # print("\n", file=sys.stderr)
    changes = 0
    i = getIndex(s, t, N)
    if (firstPassage):
        # print("i: ", file=sys.stderr)
        # print(i, file=sys.stderr)
        # print("firstPassage", file=sys.stderr)
        # for iterator in range(N-i):
        # continue
        # bulbIndex = N-1-iterator
        # print("iterator: ", file=sys.stderr)
        # print(iterator, file=sys.stderr)
        # print("bulbIndex: ", file=sys.stderr)
        # print(bulbIndex, file=sys.stderr)
        # print("sumchanges before: ", file=sys.stderr)
        # print(sumchanges, file=sys.stderr)
        # print(s, file=sys.stderr)
        # if not s[bulbIndex] or checkReq(i,s,N):
        # print(s, file=sys.stderr)
        # print(s[bulbIndex], file=sys.stderr)
        # print("continue\n", file=sys.stderr)
        # continue
        # if(iterator == N-1-i):
        # sumchanges += int((changesNeeded(iterator)/2))
        # s[bulbIndex + 1] = True
        # print("\n", file=sys.stderr)
        # break
        # else:
        # if not (s[bulbIndex-1]) and checkReq(bulbIndex-1,s,N):
        # s[bulbIndex-1]=True
        # sumchanges += 1
        # print("FIRST CHANGE**********", file=sys.stderr)
        # print(s, file=sys.stderr)
        # sumchanges += changesNeeded(iterator+1)-1
        # print("else", file=sys.stderr)
        # s[bulbIndex] = False
        # s[N-1] = True
        # print("sumchanges after: ", file=sys.stderr)
        # print(sumchanges, file=sys.stderr)
        # print(s, file=sys.stderr)
        # print("\n", file=sys.stderr)
        # print("sumchanges: ", file=sys.stderr)
        # print(sumchanges, file=sys.stderr)
        # print("out of loop", file=sys.stderr)
        # print(s, file=sys.stderr)
        s, changes = changeBit(i, s, N)
        # sumchanges+=changes
        print("out of recursion;", file=sys.stderr)
        # print("after s,changes;", file=sys.stderr)
        # print(s, file=sys.stderr)
        # print("changes: ", file=sys.stderr)
        # print(changes, file=sys.stderr)
        # print("sumchanges: ", file=sys.stderr)
        # print(sumchanges, file=sys.stderr)
        end_time_1 = time.time()
        # print((end_time_1 - start_time)*1000, file=sys.stderr)
    else:
        changes = changesNeeded(N - i - 1)
        s[i] = not s[i]
        if (i < N - 1):
            s[i + 1] = True
    if (checkReq(i, s, N) and firstPassage):
        firstPassage = False
        print("after first passage1", file=sys.stderr)
        print(s, file=sys.stderr)
        s[i] = not s[i]
        changes += 1
        print("after first passage2", file=sys.stderr)
        print(s, file=sys.stderr)
        end_time_2 = time.time()
    end_time_3 = time.time()
    # print(s, file=sys.stderr)

    sumchanges += changes

print((end_time_1 - start_time) * 1000, file=sys.stderr)
print((end_time_2 - start_time) * 1000, file=sys.stderr)
print((end_time_3 - start_time) * 1000, file=sys.stderr)
print(sumchanges)

if sumchanges == 877:
    print("\n\nSUCCESS!!!!")
