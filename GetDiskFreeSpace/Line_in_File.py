import paramiko 
port = 22
username = "allen"
file=open("ip.list")
for line in file: 
    hostname = str(line.split("\t")[1]) 
    password = str(line.split("\t")[4]).strip() 
    print "##########################",hostname,"########################"
    s = paramiko.SSHClient() 
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    s.connect(hostname, port, username, password) 
    stdin,stdout,sterr = s.exec_command("df -Th") 
    print stdout.read() 
    s.close() 
file.close()

ip.list内容：
dx 192.168.0.1 22 root loveyou

