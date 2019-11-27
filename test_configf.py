#!/usr/bin/python3.5

import configparser

conf_f = configparser.ConfigParser() #创建配置文件对象
conf_f["Global"] = {"compression":"yes",
                    "listen":"8080",
                    "ip":"192.168.31.1"
                    }

conf_f["front"] = {"servername":"test1",
                   "serverip":"192.168.31.12",
                   "timeout":"60s"
                   }

conf_f["back"] = {"servername":"wordpress",
                   "serverip":"192.168.10.12",
                   "timeout":""
                   }

conf_f["back"]["timeout"] = "180s" #修改其中一项的值

with open("example.ini","w") as config_f: #将内容以配置文件格式写入到配置文档
    conf_f.write(config_f)
    config_f.close()