
def half_find(data_li,data):
    '''
    二分查找算法，实现在有序列表中查找某个数
    :param data_li:
    :param data:
    :return:
    '''
    start = 0
    end = len(data_li)-1
    while start <= end:
        mid = (start+end)//2
        if data_li[mid]['id'] == data:
            return mid,data_li[mid]['name'],data_li[mid]['age']
        elif data_li[mid]['id'] > data:
            end = mid-1
        else:
            start = start+1
    return


data_li = [
    {'id':100,'name':'daljdkl','age':34},
    {'id':101,'name':'daljdkl1','age':32},
    {'id':102,'name':'daljdkl2','age':54},
    {'id':103,'name':'daljdkl3','age':12},
    {'id':104,'name':'daljdkl4','age':65},
    {'id':105,'name':'daljdkl5','age':45},
    {'id':106,'name':'daljdkl6','age':90},
]


if __name__ == '__main__':

    res1 = half_find(data_li, 105)
    print(res1)