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

<\code>
