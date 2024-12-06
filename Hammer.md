<code>

### Hammer
  
https://tryhackme.com/r/room/hammer

### Service Enumeration


┌──(kali㉿kali)-[~]
└─$ nmap -p- -Pn 10.10.80.225
PORT     STATE SERVICE
22/tcp   open  ssh
1337/tcp open  waste
                                                                             
┌──(kali㉿kali)-[~]
└─$ nmap -A -p1337  -Pn 10.10.80.225
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-06 08:03 EST
Nmap scan report for 10.10.80.225
Host is up (0.032s latency).

PORT     STATE SERVICE VERSION
1337/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Login
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.34 seconds



  
<\code>
