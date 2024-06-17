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

www.dodge.thm
blog.dodge.thm
touch-me-not.dodge.thm
dev.dodge.thm
netops-dev.dodge.thm
ball.dodge.thm

</code>
