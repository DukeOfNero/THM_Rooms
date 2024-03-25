<code>
  
## Service Enumaration 

└─$ nmap  -p- -Pn 10.10.200.162 
Starting Nmap 7.92 ( https://nmap.org ) at 2024-03-25 05:24 CDT
Nmap scan report for 10.10.200.162
Host is up (0.037s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT   STATE SERVICE
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.36 seconds

### FTP - nothing 
└─$ nmap  -sV -sC -A  -p21 10.10.200.162
Starting Nmap 7.92 ( https://nmap.org ) at 2024-03-25 05:27 CDT
Nmap scan report for 10.10.200.162
Host is up (0.037s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.9.30.202
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.27 seconds

### WwWW

┌──(duke㉿kali)-[~/Documents/THM_all_in_one]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.200.162 -x .php, .txt, .html

Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

[+] Url:                     http://10.10.200.162
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s

2024/03/25 05:30:23 Starting gobuster in directory enumeration mode

/wordpress            (Status: 301) [Size: 318] [--> http://10.10.200.162/wordpress/]
/hackathons           (Status: 200) [Size: 197]                                      
/server-status        (Status: 403) [Size: 278]                                      

2024/03/25 06:13:56 Finished





<\code>
