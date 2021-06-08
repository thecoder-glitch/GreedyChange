import resource, sys

# up recur limit
sys.setrecursionlimit(10**6)
data_open = open('/Users/taraghazanfari/Desktop/Week4_BENG181/dataset.txt', 'r')
data_read = data_open.read().splitlines()
v = data_read[0]
w = data_read[1]



def LCSBackTrack(v, w):
    s = [i[:] for i in [[0] * (len(w) + 1)] * (len(v) + 1)]
    backtrack = [i[:] for i in [[0] * (len(w) + 1)] * (len(v) + 1)]
    for i in range(0, len(v) + 1):
        s[i][0] = 0
    for j in range(0, len(w) + 1):
        s[0][j] = 0
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            match = 0
            if v[i - 1] == w[j - 1]:
                match = 1
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i-1][j-1] + match)
            if s[i][j] == s[i-1][j]:
                #down
                backtrack[i][j] = "d"
            elif s[i][j] == s[i][j-1]:
                #right
                backtrack[i][j] = "r"
            else:
                #diagnol
                backtrack[i][j] = "dg"
    return backtrack


def outputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == "d":
        return outputLCS(backtrack, v, i-1, j)
    elif backtrack[i][j] == "r":
        return outputLCS(backtrack, v, i, j-1)
    else:
        return outputLCS(backtrack, v, i-1, j-1) + v[i - 1]



back = LCSBackTrack(v, w)
print(outputLCS(back, v, len(v), len(w)))


