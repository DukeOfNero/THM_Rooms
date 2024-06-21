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


