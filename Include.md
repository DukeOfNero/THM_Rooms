<code>
https://tryhackme.com/r/room/include

### Enumeration
  
nmap -sV -A 10.10.125.163
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-09 04:31 EST
Nmap scan report for 10.10.125.163
Host is up (0.033s latency).
Not shown: 992 closed tcp ports (conn-refused)
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 2f:59:39:c8:e1:95:ed:40:fb:4b:36:61:e7:54:02:81 (RSA)
|   256 b7:f8:13:db:cd:94:3c:31:cc:12:5b:46:8e:e6:34:fd (ECDSA)
|_  256 40:d4:4c:c4:8d:28:5a:03:b4:b7:78:04:33:df:25:7b (ED25519)
25/tcp    open  smtp     Postfix smtpd
|_ssl-date: TLS randomness does not represent time
|_smtp-commands: mail.filepath.lab, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
| ssl-cert: Subject: commonName=ip-10-10-31-82.eu-west-1.compute.internal
| Subject Alternative Name: DNS:ip-10-10-31-82.eu-west-1.compute.internal
| Not valid before: 2021-11-10T16:53:34
|_Not valid after:  2031-11-08T16:53:34
110/tcp   open  pop3     Dovecot pop3d
|_pop3-capabilities: CAPA SASL STLS UIDL AUTH-RESP-CODE RESP-CODES TOP PIPELINING
| ssl-cert: Subject: commonName=ip-10-10-31-82.eu-west-1.compute.internal
| Subject Alternative Name: DNS:ip-10-10-31-82.eu-west-1.compute.internal
| Not valid before: 2021-11-10T16:53:34
|_Not valid after:  2031-11-08T16:53:34
|_ssl-date: TLS randomness does not represent time
143/tcp   open  imap     Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=ip-10-10-31-82.eu-west-1.compute.internal
| Subject Alternative Name: DNS:ip-10-10-31-82.eu-west-1.compute.internal
| Not valid before: 2021-11-10T16:53:34
|_Not valid after:  2031-11-08T16:53:34
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: more Pre-login LITERAL+ LOGIN-REFERRALS have post-login listed capabilities SASL-IR ID STARTTLS ENABLE LOGINDISABLEDA0001 IDLE OK IMAP4rev1
993/tcp   open  ssl/imap Dovecot imapd (Ubuntu)
|_imap-capabilities: more Pre-login LITERAL+ LOGIN-REFERRALS have post-login listed capabilities OK ID AUTH=PLAIN ENABLE SASL-IR IDLE AUTH=LOGINA0001 IMAP4rev1
| ssl-cert: Subject: commonName=ip-10-10-31-82.eu-west-1.compute.internal
| Subject Alternative Name: DNS:ip-10-10-31-82.eu-west-1.compute.internal
| Not valid before: 2021-11-10T16:53:34
|_Not valid after:  2031-11-08T16:53:34
|_ssl-date: TLS randomness does not represent time
995/tcp   open  ssl/pop3 Dovecot pop3d
|_pop3-capabilities: CAPA SASL(PLAIN LOGIN) USER UIDL AUTH-RESP-CODE RESP-CODES TOP PIPELINING
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=ip-10-10-31-82.eu-west-1.compute.internal
| Subject Alternative Name: DNS:ip-10-10-31-82.eu-west-1.compute.internal
| Not valid before: 2021-11-10T16:53:34
|_Not valid after:  2031-11-08T16:53:34
4000/tcp  open  http     Node.js (Express middleware)
|_http-title: Sign In
50000/tcp open  http     Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: System Monitoring Portal
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: Host:  mail.filepath.lab; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.44 seconds

──(kali㉿kali)-[~/Documents/THM/THM_Include]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.125.163:4000 -x php,txt,html 

/index                (Status: 302) [Size: 29] [--> /signin]
/images               (Status: 301) [Size: 179] [--> /images/]
/signup               (Status: 500) [Size: 1246]
/Index                (Status: 302) [Size: 29] [--> /signin]
/signin               (Status: 200) [Size: 1295]
/fonts                (Status: 301) [Size: 177] [--> /fonts/]
/INDEX                (Status: 302) [Size: 29] [--> /signin]
/Signup               (Status: 500) [Size: 1246]
/SignUp               (Status: 500) [Size: 1246]
/signUp               (Status: 500) [Size: 1246]
/SignIn               (Status: 200) [Size: 1295]
Progress: 882240 / 882244 (100.00%)


┌──(kali㉿kali)-[~/Documents/THM/THM_Include]
└─$ nikto -h http://10.10.125.163:4000  -Tuning 4
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.125.163
+ Target Hostname:    10.10.125.163
+ Target Port:        4000
+ Start Time:         2025-01-09 05:57:03 (GMT-5)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ /: Retrieved x-powered-by header: Express.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OPTIONS: Allowed HTTP Methods: GET, HEAD .
+ 983 requests: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-01-09 05:57:48 (GMT-5) (45 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/THM/THM_Include]
└─$ nikto -h http://10.10.125.163:50000  -Tuning 4
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.125.163
+ Target Hostname:    10.10.125.163
+ Target Port:        50000
+ Start Time:         2025-01-09 06:14:36 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /: Cookie PHPSESSID created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.41 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ 983 requests: 0 error(s) and 5 item(s) reported on remote host
+ End Time:           2025-01-09 06:15:18 (GMT-5) (42 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested


┌──(kali㉿kali)-[~/Documents/THM/THM_Include]
└─$ sqlmap -r req2.txt --level 4 --risk 3 --dbs  --dump 1
        ___
       __H__                                                                                                        
 ___ ___[,]_____ ___ ___  {1.8.7#stable}                                                                            
|_ -| . [(]     | .'| . |                                                                                           
|___|_  [']_|_|_|__,|  _|                                                                                           
      |_|V...       |_|   https://sqlmap.org                                                                        

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 07:33:13 /2025-01-09/

[07:33:13] [INFO] parsing HTTP request from 'req2.txt'
[07:33:13] [INFO] testing connection to the target URL
got a 302 redirect to 'http://10.10.125.163:4000/friend/1'. Do you want to follow? [Y/n] n
[07:33:17] [INFO] checking if the target is protected by some kind of WAF/IPS
[07:33:18] [CRITICAL] heuristics detected that the target is protected by some kind of WAF/IPS
are you sure that you want to continue with further target testing? [Y/n] Y
[07:33:22] [WARNING] please consider usage of tamper scripts (option '--tamper')
[07:33:22] [INFO] testing if the target URL content is stable
[07:33:22] [WARNING] POST parameter 'activityType' does not appear to be dynamic
[07:33:22] [WARNING] heuristic (basic) test shows that POST parameter 'activityType' might not be injectable
[07:33:23] [INFO] testing for SQL injection on POST parameter 'activityType'
[07:33:23] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[07:33:24] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause'
[07:33:28] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT)'
[07:33:29] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[07:33:31] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[07:33:33] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (comment)'
[07:33:34] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (comment)'
[07:33:35] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - comment)'
[07:33:35] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[07:33:36] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[07:33:38] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)'
[07:33:39] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (Microsoft Access comment)'
[07:33:40] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (Microsoft Access comment)'
[07:33:42] [INFO] testing 'MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause'
[07:33:44] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[07:33:46] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[07:33:49] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[07:33:50] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[07:33:54] [INFO] testing 'PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)'
[07:33:55] [INFO] testing 'PostgreSQL OR boolean-based blind - WHERE or HAVING clause (CAST)'
[07:33:59] [INFO] testing 'Oracle AND boolean-based blind - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[07:34:01] [INFO] testing 'Oracle OR boolean-based blind - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[07:34:05] [INFO] testing 'SQLite AND boolean-based blind - WHERE, HAVING, GROUP BY or HAVING clause (JSON)'
[07:34:08] [INFO] testing 'SQLite OR boolean-based blind - WHERE, HAVING, GROUP BY or HAVING clause (JSON)'
[07:34:10] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[07:34:11] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET)'
[07:34:11] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT)'
[07:34:11] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int)'
[07:34:11] [INFO] testing 'PostgreSQL boolean-based blind - Parameter replace'
[07:34:11] [INFO] testing 'PostgreSQL boolean-based blind - Parameter replace (original value)'
[07:34:11] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Parameter replace'
[07:34:11] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Parameter replace (original value)'
[07:34:11] [INFO] testing 'Oracle boolean-based blind - Parameter replace'
[07:34:11] [INFO] testing 'Oracle boolean-based blind - Parameter replace (original value)'
[07:34:11] [INFO] testing 'Informix boolean-based blind - Parameter replace'
[07:34:11] [INFO] testing 'Informix boolean-based blind - Parameter replace (original value)'
[07:34:11] [INFO] testing 'Microsoft Access boolean-based blind - Parameter replace'
[07:34:11] [INFO] testing 'Microsoft Access boolean-based blind - Parameter replace (original value)'
[07:34:11] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL)'
[07:34:11] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL - original value)'
[07:34:11] [INFO] testing 'Boolean-based blind - Parameter replace (CASE)'
[07:34:11] [INFO] testing 'Boolean-based blind - Parameter replace (CASE - original value)'
[07:34:11] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[07:34:11] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[07:34:11] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[07:34:11] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[07:34:11] [INFO] testing 'PostgreSQL boolean-based blind - ORDER BY, GROUP BY clause'
[07:34:12] [INFO] testing 'PostgreSQL boolean-based blind - ORDER BY clause (original value)'
[07:34:12] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - ORDER BY clause'
[07:34:12] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - ORDER BY clause (original value)'
[07:34:12] [INFO] testing 'Oracle boolean-based blind - ORDER BY, GROUP BY clause'
[07:34:12] [INFO] testing 'Oracle boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[07:34:12] [INFO] testing 'Microsoft Access boolean-based blind - ORDER BY, GROUP BY clause'
[07:34:12] [INFO] testing 'SAP MaxDB boolean-based blind - ORDER BY, GROUP BY clause'
[07:34:12] [INFO] testing 'IBM DB2 boolean-based blind - ORDER BY clause'
[07:34:12] [INFO] testing 'HAVING boolean-based blind - WHERE, GROUP BY clause'
[07:34:14] [INFO] testing 'MySQL >= 5.0 boolean-based blind - Stacked queries'
[07:34:15] [INFO] testing 'PostgreSQL boolean-based blind - Stacked queries'
[07:34:16] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Stacked queries (IF)'
[07:34:16] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Stacked queries'
[07:34:17] [INFO] testing 'Oracle boolean-based blind - Stacked queries'
[07:34:18] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'                                                                                                                 
[07:34:20] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[07:34:22] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[07:34:24] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[07:34:26] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[07:34:28] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[07:34:30] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[07:34:32] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[07:34:34] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[07:34:36] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[07:34:38] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[07:34:40] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[07:34:42] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[07:34:45] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[07:34:47] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[07:34:47] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[07:34:49] [INFO] testing 'PostgreSQL OR error-based - WHERE or HAVING clause'
[07:34:51] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[07:34:54] [INFO] testing 'Microsoft SQL Server/Sybase OR error-based - WHERE or HAVING clause (IN)'
[07:34:55] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (CONVERT)'
[07:34:58] [INFO] testing 'Microsoft SQL Server/Sybase OR error-based - WHERE or HAVING clause (CONVERT)'
[07:35:00] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (CONCAT)'
[07:35:02] [INFO] testing 'Microsoft SQL Server/Sybase OR error-based - WHERE or HAVING clause (CONCAT)'
[07:35:04] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[07:35:06] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (XMLType)'
[07:35:08] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (UTL_INADDR.GET_HOST_ADDRESS)'
[07:35:10] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (UTL_INADDR.GET_HOST_ADDRESS)'
[07:35:12] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[07:35:14] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[07:35:16] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (DBMS_UTILITY.SQLID_TO_SQLHASH)'
[07:35:18] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (DBMS_UTILITY.SQLID_TO_SQLHASH)'
[07:35:21] [INFO] testing 'Firebird AND error-based - WHERE or HAVING clause'
[07:35:23] [INFO] testing 'Firebird OR error-based - WHERE or HAVING clause'
[07:35:25] [INFO] testing 'MonetDB AND error-based - WHERE or HAVING clause'
[07:35:26] [INFO] testing 'MonetDB OR error-based - WHERE or HAVING clause'
[07:35:28] [INFO] testing 'Vertica AND error-based - WHERE or HAVING clause'
[07:35:31] [INFO] testing 'Vertica OR error-based - WHERE or HAVING clause'
[07:35:34] [INFO] testing 'IBM DB2 AND error-based - WHERE or HAVING clause'
[07:35:36] [INFO] testing 'IBM DB2 OR error-based - WHERE or HAVING clause'
[07:35:38] [INFO] testing 'ClickHouse AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause'
[07:35:40] [INFO] testing 'ClickHouse OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause'
[07:35:42] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[07:35:44] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[07:35:44] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[07:35:44] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[07:35:44] [INFO] testing 'PostgreSQL error-based - Parameter replace'
[07:35:44] [INFO] testing 'Microsoft SQL Server/Sybase error-based - Parameter replace'
[07:35:44] [INFO] testing 'Microsoft SQL Server/Sybase error-based - Parameter replace (integer column)'
[07:35:44] [INFO] testing 'Oracle error-based - Parameter replace'
[07:35:45] [INFO] testing 'Firebird error-based - Parameter replace'
[07:35:45] [INFO] testing 'IBM DB2 error-based - Parameter replace'
[07:35:45] [INFO] testing 'MySQL >= 5.0 error-based - ORDER BY, GROUP BY clause (FLOOR)'
[07:35:45] [INFO] testing 'MySQL >= 5.1 error-based - ORDER BY, GROUP BY clause (EXTRACTVALUE)'
[07:35:45] [INFO] testing 'MySQL >= 4.1 error-based - ORDER BY, GROUP BY clause (FLOOR)'
[07:35:45] [INFO] testing 'PostgreSQL error-based - ORDER BY, GROUP BY clause'
[07:35:45] [INFO] testing 'Microsoft SQL Server/Sybase error-based - ORDER BY clause'
[07:35:45] [INFO] testing 'Oracle error-based - ORDER BY, GROUP BY clause'
[07:35:45] [INFO] testing 'Microsoft SQL Server/Sybase error-based - Stacking (EXEC)'
[07:35:47] [INFO] testing 'Generic inline queries'
[07:35:47] [INFO] testing 'MySQL inline queries'
[07:35:47] [INFO] testing 'PostgreSQL inline queries'
[07:35:47] [INFO] testing 'Microsoft SQL Server/Sybase inline queries'
[07:35:47] [INFO] testing 'Oracle inline queries'
[07:35:47] [INFO] testing 'SQLite inline queries'
[07:35:47] [INFO] testing 'Firebird inline queries'
[07:35:47] [INFO] testing 'ClickHouse inline queries'
[07:35:47] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[07:35:49] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[07:35:51] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[07:35:53] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[07:35:54] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[07:35:56] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[07:35:57] [INFO] testing 'PostgreSQL > 8.1 stacked queries'
[07:35:59] [INFO] testing 'PostgreSQL stacked queries (heavy query - comment)'
[07:36:01] [INFO] testing 'PostgreSQL < 8.2 stacked queries (Glibc - comment)'
[07:36:03] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[07:36:05] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (DECLARE - comment)'
[07:36:06] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries'
[07:36:09] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[07:36:10] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE)'
[07:36:12] [INFO] testing 'Oracle stacked queries (heavy query - comment)'
[07:36:14] [INFO] testing 'Oracle stacked queries (DBMS_LOCK.SLEEP - comment)'
[07:36:15] [INFO] testing 'IBM DB2 stacked queries (heavy query - comment)'
[07:36:17] [INFO] testing 'SQLite > 2.0 stacked queries (heavy query - comment)'
[07:36:18] [INFO] testing 'Firebird stacked queries (heavy query - comment)'
[07:36:20] [INFO] testing 'SAP MaxDB stacked queries (heavy query - comment)'
[07:36:21] [INFO] testing 'HSQLDB >= 1.7.2 stacked queries (heavy query - comment)'
[07:36:22] [INFO] testing 'HSQLDB >= 2.0 stacked queries (heavy query - comment)'
[07:36:24] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[07:36:26] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP)'
[07:36:29] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP)'
[07:36:31] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (SLEEP)'
[07:36:34] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP - comment)'
[07:36:35] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (SLEEP - comment)'
[07:36:37] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP - comment)'
[07:36:38] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP - comment)'
[07:36:40] [INFO] testing 'MySQL < 5.0.12 AND time-based blind (BENCHMARK)'
[07:36:44] [INFO] testing 'MySQL > 5.0.12 AND time-based blind (heavy query)'
[07:36:47] [INFO] testing 'MySQL < 5.0.12 OR time-based blind (BENCHMARK)'
[07:36:49] [INFO] testing 'MySQL > 5.0.12 OR time-based blind (heavy query)'
[07:36:52] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind'
[07:36:54] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (comment)'
[07:36:56] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (query SLEEP)'
[07:36:58] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (query SLEEP - comment)'
[07:37:00] [INFO] testing 'MySQL AND time-based blind (ELT)'
[07:37:02] [INFO] testing 'MySQL OR time-based blind (ELT)'
[07:37:05] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[07:37:08] [INFO] testing 'PostgreSQL > 8.1 OR time-based blind'
[07:37:10] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind (comment)'
[07:37:12] [INFO] testing 'PostgreSQL > 8.1 OR time-based blind (comment)'
[07:37:14] [INFO] testing 'PostgreSQL AND time-based blind (heavy query)'
[07:37:17] [INFO] testing 'PostgreSQL OR time-based blind (heavy query)'
[07:37:20] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[07:37:23] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF - comment)'
[07:37:25] [INFO] testing 'Microsoft SQL Server/Sybase AND time-based blind (heavy query)'
[07:37:28] [INFO] testing 'Microsoft SQL Server/Sybase OR time-based blind (heavy query)'
[07:37:30] [INFO] testing 'Oracle AND time-based blind'
[07:37:34] [INFO] testing 'Oracle OR time-based blind'
[07:37:36] [INFO] testing 'Oracle AND time-based blind (comment)'
[07:37:38] [INFO] testing 'Oracle OR time-based blind (comment)'
[07:37:40] [INFO] testing 'Oracle AND time-based blind (heavy query)'
[07:37:42] [INFO] testing 'Oracle OR time-based blind (heavy query)'
[07:37:45] [INFO] testing 'IBM DB2 AND time-based blind (heavy query)'
[07:37:47] [INFO] testing 'IBM DB2 OR time-based blind (heavy query)'
[07:37:50] [INFO] testing 'SQLite > 2.0 AND time-based blind (heavy query)'
[07:37:52] [INFO] testing 'SQLite > 2.0 OR time-based blind (heavy query)'
[07:37:55] [INFO] testing 'Firebird >= 2.0 AND time-based blind (heavy query)'
[07:37:58] [INFO] testing 'Firebird >= 2.0 OR time-based blind (heavy query)'
[07:38:01] [INFO] testing 'SAP MaxDB AND time-based blind (heavy query)'
[07:38:05] [INFO] testing 'SAP MaxDB OR time-based blind (heavy query)'
[07:38:08] [INFO] testing 'HSQLDB >= 1.7.2 AND time-based blind (heavy query)'
[07:38:11] [INFO] testing 'HSQLDB >= 1.7.2 OR time-based blind (heavy query)'
[07:38:14] [INFO] testing 'HSQLDB > 2.0 AND time-based blind (heavy query)'
[07:38:17] [INFO] testing 'HSQLDB > 2.0 OR time-based blind (heavy query)'
[07:38:21] [INFO] testing 'Informix AND time-based blind (heavy query)'
[07:38:24] [INFO] testing 'Informix OR time-based blind (heavy query)'
[07:38:27] [INFO] testing 'ClickHouse AND time-based blind (heavy query)'
[07:38:30] [INFO] POST parameter 'activityType' appears to be 'ClickHouse AND time-based blind (heavy query)' injectable 
it looks like the back-end DBMS is 'ClickHouse'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'ClickHouse' extending provided level (4) value? [Y/n] Y
[07:51:02] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[07:51:02] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[07:51:05] [INFO] testing 'Generic UNION query (random number) - 1 to 20 columns'
[07:51:06] [INFO] testing 'Generic UNION query (NULL) - 21 to 40 columns'
[07:51:08] [INFO] testing 'Generic UNION query (random number) - 21 to 40 columns'
[07:51:10] [INFO] testing 'Generic UNION query (NULL) - 41 to 60 columns'
[07:51:11] [INFO] testing 'Generic UNION query (random number) - 41 to 60 columns'
[07:51:13] [INFO] testing 'Generic UNION query (NULL) - 61 to 80 columns'
[07:51:15] [INFO] checking if the injection point on POST parameter 'activityType' is a false positive
[07:51:15] [WARNING] false positive or unexploitable injection point detected
[07:51:15] [WARNING] POST parameter 'activityType' does not seem to be injectable
[07:51:15] [WARNING] POST parameter 'activityName' does not appear to be dynamic
[07:51:15] [WARNING] heuristic (basic) test shows that POST parameter 'activityName' might not be injectable
[07:51:15] [INFO] testing for SQL injection on POST parameter 'activityName'
[07:51:15] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[07:51:18] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause'
[07:51:23] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT)'
[07:51:26] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[07:51:28] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[07:51:33] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (comment)'
[07:51:33] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (comment)'
[07:51:36] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - comment)'
[07:51:37] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[07:51:37] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL)'
[07:51:37] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL - original value)'
[07:51:37] [INFO] testing 'Boolean-based blind - Parameter replace (CASE)'
[07:51:37] [INFO] testing 'Boolean-based blind - Parameter replace (CASE - original value)'
[07:51:37] [INFO] testing 'HAVING boolean-based blind - WHERE, GROUP BY clause'
[07:51:39] [INFO] testing 'Generic inline queries'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] 





  
<\code>

