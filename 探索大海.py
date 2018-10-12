
def euler_dis(x, y):
    # print((x[0] - y[0])*(x[0] - y[0]) + (x[1] - y[1])*(x[1] - y[1]))
    return (x[0] - y[0])*(x[0] - y[0]) + (x[1] - y[1])*(x[1] - y[1])


def check_exist(coord, classify_array):
    for coord_sub in classify_array:
        if coord == coord_sub[0]:
            return 1  # 相同
        return 0


n = input()
array = [[0] * int(n)] * int(n)
for i in range(int(n)):
    temp = input()
    array[i] = temp.strip().split(" ")

position_array = []
for i in range(int(n)):
    for j in range(int(n)):
        if int(array[i][j]) == 1:
            position_array.append((i, j))
min_dis = 2
#print(position_array)
classify_number = 1
classify_array = []
while len(position_array) != 0:
    # print(position_array)
    classify_array.append((position_array[0], classify_number))
    position_array.remove(position_array[0])
    flag_1 = 1  # 第一个flag 标记是否一个类别的数据分类完毕
    # 遍历一个类别
    while flag_1:
        flag_2 = 1  # 第二个flag 标记是否有新的数据加入分类数组
        #print("position", position_array)
        for coord in position_array:
            #print("coord1", coord)
            # 与子分类做对比，符合子分类则归类。
            for classify_array_sub in classify_array:
                if 0 < euler_dis(x=classify_array_sub[0], y=coord) < min_dis:
                    # print(coord)
                    if not check_exist(coord=coord, classify_array=classify_array):
                        # print(coord)
                        classify_array.append((coord, classify_number))
                        flag_2 = 0
                        #print("coord", coord)
                        #print("array", position_array)
                        position_array.remove(coord)
                        #print("array_remove", position_array)
                        #print("classify ", classify_array)
                        break
        if flag_2 == 1:
            break
    classify_number = classify_number + 1
len_array = len(classify_array)
sum_number = classify_array[len_array-1][1]
print(sum_number)
