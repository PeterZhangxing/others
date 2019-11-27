import random
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper


def merge_once(data,low,mid,high):
    '''
    完成一次归并排序，本质就是把两个有序的列表合并成一个有序的列表
    :param data: 要完成合并的，从中间分开两头有序的数组
    :param low: 第一个元素的下标
    :param mid: 列表的中间位置
    :param high: 列表的最后一个元素的下标
    :return:
    '''
    i = low # 第一个列表的开始下标
    j = mid+1 # 第二个列表的开始下标
    tmp_li = [] # 用于存储合并完成的列表的临时列表

    # 当两个列表都有元素时，按顺序比较两个列表的元素，
    # 小的那个添加到临时列表中，直到其中一个列表没有元素
    while i <= mid and j <= high:
        if data[i] > data[j]:
            tmp_li.append(data[j])
            j += 1
        else:
            tmp_li.append(data[i])
            i += 1

    # 当第一个列表有元素剩余时，
    # 把剩余的元素全部放入临时列表
    while i <= mid:
        tmp_li.append(data[i])
        i += 1

    # 当第二个列表有元素剩余时，
    # 把剩余的元素全部放入临时列表
    while j <= high:
        tmp_li.append(data[j])
        j += 1

    # 将排好序的元素重新放回原理的列表中
    data[low:high+1] = tmp_li


def merge_sort(data,low,high):
    '''
    使用递归算法，完成把一个无序列表变成有序列表，
    本质就是通过递归把列表分成多个只有一个元素的小列表，
    对这些小列表完成一次归并，然后，依次完成对逐渐增大的两个有序列表的归并
    :param data:
    :param low:
    :param high:
    :return:
    '''
    if low < high: # 只要列表中还有两个以上的元素，就继续递归
        mid = (low+high) // 2 # 找到把一个列表拆分成两个的下标位置
        merge_sort(data,low,mid) # 左归并
        merge_sort(data,mid+1,high) # 右归并
        merge_once(data,low,mid,high)


@cal_time
def my_merge_sort(data):
    return merge_sort(data,0,len(data_li)-1)


if __name__ == '__main__':

    data_li = list(range(1,111120))
    random.shuffle(data_li)
    # print(data_li)

    my_merge_sort(data_li)
    print(data_li) # 0.5467894077301025 secs