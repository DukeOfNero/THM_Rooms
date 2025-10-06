<code>

https://tryhackme.com/room/yougotmail
  
alias https://brownbrick.co/
not fill to etc/hosts

`root@ip-10-10-123-138:~# nmap -sV brownbrick.co
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
Service Info: Host: BRICK-MAIL; OS: Windows; CPE: cpe:/o:microsoft:windows'


**Username Enumeration**
from web page
oaurelius@brownbrick.co
wrohit@brownbrick.co
lhedvig@brownbrick.co
tchikondi@brownbrick.co
pcathrine@brownbrick.co
fstamatis@brownbrick.co


