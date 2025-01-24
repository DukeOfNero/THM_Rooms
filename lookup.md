<code>


┌──(kali㉿kali)-[~]
└─$ nmap  -sV -A -Pn 10.10.217.222
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-23 11:23 CET
Nmap scan report for 10.10.217.222
Host is up (0.039s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 44:5f:26:67:4b:4a:91:9b:59:7a:95:59:c8:4c:2e:04 (RSA)
|   256 0a:4b:b9:b1:77:d2:48:79:fc:2f:8a:3d:64:3a:ad:94 (ECDSA)
|_  256 d3:3b:97:ea:54:bc:41:4d:03:39:f6:8f:ad:b6:a0:fb (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Did not follow redirect to http://lookup.thm
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.55 seconds


https://tryhackme.com/r/room/lookup

┌──(kali㉿kali)-[~/Documents/THM]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://lookup.thm -x php,txt,html 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://lookup.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt,html
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 275]
/.html                (Status: 403) [Size: 275]
/index.php            (Status: 200) [Size: 719]
/login.php            (Status: 200) [Size: 1]
/.html                (Status: 403) [Size: 275]
/.php                 (Status: 403) [Size: 275]
/server-status        (Status: 403) [Size: 275]
Progress: 882240 / 882244 (100.00%)
===============================================================
Finished
===============================================================


└─$ ffuf -c -w ../../www/wordlists/Subdomain.txt -u  "http://lookup.thm/" -H 'Host: FUZZ.lookup.thm' -fw 1

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://lookup.thm/
 :: Wordlist         : FUZZ: /home/kali/Documents/www/wordlists/Subdomain.txt
 :: Header           : Host: FUZZ.lookup.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response words: 1
________________________________________________

www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 40ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
WWW                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 340ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 43ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 281ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 36ms]
WWW                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 40ms]
WWW                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 38ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
WWW                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 39ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
WWW                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
:: Progress: [649649/649649] :: Job [1/1] :: 544 req/sec :: Duration: [0:11:43] :: Errors: 0 ::





<\code>
