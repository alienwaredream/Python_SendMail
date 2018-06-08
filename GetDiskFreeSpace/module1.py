#!/usr/bin/env python3

import paramiko
import pprint
import sendmail

def ssh2(ip,port,username,passwd,timeout=10,cmd='df -h --total',*key_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,22,username,passwd)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    #pprint.pprint(stdout.read().decode('utf-8').split('\n'))
    DiskFreeSpacs = stdout.read().decode('utf-8')
    return DiskFreeSpacs

if __name__ == '__main__':
    a = ( ssh2('207.246.116.203',22,'root','zhuyuzhe262526') )
    print(a)
    #sendmail.SendMail(a)

