
class MyStack(object):

    def __init__(self):
        self.data_contaner = []

    def push_stack(self,data):
        self.data_contaner.append(data)

    def pop_stack(self):
        try:
            res = self.data_contaner.pop(-1)
        except IndexError:
            res = None
        return res

    def top_ele(self):
        try:
            res = self.data_contaner[-1]
        except IndexError as e:
            res = None
        return res


class MyFiFoQ(object):

    def __init__(self):
        self.data_contaner = []

    def enqueue(self,data):
        self.data_contaner.append(data)

    def outqueue(self):
        try:
            res = self.data_contaner.pop(0)
        except IndexError:
            res = None
        return res


if __name__ == '__main__':
    # mystack = MyStack()
    #
    # for i in range(0,10,2):
    #     mystack.push_stack(i)
    #
    # print(mystack.data_contaner)
    #
    # mystack.pop_stack()
    # mystack.pop_stack()
    # mystack.pop_stack()
    # mystack.pop_stack()
    # ele = mystack.pop_stack()
    # print(ele)
    #
    # print(mystack.data_contaner)
    #
    # print(mystack.top_ele())
    # print(mystack.top_ele())

    myqueue = MyFiFoQ()
    for i in range(1,6):
        myqueue.enqueue(i)

    print(myqueue.data_contaner)

    print(myqueue.outqueue())
    print(myqueue.outqueue())
    print(myqueue.outqueue())
    print(myqueue.outqueue())
    print(myqueue.outqueue())
    print(myqueue.outqueue())
    print(myqueue.outqueue())