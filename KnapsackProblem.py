def take_four(elem):
    return elem[3]


def dynasty():
    number, fund = input().split(' ')
    fund = int(fund)
    number = int(number)
    max_prob = [[0 for col in range(fund+1)] for row in range(number+1)]
    raw_data = []
    for i in range(int(number)):  # 输入锁定金额和概率
        value, prob = input().split(' ')
        current_id = i+1
        raw_data.append([current_id, int(value), float(prob), float(prob)/float(value)])
    all_max = 0
    for i in range(1, number+1):  # 遍历所有的房价,number为房产个数
        for j in range(1, fund+1):  # 遍历所有总金额,
            # print(i, j, raw_data[i-1][1])
            if j < raw_data[i-1][1]:  # 假定的总金额小于当前房产的价格
                max_prob[i][j] = max_prob[i-1][j]  # 概率等于之前的
            else:
                max_prob[i][j] = max(max_prob[i-1][j], (max_prob[i-1][j-raw_data[i-1][1]] + raw_data[i-1][2]))
                if max_prob[i][j] > all_max:  # 记录概率最大值
                    all_max = max_prob[i][j]
    # 打印改率分布矩阵
    print('概率分布矩阵:\n', max_prob)
    # print(max_id)
    print('all_max_prob:', all_max)
    id_list = []
    # id_list.append(max_id)
    # 反向查找关键节点
    j = fund  # 定义列位置
    i = number  # 定义行位置
    while i != 0 and j != 0:  # 从max_prob表右下位置开始，逆序遍历
        # print('all_max:', all_max)
        print('当前遍历的节点i,j,prob:', i, j, max_prob[i][j])
        # print('value:', int(max_prob[i][j]))
        # print('value_(i,j-1):', int(max_prob[i][j-1]))
        # 如果同行上一列的的概率值仍然为最大，则切换到上一列
        if max_prob[i][j-1] == all_max:
            # print('j = j-1')
            j = j-1
        # 如果同列上一行的的概率值仍然为最大，则切换到上一行
        elif max_prob[i - 1][j] == all_max:
            # print('i = i-1')
            i = i-1
        # 处于拐点，可能是一个关键点。
        else:
            # print('test', int(max_prob[i][j]), int(all_max - raw_data[i-1][2]))
            # 如果当前概率等于最大的概率，则是关键点
            if max_prob[i][j] == all_max:
                id_list.append(raw_data[i-1][0])  # 保存当前楼盘的id
                all_max = all_max - raw_data[i-1][2]  # 转换当前最大概率，寻找下一个关键节点
                print('----当前楼盘是关键点之一：', i, '下一个节点prob为：', all_max)
            i = i-1
            j = j-1
    print(id_list)


def greedy():
    number, fund = input().split(' ')
    fund = int(fund)
    array = []
    max_prob = []
    max_value = 0
    for i in range(int(number)):  # 输入锁定金额和概率
        value, prob = input().split(' ')
        current_id = i+1
        array.append([current_id, int(value), float(prob), float(prob)/float(value)])
    print(array)
    # 第四位排序
    array.sort(key=take_four, reverse=True)
    print(array)
    for i in array:  # 选中最佳可能的资金
        max_value += i[1]
        if max_value < fund:
            max_prob.append([i[0], i[2]])
    print('max_prob:', max_prob)
    max_prob_value = 0
    for i in max_prob:
        max_prob_value = i[1] + max_prob_value
    print(max_prob_value, [x[0] for x in max_prob])


def test():
    for i in range(1, 11)[::-1]:
        print(i)


if __name__ == '__main__':
    dynasty()
    # greedy()