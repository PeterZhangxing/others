#!/usr/bin/python3.5

# l1 = ["1","2","3"]
# l2 = ["+","+"]
# test_str = l1[0]
# #print(len(l1))
# for i in range(1,len(l1)):
#     test_str += l2[i - 1]
#     test_str += l1[i]
#
# print(test_str)

def connet_list_str(l1,l2):
    test_str = l1[0]
    for i in range(1,len(l1)):
        test_str += l2[i-1]
        test_str += l1[i]
    return test_str

l1=["1","2","3","4","5"]
l2=["+","+","+","-"]
final_str = connet_list_str(l1,l2)
print(final_str)