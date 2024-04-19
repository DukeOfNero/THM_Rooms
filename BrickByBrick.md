<code>
https://tryhackme.com/r/room/tryhack3mbricksheist

Note: Add 10.10.207.101 bricks.thm to your /etc/hosts file.

└─$ nmap  -sV -Pn  bricks.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-04-18 07:13 CDT
Nmap scan report for bricks.thm (10.10.207.101)
Host is up (0.041s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     WebSockify Python/3.8.10
443/tcp  open  ssl/http Apache httpd
3306/tcp open  mysql    MySQL (unauthorized)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
└─$ nmap  -sV -Pn  bricks.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-04-18 07:13 CDT
Nmap scan report for bricks.thm (10.10.207.101)
Host is up (0.041s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     WebSockify Python/3.8.10
443/tcp  open  ssl/http Apache httpd
3306/tcp open  mysql    MySQL (unauthorized)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.92%I=7%D=4/18%Time=66210E70%P=x86_64-pc-linux-gnu%r(GetR
SF:equest,291,"HTTP/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nServer:\x20
SF:rver\x20does\x20not\x20support\x20this\x20operation\.</p>\n\x20\x20\x20
SF:\x20</body>\n</html>\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

┌(duke kali) [/Documents/THM_BrickByBrick]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u https://bricks.thm -x .php, .txt, .html -k | egrep -v "Status: 301"

===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================

[+] Url:                     https://bricks.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s

===============================================================
2024/04/18 07:24:48 Starting gobuster in directory enumeration mode
===============================================================

/login                (Status: 302) [Size: 0] [--> https://bricks.thm/wp-login.php]
/login.php            (Status: 302) [Size: 0] [--> https://bricks.thm/wp-login.php]
/admin                (Status: 302) [Size: 0] [--> https://bricks.thm/wp-admin/]                 
/wp-login.php         (Status: 200) [Size: 4042]                                                 
/dashboard            (Status: 302) [Size: 0] [--> https://bricks.thm/wp-admin/]  



## Wordpress Enumeration
                                                                                                                                                  
┌──(duke㉿kali)-[~]
└─$ wpscan --url https://bricks.thm --enumerate u --disable-tls-checks 
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

[i] It seems like you have not updated the database for some time.
[?] Do you want to update now? [Y]es [N]o, default: [N]n
[+] URL: https://bricks.thm/ [10.10.119.30]
[+] Started: Fri Apr 19 05:54:19 2024

Interesting Finding(s):

[+] Headers
 | Interesting Entry: server: Apache
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: https://bricks.thm/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: https://bricks.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: https://bricks.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: https://bricks.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

Fingerprinting the version - Time: 00:00:28 <==========================================================================================================================================================> (708 / 708) 100.00% Time: 00:00:28
[i] The WordPress version could not be detected.

[+] WordPress theme in use: bricks
 | Location: https://bricks.thm/wp-content/themes/bricks/
 | Readme: https://bricks.thm/wp-content/themes/bricks/readme.txt
 | Style URL: https://bricks.thm/wp-content/themes/bricks/style.css
 | Style Name: Bricks
 | Style URI: https://bricksbuilder.io/
 | Description: Visual website builder for WordPress....
 | Author: Bricks
 | Author URI: https://bricksbuilder.io/
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Urls In 404 Page (Passive Detection)
 |
 | Version: 1.9.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - https://bricks.thm/wp-content/themes/bricks/style.css, Match: 'Version: 1.9.5'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:00 <=============================================================================================================================================================> (10 / 10) 100.00% Time: 00:00:00

[i] User(s) Identified:

[+] administrator
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By:
 |  Wp Json Api (Aggressive Detection)
 |   - https://bricks.thm/wp-json/wp/v2/users/?per_page=100&page=1
 |  Rss Generator (Aggressive Detection)
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Fri Apr 19 05:54:53 2024
[+] Requests Done: 1332
[+] Cached Requests: 11
[+] Data Sent: 354.176 KB
[+] Data Received: 28.813 MB
[+] Memory used: 227.711 MB
[+] Elapsed time: 00:00:34

### found brick theme 1.9.5 -- vulneable by CVE-2024-25600

use exploit from 
https://github.com/K3ysTr0K3R/CVE-2024-25600-EXPLOIT/blob/main/CVE-2024-25600.py



https://bricks.thm/phpmyadmin/
https://bricks.thm/sample/





<\code>
