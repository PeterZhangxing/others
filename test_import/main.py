import importlib

# class_string = "core.test.MyImportTest"
#
# module_name ,class_name = class_string.rsplit(".",1)
#
# mymodule = importlib.import_module(module_name)
# myclass = getattr(mymodule,class_name)
#
# obj = myclass("zx")
# print(obj.show_name())


class_string = "testinnerimport.MyImportTest"

module_name ,class_name = class_string.rsplit(".",1)

mymodule = __import__(module_name) # 只能导入一层模块
myclass = getattr(mymodule,class_name)

obj = myclass("zx")
print(obj.show_name())