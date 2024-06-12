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

                                                                                               
┌──(duke㉿kali)-[~]
└─$ gobuster vhost -w www/wordlists/Subdomain.txt -u http://futurevera.thm -k | egrep -e "Status: 200"  
Found: portal.futurevera.thm (Status: 200) [Size: 69]    
Found: payroll.futurevera.thm (Status: 200) [Size: 70]   
Found: portal.futurevera.thm (Status: 200) [Size: 69]    
Found: payroll.futurevera.thm (Status: 200) [Size: 70]                     
Found: portal.futurevera.thm (Status: 200) [Size: 69]                      
Found: Portal.futurevera.thm (Status: 200) [Size: 69]                      
Found: PORTAL.futurevera.thm (Status: 200) [Size: 69]          

### Web Enum                                                                                                    
                                                                                                    
┌──(duke㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u https://futurevera.thm -x php,txt,html -k

Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

[+] Url:                     https://futurevera.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,txt,html
[+] Timeout:                 10s

2024/06/12 01:52:08 Starting gobuster in directory enumeration mode

/index.html           (Status: 200) [Size: 4605]
/assets               (Status: 301) [Size: 319] [--> https://futurevera.thm/assets/]
/css                  (Status: 301) [Size: 316] [--> https://futurevera.thm/css/]   
/js                   (Status: 301) [Size: 315] [--> https://futurevera.thm/js/]    
/server-status        (Status: 403) [Size: 280]                                     
                                                                                    
2024/06/12 02:52:47 Finished

┌──(duke㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://payroll.futurevera.thm -x php,txt,html -k 
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

[+] Url:                     http://payroll.futurevera.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,txt,html
[+] Timeout:                 10s

2024/06/12 04:02:48 Starting gobuster in directory enumeration mode

/index.html           (Status: 200) [Size: 70]
/server-status        (Status: 403) [Size: 287]


## inspecting certificate for web support and blog and fount in CN=secrethelpdesk934752.support.futurevera.thm

  
</code>
