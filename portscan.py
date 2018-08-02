#encoding:utf-8
import socket
import argparse
from IPy import IP
import re
import sys
import ftplib
import datetime
import linecache
open_port = 0
socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒
def read_txt(txt_boot):
    f = linecache.getlines(txt_boot)
    # print(f)
    return f

#创建ftp扫描
# def Login_Ftp(ip,username,password):#设置用户名密码登录
#     try:
#
#         Ftp = ftplib.FTP(ip,timeout=1)
#         # print('111')
#         Ftp.login(username,password)
#         # print('222')
#     except Exception as e:
#         print('[+]username:{1},password:{2},连接{0}失败'.format(ip,username,password))
#         print(e)
#     else:
#         print('[+]{} Login success!'.format(ip))
#         with open('ftpscan.txt','a+') as  f:
#             f.write(ip+'*'+username+'*'+password)
#             f.write('\n')
#         Ftp.quit()
# def ftp_main(ftplists):
#     a = datetime.datetime.now()
#     print(ftplists)
#     p = 'pass.dic'
#     u = 'user.dic'
#     passwords = read_txt(p)
#     usernames = read_txt(u)
#     for ip in ftplists:
#         print(ip)
#         for username in usernames:
#             username = username.strip('\n')
#             for password in passwords:
#                 password = password.strip('\n')
#                 Login_Ftp(str(ip),username,password)
#                 # time.sleep()
#     b = datetime.datetime.now()
#     run_time = (a - b).seconds
#     print('[+]扫描开始时间为：{0},扫描结束时间为：{1},总用时为{2}'.format(a, b, run_time))

#端口扫描
def portScanner(ip,port):
    global open_port
    socket.setdefaulttimeout(0.1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        a = s.connect_ex(((ip), int(port)))
        if a == 0:
            print('[-] {0} open port: {1}'.format(ip,port))
            open_port += 1
    except Exception as e:
        print(e)
    s.close()

def threading(iplists,portlists):
    for ip in iplists:
        for port in portlists:
            print('[-] this scan is scaning {0}:{1}'.format(ip, port))
            portScanner(str(ip),port)
    print('[-] Scan is complete!')
    print('[-] A total of {} open port ' .format(open_port))

#命令行创建
def main():
    iplists = []
    portlists = []
    ftplists = []
    p = argparse.ArgumentParser(description='port,scan!')
    p.add_argument('-i', '--ip', dest='ip', type=str, help='请输入ip！-i ip')
    p.add_argument('-p', '--port', dest='port', type=str, default='80,21,22,23,25,53,110,443,1433,1863,2289,3306,5631,5632,5000,8080,9090' ,help='请输入port -p port')
    p.add_argument('-f', '--ftp', dest='ftp', type =str,default='' ,help='请输入要扫描的ftp服务器的的ip')
    args = p.parse_args(sys.argv[1:])
    try:
        iplist = args.ip.split(',')
        portlist = args.port.split(',')
    except:
        pass
    try:
        ftplist = args.ftp.split(',')
    except:
        pass
    try:
        for i in iplist:
            print(i)
            # if re.match(r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})){3}$",i) is None:
            #     sys.exit('请输入准确的ip')
            if '/' in i:
                ip = IP(i)
                for t in ip:
                    iplists.append(t)
                # print(iplists)
            else:
                iplists.append(i)
    except:
        pass
    try:
        for ftpip in ftplist:
            if '/' in ftpip:
                ip = IP(ftpip)
                for t_ftp in ip:
                    ftplists.append(t_ftp)
                # print(iplists)
            else:
                ftplists.append(ftpip)
    except:
        pass
    try:
        for p in portlist:
            if '-' in p:
                a = int(p.split('-')[0])
                b = int(p.split('-')[1])
                for o in range(a,b+1):
                    portlists.append(o)
            else:
                portlists.append(p)
    except:
        pass
    try:
        if len(args.ip) > 0:
            threading(iplists,portlists)
    except:
        pass
    try:
        if len(args.ftp) > 0:
            # print(ftplists)
            # ftp_main(ftplists)
            print('222')
    except:
        pass
if __name__ == '__main__':
    a = datetime.datetime.now()
    main()
    b = datetime.datetime.now()
    c =(b-a).seconds
    print('All use time {} s'.format(c))





