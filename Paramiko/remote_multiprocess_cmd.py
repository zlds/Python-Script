# -*- coding: utf-8 -*-
import paramiko
import threading

# 认证路径
private = paramiko.RSAKey.from_private_key_file("/Users/xxx/.ssh/id_rsa")

# 连接函数
def cmd_run(ip,username,key,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip,username=username,port=22,pkey=key)

        for cmd in cmd:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.readlines()
            for result in result:
                print(result)
        ssh.close() # 关闭ssh连接
    except:
        print("%s\tERROR\n" %(ip))

if __name__ == '__main__':
    cmd = ["date"] # 命令
    username = 'xxx'  # 远程用户
    key = private  # 密钥
    ip_list = []  # IP 列表
    with open('ip.txt', 'r') as res:
        for ip in res.readlines():
            ip = ip.strip("\n")
            ip_list.append(ip)  # 将结果添加到列表中
    for ip in ip_list:
        t  = threading.Thread(target=cmd_run,args=(ip,username,key,cmd))
        t.start()
