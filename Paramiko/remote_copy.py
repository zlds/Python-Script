# -*- coding: utf-8 -*-
import paramiko


LOCAL_DRI = "/xxX/appdemon/target/appdemon.war"
REMOTE_DIR = "/data/app/appdemon/appdemon.war"

# 通过key认证
private_key = paramiko.RSAKey.from_private_key_file("/Users/xxx/.ssh/id_rsa")


# 定义连接对象
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接对象
ssh.connect(hostname="x.x.x.x", port=22, username="xx", pkey=private_key)

# 开启sftp
sftp = ssh.open_sftp()

# 上次文件
sftp.put(LOCAL_DRI,REMOTE_DIR)


# 关闭连接
ssh.close()