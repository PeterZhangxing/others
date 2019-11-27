import time
import sys
import random

sys.setrecursionlimit(100000)


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper


def quick_sort(data,left,right):
    '''
    递归的为列表中的所有元素找到其合适的位置，
    这个位置左边的数都比他小或者等于他，
    右边的数都比他大或者等于他，最终完成排序。
    :param data:
    :param left:
    :param right:
    :return:
    '''
    if left < right:
        mid = partition(data,left,right)
        quick_sort(data,left,mid-1)
        quick_sort(data,mid+1,right)


def partition(data,left,right):
    '''
    为列表中的某个元素找到一个位置，
    这个位置左边的数都比他小或者等于他，
    右边的数都比他大或者等于他
    :param data: 整个列表的数据
    :param left: 列表中开始查找的位置
    :param right: 列表中结束查找的位置
    :return: 最后这个数在列表中位置的下标
    '''
    tmp = data[left]
    while left < right:
        while left < right and data[right] <= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] >= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left


@cal_time
def my_quick_sort(data):
    '''
    在有递归的函数上使用装饰器，会造成每次递归都调用装饰器，
    所以需要重新定义一个函数封装有递归调用的函数，在其外层再加上装饰器，
    只有整个函数执行完成才会调用装饰器函数。
    :param data:
    :return:
    '''
    return quick_sort(data,0,len(data)-1)


if __name__ == '__main__':

    data_li = list(range(1,20))
    random.shuffle(data_li)
    print(data_li)

    my_quick_sort(data_li)
    print(data_li)