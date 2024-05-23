<code>

https://tryhackme.com/r/room/hijack

### Service Enumeration

──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ nmap -A  -p- 10.10.28.220
Starting Nmap 7.92 ( https://nmap.org ) at 2024-05-23 04:24 CDT
Nmap scan report for 10.10.28.220
Host is up (0.046s latency).
Not shown: 65526 closed tcp ports (conn-refused)
PORT      STATE SERVICE  VERSION
21/tcp    open  ftp      vsftpd 3.0.3
22/tcp    open  ssh      OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 94:ee:e5:23:de:79:6a:8d:63:f0:48:b8:62:d9:d7:ab (RSA)
|   256 42:e9:55:1b:d3:f2:04:b6:43:b2:56:a3:23:46:72:c7 (ECDSA)
|_  256 27:46:f6:54:44:98:43:2a:f0:59:ba:e3:b6:73:d3:90 (ED25519)
80/tcp    open  http     Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Home
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.18 (Ubuntu)
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs
|   100003  2,3,4       2049/udp6  nfs
|   100005  1,2,3      41347/tcp6  mountd
|   100005  1,2,3      45038/udp   mountd
|   100005  1,2,3      51547/udp6  mountd
|   100005  1,2,3      58786/tcp   mountd
|   100021  1,3,4      36081/tcp6  nlockmgr
|   100021  1,3,4      42932/tcp   nlockmgr
|   100021  1,3,4      48773/udp   nlockmgr
|   100021  1,3,4      57240/udp6  nlockmgr
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl
2049/tcp  open  nfs_acl  2-3 (RPC #100227)
42877/tcp open  mountd   1-3 (RPC #100005)
42932/tcp open  nlockmgr 1-4 (RPC #100021)
43051/tcp open  mountd   1-3 (RPC #100005)
58786/tcp open  mountd   1-3 (RPC #100005)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 40.72 seconds


### FTP nothing                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ ftp anonymous@10.10.28.220
Connected to 10.10.28.220.
220 (vsFTPd 3.0.3)
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed
ftp> dir
530 Please login with USER and PASS.
530 Please login with USER and PASS.
ftp: Can't bind for data connection: Address already in use
ftp> ls
530 Please login with USER and PASS.
ftp> exit
221 Goodbye.

### NFS nothing                                                                                                                                                                                                                                     
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ showmount 10.10.28.220
Hosts on 10.10.28.220:
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ showmount 10.10.28.220 -e
Export list for 10.10.28.220:
/mnt/share *
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ mkdir nfs       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ sudo mount -t nfs 10.10.28.220:/mnt/share ./nfs 
[sudo] password for duke: 
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Hijack]
└─$ cd nfs        
cd: permission denied: nfs
                                                                                                                                                                                                                                          
drwx------   2 1003 1003 4096 Aug  8  2023 nfs
                                                                                                                                                                                                                                           

<\code>
