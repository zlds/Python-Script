# -*- coding: utf-8 -*-
import paramiko


IP = "x.x.x.x"
USER = "xx"

# 定义本地key 通过key认证
private_key = paramiko.RSAKey.from_private_key_file("/Users/xxx/.ssh/id_rsa")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接
ssh.connect(hostname=IP,username=USER,port=22,pkey=private_key)


# 执行命令、并返回结果
stdin, stdout, stderr = ssh.exec_command("/usr/local/tomcat/tomcat.sh ")

# 查看返回结果
res, err = stdout.read(), stderr.read()

result = res if res else err

# 打印结果
print(result.decode())

ssh.close()
