<code>
  
https://tryhackme.com/r/room/dodge

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
netops-dev.dodge.thm - Firewall - Upload Logs
ball.dodge.thm 403



https://netops-dev.dodge.thm/firewall10110.php


┌──(duke㉿kali)-[~]
└─$ nmap  -Sv -p 21 dodge.thm                                                                         
Failed to resolve/decode supposed IPv4 source address "v": Temporary failure in name resolution
QUITTING!
                                                                                                                                                                                                                                            
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
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~]
└─$ ftp anonymous@dodge.thm                                                                                  
Connected to dodge.thm.
220 Welcome to Dodge FTP service
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||57843|)

ls


^C
receive aborted. Waiting for remote to finish abort.
ftp> ls
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



</code>
