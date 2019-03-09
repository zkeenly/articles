# 输入硬币种类数量和需要凑的金钱
number, money = input().split(' ')
# 金钱种类列表，存放所有类型的硬币
money_lists = []
# 输入所有硬币种类的面值
for i in range(int(number)):
    money_lists.append(int(input()))

res_list = [0 for i in range(int(money)+1)]  # 保存结果列表，每个数组都是该情况最小的种类数量
res_order = [[0 for j in range(0)] for i in range(int(money)+1)]  # 保存结果序列，其中每一个数组都保存了一个该情况的最小硬币序列
for i in range(1, int(money)+1):  # 遍历所需要凑的金额
    current_coin = -1
    min_res = -1
    for j in money_lists:  # 遍历硬币面值
        if i >= j:  # 确定不会超出界限，即当前需要的硬币总额不小于当前硬币面额
            if min_res == -1:
                min_res = res_list[i-j]+1
                current_coin = j
            elif res_list[i-j]+1 < min_res:
                min_res = res_list[i-j]+1
                current_coin = j
    res_list[i] = min_res  # 将最小的种类组合个数复制给当前res_lists
    for k in res_order[i-current_coin]:
        # print(res_order[i-current_coin])
        # print(i)
        if k != 0:
            res_order[i].append(k)
    if current_coin != 0:
        res_order[i].append(current_coin)

# print(res_list)
print(res_order)
