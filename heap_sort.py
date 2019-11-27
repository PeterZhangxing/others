import time
import random


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper


def sift_heap(data,low,high):
    '''
    该算法是把数组抽象为一个二叉树树，在其基础上构建堆
    :param data:
    :param low:
    :param high:
    :return:
    '''
    i = low # 根节点的序号
    j = 2*i+1 # 第一个左叶子节点的序号
    tmp = data[i] # 根节点的值
    while j <= high: # 只要没有到树的最后一个叶子节点
        # 如果树有右叶子节点，并且右叶子的值大于左叶子
        if j < high and data[j] < data[j+1]:
            j += 1 # j始终记录该根节点的，子节点中值大的那个的序列号
        if tmp < data[j]: # 如果根节点的值小于其最大的那个子节点的值
            data[i] = data[j] # 把叶子节点的值赋值给根节点
            i = j # 对以值大的这个叶子节点为根节点的子树执行上面的替换操作
            j = 2*i+1 # 取此子树左叶子节点的序号
        else:
            break
    data[i] = tmp # 把根节点的值放到最后空出来的叶子节点的位置


@cal_time
def heap_sort(data):
    n = len(data)
    # 从第一个有叶子节点的子树开始，为每一棵树执行筛选算法，
    # 对所有树执行完筛选操作后，建堆操作完成
    for i in range(n//2-1,-1,-1):
        sift_heap(data,i,n-1)

    # i是堆的最后一个元素的下标，
    # 0是每次筛选出的最大的元素的下标
    for i in range(n-1,-1,-1):
        data[0],data[i] = data[i],data[0]
        sift_heap(data,0,i-1)

@cal_time
def sys_sort(data):
    return data.sort()

if __name__ == '__main__':

    data_li = list(range(1,111120))
    random.shuffle(data_li)
    # print(data_li)

    # heap_sort(data_li)
    # print(data_li) # 0.8287804126739502 secs

    sys_sort(data_li)
    print(data_li) # 0.06183767318725586 secs