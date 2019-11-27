
import shutil,os
dd=os.getcwd()
# shutil.copyfile("fortest","new_f") #将第一个文件的内容覆盖复制到第二个文件，不是追加
#shutil.copystat("fortest","new_f") #只是将第一个文件的属性复制给第二个文件，不复制内容
#shutil.copytree("a","c") #把第一个目录中的所有内容递归的复制到第二个目录中，目标目录必须为空
#shutil.rmtree("a") #递归删除该目录和目录中的所有内容
#shutil.make_archive("shutil_archive_test","zip","%s"%(dd)) #只能归档压缩一个目录，不能是文件

import zipfile

z = zipfile.ZipFile("my_zip.zip","w") #创建并打开一个压缩文件
z.write("test.py") #压缩一个文件
z.write("test_func.py") #再次压缩一个文件
z.close() #关闭压缩文件