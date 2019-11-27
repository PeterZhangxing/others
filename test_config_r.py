#!/usr/bin/python3.5

import configparser

conf = configparser.ConfigParser()
conf.read("example.ini")
sec = conf.sections()
conf[sec[0]]["listen"] = "880"
print(conf[sec[0]]["listen"])
# conf.remove_section("back") #删除整个字段
conf.write(open("example.ini","w"))