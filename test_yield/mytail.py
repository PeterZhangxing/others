
# 使用生成器实现文件内容的实时追踪
def mytailfunc(filename):
    f =  open(filename,'r',encoding='utf-8')
    while True:
        line = f.readline().strip()
        if line:
            yield line

myiter = mytailfunc('test.txt')

for i in myiter:
    print(i)