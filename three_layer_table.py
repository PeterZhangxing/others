
class MyThreeLayerTable(object):

    def __init__(self,menu_dic):
        self.menu_dic = menu_dic
        self.li = [menu_dic]

    def recshow_table(self,menu):
        while True:
            for key in menu:print(key)
            k = input('input>>>').strip()
            if k == 'b' or k == 'q': return k
            elif k in menu.keys() and menu[k]:
                ret = self.recshow_table(menu[k])
                if ret == 'q':return 'q'

    def show_table(self):
        while self.li:
            for key in self.li[-1]:print(key)
            k = input('input>>>').strip()
            if k in self.li[-1].keys() and self.li[-1][k]:
                self.li.append(self.li[-1][k])
            elif k == 'b':self.li.pop()
            elif k == 'q':break


if __name__ == '__main__':

    menu = {'1':{'12':{'113':{}}},'2':{'22':{'223':{}}},'3':{'33':{'333':{}}}}

    threeobj = MyThreeLayerTable(menu)
    threeobj.recshow_table(menu)
    # threeobj.show_table()