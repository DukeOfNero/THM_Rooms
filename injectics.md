<code>
  
## injectics

https://tryhackme.com/r/room/injectics

### Enumeration

Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-16 06:01 EST
Nmap scan report for 10.10.136.219
Host is up (0.036s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 df:14:5e:7b:3c:5d:14:1e:a2:fb:8e:16:69:e8:1d:b7 (RSA)
|   256 d8:a2:ad:30:00:60:82:f1:a0:d9:8e:b8:50:93:65:7c (ECDSA)
|_  256 0f:50:9b:b7:2a:46:2c:d3:be:bb:dd:41:ee:d6:79:1b (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: Injectics Leaderboard
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.80 seconds


gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.136.219 -x php,txt,html                                            

[+] Url:                     http://10.10.136.219
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt,html
[+] Timeout:                 10s
/.html                (Status: 403) [Size: 278]
/index.php            (Status: 200) [Size: 6592]
/.php                 (Status: 403) [Size: 278]
/login.php            (Status: 200) [Size: 5401]
/flags                (Status: 301) [Size: 314] [--> http://10.10.136.219/flags/]
/css                  (Status: 301) [Size: 312] [--> http://10.10.136.219/css/]
/js                   (Status: 301) [Size: 311] [--> http://10.10.136.219/js/]
/javascript           (Status: 301) [Size: 319] [--> http://10.10.136.219/javascript/]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/vendor               (Status: 301) [Size: 315] [--> http://10.10.136.219/vendor/]
/dashboard.php        (Status: 302) [Size: 0] [--> dashboard.php]
/functions.php        (Status: 200) [Size: 0]
/phpmyadmin           (Status: 301) [Size: 319] [--> http://10.10.136.219/phpmyadmin/]
/.php                 (Status: 403) [Size: 278]
/.html                (Status: 403) [Size: 278]
/conn.php             (Status: 200) [Size: 0]
/server-status        (Status: 403) [Size: 278]



### in source code found notice about mail.log

http://10.10.136.219/mail.log

from: dev@injectics.thm
To: superadmin@injectics.thm
Subject: Update before holidays

Hey,

Before heading off on holidays, I wanted to update you on the latest changes to the website. I have implemented several enhancements and enabled a special service called Injectics. This service continuously monitors the database to ensure it remains in a stable state.

To add an extra layer of safety, I have configured the service to automatically insert default credentials into the `users` table if it is ever deleted or becomes corrupted. This ensures that we always have a way to access the system and perform necessary maintenance. I have scheduled the service to run every minute.

Here are the default credentials that will be added:

| Email                     | Password 	              |
|---------------------------|-------------------------|
| superadmin@injectics.thm  | superSecurePasswd101    |
| dev@injectics.thm         | devPasswd123            |

Please let me know if there are any further updates or changes needed.

Best regards,
Dev Team

dev@injectics.thm



  
<\code>
