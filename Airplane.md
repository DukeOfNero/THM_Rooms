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

</code>
