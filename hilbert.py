import numpy as np
import copy
import math
def add_box(base_box, n):
    len_box = len(base_box)
    temp_box = copy.deepcopy(base_box)
    for i in range(len_box):
        for j in range(len_box):
            temp_box[i][j] = base_box[i][j] + n
    return temp_box


def fill_box(base_box, extr_box):
    box_len = int(len(base_box))
    box_number = box_len*box_len
    print('lenbox__', box_number)
    extr_box = np.array(extr_box)
    # 左两行
    #print(base_box)
    extr_box[0:box_len, 0:box_len] = add_box(base_box, box_number)
    extr_box[box_len:box_len*2, 0:box_len] = convert_cw(base_box)
    # 右两行
    extr_box[0:box_len, box_len:box_len*2] = add_box(base_box, box_number*2)
    extr_box[box_len:box_len*2, box_len:box_len*2] = add_box(convert_acw(base_box), box_number*3)

    return extr_box
# 顺时针 改变字符顺序
def convert_cw(base_box):
    box_len = len(base_box)
    temp_box = copy.deepcopy(base_box)
    for i in range(len(base_box)):
        for j in range(len(base_box)):
            temp_box[i][j] = box_len*box_len - base_box[box_len - 1 - j][i] + 1
    return temp_box


# 逆时针 改变字符顺序
def convert_acw(base_box):
    box_len = len(base_box)
    temp_box = copy.deepcopy(base_box)
    for i in range(len(base_box)):
        for j in range(len(base_box)):
            temp_box[i][j] = box_len*box_len - base_box[j][box_len-i-1] + 1
    return temp_box


n = input()
n = int(n)
base_box = [[2, 3],
            [1, 4]]
base_box = np.array(base_box)
print(base_box)
for i in range(1, n):
    dim_i = int(math.pow(2, i+1))
    print("dim_i", dim_i)
    extr_box = [[0 for j in range(dim_i)] for j in range(dim_i)]
    extr_box = fill_box(base_box, extr_box)
    base_box = extr_box
    print(extr_box)
