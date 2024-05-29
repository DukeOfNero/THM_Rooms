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
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://red.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,html,php
[+] Timeout:                 10s
===============================================================
2024/05/29 02:52:10 Starting gobuster in directory enumeration mode
===============================================================
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

</code>
