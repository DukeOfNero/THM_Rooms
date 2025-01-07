<code>
https://tryhackme.com/r/room/whatsyourname

### Enumeration
                                                                                                                 
┌──(kali㉿kali)-[~]
└─$ nmap -sV -A worldwap.thm     
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-07 04:46 EST
Nmap scan report for worldwap.thm (10.10.133.78)
Host is up (0.036s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 19:17:91:7b:c7:75:e2:35:74:31:c9:34:8d:5f:c0:84 (RSA)
|   256 e7:3c:be:15:d0:ab:cc:10:93:de:1d:e9:bf:46:24:52 (ECDSA)
|_  256 11:1a:26:ec:d1:eb:56:dd:d4:b7:11:41:87:5f:b6:26 (ED25519)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-title: Welcome
|_Requested resource was /public/html/
8081/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.78 seconds

┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://worldwap.thm -x php,txt,html 
/.php                 (Status: 403) [Size: 277]
/index.php            (Status: 302) [Size: 0] [--> /public/html/]
/.html                (Status: 403) [Size: 277]
/public               (Status: 301) [Size: 313] [--> http://worldwap.thm/public/]
/api                  (Status: 301) [Size: 310] [--> http://worldwap.thm/api/]
/javascript           (Status: 301) [Size: 317] [--> http://worldwap.thm/javascript/]
/logs.txt             (Status: 200) [Size: 0]
/phpmyadmin           (Status: 301) [Size: 317] [--> http://worldwap.thm/phpmyadmin/]
/.html                (Status: 403) [Size: 277]
/.php                 (Status: 403) [Size: 277]
/server-status        (Status: 403) [Size: 277]

┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://login.worldwap.thm -x php,txt,html 

/.php                 (Status: 403) [Size: 283]
/.html                (Status: 403) [Size: 283]
/index.php            (Status: 200) [Size: 70]
/login.php            (Status: 200) [Size: 3108]
/profile.php          (Status: 302) [Size: 0] [--> login.php]
/clear.php            (Status: 200) [Size: 4]
/assets               (Status: 301) [Size: 325] [--> http://login.worldwap.thm/assets/]
/chat.php             (Status: 302) [Size: 0] [--> login.php]
/db.php               (Status: 200) [Size: 0]
/javascript           (Status: 301) [Size: 329] [--> http://login.worldwap.thm/javascript/]
/logout.php           (Status: 302) [Size: 0] [--> login.php]
/setup.php            (Status: 200) [Size: 149]
/block.php            (Status: 200) [Size: 15]
/logs.txt             (Status: 200) [Size: 0]
/phpmyadmin           (Status: 301) [Size: 329] [--> http://login.worldwap.thm/phpmyadmin/]
/.html                (Status: 403) [Size: 283]
/.php                 (Status: 403) [Size: 283]
/change_password.php  (Status: 302) [Size: 4] [--> login.php]
/server-status        (Status: 403) [Size: 283]
Progress: 882240 / 882244 (100.00%)



  
<\code>
