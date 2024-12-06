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


┌──(kali㉿kali)-[~]
└─$ ffuf -u http://10.10.80.225:1337/hmr_FUZZ -c -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.80.225:1337/hmr_FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

css                     [Status: 301, Size: 321, Words: 20, Lines: 10, Duration: 32ms]
js                      [Status: 301, Size: 320, Words: 20, Lines: 10, Duration: 31ms]
images                  [Status: 301, Size: 324, Words: 20, Lines: 10, Duration: 4833ms]
logs                    [Status: 301, Size: 322, Words: 20, Lines: 10, Duration: 32ms]



┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.80.225:1337 -x php,txt,html  
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.80.225:1337
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
/.php                 (Status: 403) [Size: 279]
/.html                (Status: 403) [Size: 279]
/index.php            (Status: 200) [Size: 1326]
/javascript           (Status: 301) [Size: 324] [--> http://10.10.80.225:1337/javascript/]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/vendor               (Status: 301) [Size: 320] [--> http://10.10.80.225:1337/vendor/]
/config.php           (Status: 200) [Size: 0]
/dashboard.php        (Status: 302) [Size: 0] [--> logout.php]
/phpmyadmin           (Status: 301) [Size: 324] [--> http://10.10.80.225:1337/phpmyadmin/]
/.php                 (Status: 403) [Size: 279]
/.html                (Status: 403) [Size: 279]
/reset_password.php   (Status: 200) [Size: 1664]
/server-status        (Status: 403) [Size: 279]



### http://10.10.80.225:1337/hmr_logs/error.logs

[Mon Aug 19 12:00:01.123456 2024] [core:error] [pid 12345:tid 139999999999999] [client 192.168.1.10:56832] AH00124: Request exceeded the limit of 10 internal redirects due to probable configuration error. Use 'LimitInternalRecursion' to increase the limit if necessary. Use 'LogLevel debug' to get a backtrace.
[Mon Aug 19 12:01:22.987654 2024] [authz_core:error] [pid 12346:tid 139999999999998] [client 192.168.1.15:45918] AH01630: client denied by server configuration: /var/www/html/
[Mon Aug 19 12:02:34.876543 2024] [authz_core:error] [pid 12347:tid 139999999999997] [client 192.168.1.12:37210] AH01631: user tester@hammer.thm: authentication failure for "/restricted-area": Password Mismatch
[Mon Aug 19 12:03:45.765432 2024] [authz_core:error] [pid 12348:tid 139999999999996] [client 192.168.1.20:37254] AH01627: client denied by server configuration: /etc/shadow
[Mon Aug 19 12:04:56.654321 2024] [core:error] [pid 12349:tid 139999999999995] [client 192.168.1.22:38100] AH00037: Symbolic link not allowed or link target not accessible: /var/www/html/protected
[Mon Aug 19 12:05:07.543210 2024] [authz_core:error] [pid 12350:tid 139999999999994] [client 192.168.1.25:46234] AH01627: client denied by server configuration: /home/hammerthm/test.php
[Mon Aug 19 12:06:18.432109 2024] [authz_core:error] [pid 12351:tid 139999999999993] [client 192.168.1.30:40232] AH01617: user tester@hammer.thm: authentication failure for "/admin-login": Invalid email address
[Mon Aug 19 12:07:29.321098 2024] [core:error] [pid 12352:tid 139999999999992] [client 192.168.1.35:42310] AH00124: Request exceeded the limit of 10 internal redirects due to probable configuration error. Use 'LimitInternalRecursion' to increase the limit if necessary. Use 'LogLevel debug' to get a backtrace.
[Mon Aug 19 12:09:51.109876 2024] [core:error] [pid 12354:tid 139999999999990] [client 192.168.1.50:45998] AH00037: Symbolic link not allowed or link target not accessible: /var/www/html/locked-down


  
<\code>
