<code>
  
https://tryhackme.com/r/room/airplane  

### Service Enumeration
┌──(duke㉿kali)-[~/Documents/THM_AirPlane]
└─$ nmap  -sV -p- -Pn 10.10.128.237
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-13 03:08 CDT
Nmap scan report for 10.10.128.237
Host is up (0.039s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
6048/tcp open  x11?
8000/tcp open  http-alt Werkzeug/3.0.2 Python/3.8.10



http://airplane.thm:8000/?page=index.html

┌──(duke㉿kali)-[~/Documents/THM_AirPlane]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://airplane.thm:8000 -x php,txt,html -k
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://airplane.thm:8000
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,txt,html
[+] Timeout:                 10s
===============================================================
2024/06/13 03:20:15 Starting gobuster in directory enumeration mode
===============================================================
/airplane             (Status: 200) [Size: 655]




</code>
