import numpy as np
array_B = [[0 for i in range(19)] for i in range(19)]
array_W = [[0 for i in range(19)] for i in range(19)]
array_line = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
array_long = [[0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0]]
array_slant1 = [[1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1]]
array_slant2 = [[0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]]

def matrixMul(A, B):
    sum_value = 0
    # res = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
                sum_value += A[i][j] * B[i][j]
    return sum_value


draw = 1
count_B = 0
count_W = 0
for i in range(15):
    temp = input()
    for j in range(15):
        if temp[j] == 'B':
            array_B[i+2][j+2] = 1
            count_B = count_B + 1
        elif temp[j] == 'W':
            array_W[i+2][j+2] = 1
            count_W = count_W + 1
        elif temp[j] == '.':
            draw = 0
array_W = np.array(array_W)
array_B = np.array(array_B)
win_b = 0
win_w = 0

for i in range(15):
    for j in range(15):
        #print("test")
        if matrixMul(array_B[i:i+5, j:j+5], array_line) == 5:
            win_b = win_b + 1
        if matrixMul(array_B[i:i+5, j:j+5], array_long) == 5:
            win_b = win_b + 1
        if matrixMul(array_B[i:i+5, j:j+5], array_slant1) == 5:
            win_b = win_b + 1
        if matrixMul(array_B[i:i+5, j:j+5], array_slant2) == 5:
            win_b = win_b + 1

for i in range(15):
    for j in range(15):
        if matrixMul(array_W[i:i+5, j:j+5], array_line) == 5:
            win_w = win_w + 1
        if matrixMul(array_W[i:i+5, j:j+5], array_long) == 5:
            win_w = win_w + 1
        if matrixMul(array_W[i:i+5, j:j+5], array_slant1) == 5:
            win_w = win_w + 1
        if matrixMul(array_W[i:i+5, j:j+5], array_slant2) == 5:
            win_w = win_w + 1

if draw == 1:
    print('draw')
elif win_w == 0 and win_b == 0:
    print('not finished')
elif win_w == 1 and win_b == 0:
    print('white win')
if win_w == 0 and win_b == 1:
    print('black win')

elif win_b + win_w >= 2:
    print('invalid board')
elif count_W - count_B > 1 or count_B - count_W > 1:
    print('invalid board')


