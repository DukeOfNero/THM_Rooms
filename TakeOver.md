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

                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_TakeOver]
└─$ ffuf  -u https://futurevera.thm -H "Host: FUZZ.futurevera.thm" -w ../../www/wordlists/Subdomain.txt -fw 1511

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : https://futurevera.thm
 :: Wordlist         : FUZZ: ../../www/wordlists/Subdomain.txt
 :: Header           : Host: FUZZ.futurevera.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response words: 1511
________________________________________________

:: Progress: [649649/649649] :: Job [1/1] :: 153 req/sec :: Duration: [0:31:03] :: Errors: 0 ::

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

  
</code>
