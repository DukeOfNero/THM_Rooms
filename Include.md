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
===============================================================
Finished
===============================================================



  
<\code>

