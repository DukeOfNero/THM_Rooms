<code>

https://tryhackme.com/room/supersecrettip


```nmap  -sV -A -Pn 10.10.150.162   
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-06-27 12:40 CEST
Nmap scan report for 10.10.150.162
Host is up (0.038s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 3e:b8:18:ef:45:a8:df:59:bf:11:49:4b:1d:b6:b8:93 (RSA)
|   256 0b:cf:f9:94:06:85:97:f6:bd:cc:33:66:4e:26:ea:27 (ECDSA)
|_  256 60:ce:be:2d:1e:f0:18:00:30:70:ff:a2:66:d7:85:f7 (ED25519)
7777/tcp open  cbt?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
```




````
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.150.162:7777 -x .php, .txt, .html 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.150.162:7777
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/cloud                (Status: 200) [Size: 2991]
/debug                (Status: 200) [Size: 1957]
```

                                                                                                                               
┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.67.247:7777/cloud -x .php, .txt
nothing

## FFUZ
```
POST http://10.10.247.188:7777/cloud HTTP/1.1
host: 10.10.247.188:7777
user-agent: Mozilla/5.0 (Windows NT 10.0; rv:125.0) Gecko/20100101 Firefox/125.0
pragma: no-cache
cache-control: no-cache
content-type: application/x-www-form-urlencoded
referer: http://10.10.247.188:7777/cloud
content-length: 21

download=FFUZ
```

