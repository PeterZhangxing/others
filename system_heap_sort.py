import time
import random
import heapq

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper

@cal_time
def my_heapq_sort(data):
    '''
    利用系统中自带的模块，完成列表的堆排序
    :param data:
    :return: 有序的列表
    '''
    h = [] # 创建一个空的堆
    # 向堆中插入数据
    for v in data:
        heapq.heappush(h,v)
    # 清空数组的元素，用来存储有序的数组
    data.clear()
    # 把经过堆排序的元素存储到原来的列表中
    for i in range(len(h)):
        data.append(heapq.heappop(h))
    return data

def mytopk(data,k):
    '''
    查找整个列表中，最大的k个元素的值，结果存储在列表中
    :param data:
    :param k:
    :return:
    '''
    return heapq.nlargest(k,data)

def mysmallk(data,k):
    '''
    查找整个列表中，最小的k个元素的值，结果存储在列表中
    :param data:
    :param k:
    :return:
    '''
    return heapq.nsmallest(k,data)


if __name__ == '__main__':

    data_li = list(range(1,111120))
    random.shuffle(data_li)
    # print(data_li)

    # my_heapq_sort(data_li)
    # print(data_li) # 0.10915946960449219 secs

    print(mytopk(data_li,3))

    print(mysmallk(data_li, 3))