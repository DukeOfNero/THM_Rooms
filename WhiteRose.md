<code>
https://tryhackme.com/r/room/whiterose

## Enumeration
┌──(kali㉿kali)-[~/Documents/THM/THM_whiterose]
└─$ nmap -A -Pn -p80 cyprusbank.thm 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-12 05:30 EST
Nmap scan report for cyprusbank.thm (10.10.211.123)
Host is up (0.035s latency).
rDNS record for 10.10.211.123: whiterose.thm

PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

┌──(kali㉿kali)-[~/Documents/THM/THM_whiterose]
└─$ ffuf -w ../../www/wordlists/Subdomain.txt -u http://cyprusbank.thm/ -H "Host:FUZZ.cyprusbank.thm" -fw 1 
found admin.cyprusbank.thm


### use crentials
Olivia Cortez:olivi8


http://admin.cyprusbank.thm/messages/?c=0

Gayle Bev: Of course! My password is 'p~]P@5!6;rs558:q'


  
<\code>

