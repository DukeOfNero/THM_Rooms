<code>
https://tryhackme.com/r/room/takeover

### Enumaration

┌──(duke㉿kali)-[~/Documents/THM_TakeOver]
└─$ nmap -sV  -p- -Pn  futurevera.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-11 06:27 CDT
Nmap scan report for futurevera.thm (10.10.95.221)
Host is up (0.033s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http     Apache httpd 2.4.41 ((Ubuntu))
443/tcp open  ssl/http Apache httpd 2.4.41
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.83 seconds


  
<\code>
