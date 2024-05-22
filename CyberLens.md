https://tryhackme.com/r/room/cyberlensp6
<code>
### Enumeration Services

┌──(duke㉿kali)-[~/Documents/THM_CyberLens]
└─$ nmap  -sV -p-   cyberlens.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-05-22 04:57 CDT
Nmap scan report for cyberlens.thm (10.10.136.194)
Host is up (0.032s latency).
Not shown: 65519 closed tcp ports (conn-refused)
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Apache httpd 2.4.57 ((Win64))
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49677/tcp open  msrpc         Microsoft Windows RPC
61777/tcp open  http          Jetty 8.y.z-SNAPSHOT
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 219.74 seconds


Apache24\conf\extra\httpd-ssl.conf:228:#     file needs this password: `xxj31ZMTZzkVA'.

C:\Users\CyberLens\Documents\Management>more CyberLens-Management.txt
more CyberLens-Management.txt
Remember, manual enumeration is often key in an engagement ;)


RDP ::


CyberLens
HackSmarter123



C:\Users\CyberLens\Documents\Management>


  [+] Checking AlwaysInstallElevated
   [?]  https://book.hacktricks.xyz/windows/windows-local-privilege-escalation#alwaysinstallelevated
    AlwaysInstallElevated set to 1 in HKLM!
    AlwaysInstallElevated set to 1 in HKCU!

<\code>
