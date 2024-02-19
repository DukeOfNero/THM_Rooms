link: https://tryhackme.com/room/neighbour
## Enumeration nmap, gobuster, nikto

<code>
  
┌──(duke㉿kali)-[~/Documents/TMH_Neighbour]
└─$ nmap  -sV -Pn -p22,80 10.10.205.86
Starting Nmap 7.92 ( https://nmap.org ) at 2024-02-19 02:36 CST
Nmap scan report for 10.10.205.86
Host is up (0.033s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.53 ((Debian))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.75 seconds

┌──(duke㉿kali)-[~/Documents/TMH_Neighbour]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.205.86 -x .txt,.php,html
[+] Url:                     http://10.10.205.86
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php,html
[+] Timeout:                 10s
2024/02/19 02:37:17 Starting gobuster in directory enumeration mode

/index.php            (Status: 200) [Size: 1357]
/login.php            (Status: 200) [Size: 1316]
/profile.php          (Status: 302) [Size: 0] [--> login.php]
/assets               (Status: 301) [Size: 313] [--> http://10.10.205.86/assets/]
/db                   (Status: 301) [Size: 309] [--> http://10.10.205.86/db/]    
/db.php               (Status: 200) [Size: 0]                                    
/logout.php           (Status: 302) [Size: 0] [--> login.php]                    
/server-status        (Status: 403) [Size: 277]               

┌──(duke㉿kali)-[~/Documents/TMH_Neighbour]
└─$ nikto  -h http://10.10.205.86                  
- Nikto v2.1.6
+ Target IP:          10.10.205.86
+ Target Hostname:    10.10.205.86
+ Target Port:        80
+ Start Time:         2024-02-19 03:34:49 (GMT-6)
+ Server: Apache/2.4.53 (Debian)
+ Retrieved x-powered-by header: PHP/8.0.19
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Cookie PHPSESSID created without the httponly flag
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ OSVDB-3093: /db.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ /login.php: Admin login page/section found.
+ 7889 requests: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2024-02-19 03:40:07 (GMT-6) (318 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested


</code>
