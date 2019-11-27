import pymysql

class MyMeta(type):

    def __new__(cls,class_name,class_parents,class_attrs):
        mapping_dict = {}
        new_class_attrs = {}
        for k,v in class_attrs.items():
            if isinstance(v,tuple):
                mapping_dict[k] = v
            else:
                new_class_attrs[k] = v

        # new_class_attrs = {}
        # for k,v in class_attrs.items():
        #     if k not in mapping_dict:
        #         new_class_attrs[k] = v

        new_class_attrs['__table_name__'] = class_name
        new_class_attrs['__mapping__'] = mapping_dict

        return type.__new__(cls,class_name,class_parents,new_class_attrs)


class BaseTable(object,metaclass=MyMeta):

    def __init__(self,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            database='myjd',
            user='root',
            password='',
            charset='utf8')

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def save(self):

        col_name_li = []
        val_li = []
        table_name = self.__table_name__

        for k,v in self.__mapping__.items():
            col_name_li.append(v[0])
            val_li.append(getattr(self,k))

        new_val_li = []
        for item in val_li:
            if isinstance(item,int):
                new_val_li.append('%s'%item)
            elif isinstance(item,str):
                new_val_li.append("""'%s'"""%item)

        col_namestr = ','.join(col_name_li)
        valstr = ','.join(new_val_li)
        sql_tmp = "insert into %s (%s) values (%s)"
        sql = sql_tmp%(table_name,col_namestr,valstr)
        print(sql)

        res = self.run_insert_sql(sql)
        return res

    def run_insert_sql(self,sql):
        self.cur.execute(sql)
        self.conn.commit()


class User(BaseTable):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")


if __name__ == '__main__':
    myuser = User(uid=1,name='hj',email='123@qq.com',password='redhat')
    myuser.save()