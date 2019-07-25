# @Time   : 2019/7/25 20:25
import numpy as np
import timeit

my_map = np.random.randint(2, size=(10, 10), dtype=np.int8)  # 随机生成0和1,0代表死1代表生
my_map[0, :] = my_map[-1:] = my_map[:, 0] = my_map[:, -1] = 0  # 边界定为死亡
# print(map)
neighbor = np.zeros(my_map.shape)
print('start map')
print(my_map)


def my_loop(my_map):
    neighbor = np.zeros(my_map.shape, dtype=int)  # 计数邻居的数量
    ''' 
     __ __ __
    |__|__|__|
    |__|__|__|
    |__|__|__|
    
    邻居的数量为以中间的节点为中心计算周围8个的数量之和
    
    '''
    neighbor[1:-1, 1:-1] = my_map[:-2, :-2] + my_map[:-2, 1:-1] + my_map[:-2, 2:] \
                           + my_map[1:-1, :-2] + my_map[1:-1, 2:] \
                           + my_map[2:, :-2] + my_map[2:, 1:-1] + my_map[2:, 2:]

    print('neighbor')
    print(neighbor)
    # 判定条件

    rule1 = np.argwhere((my_map == 1) & (neighbor < 2))  # 该死亡的坐标
    rule2 = np.argwhere((my_map == 1) & (neighbor > 3))  # 该死亡的坐标
    rule3 = np.argwhere((my_map == 0) & (neighbor == 3))  # 该生存的坐标，其余的不需要改变
    for i in rule1:
        my_map[i[0]][i[1]] = 0
    for j in rule2:
        my_map[j[0]][j[1]] = 0
    for k in rule3:
        my_map[k[0]][k[1]] = 1
    print('-' * 50, '\n', 'map')
    print(my_map)


print(timeit.timeit(lambda: my_loop(my_map), number=10))
