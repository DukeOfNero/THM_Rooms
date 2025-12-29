<code>
  
**TryHack3M: Burg3r Bytes**

https://tryhackme.com/room/burg3rbytes

**Enumeration**

``` root@ip-10-67-96-166:~# nmap -Pn -p- 10.67.167.186
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-29 12:10 GMT
Nmap scan report for 10.67.167.186
Host is up (0.00019s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

```root@ip-10-67-96-166:~# gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.67.167.186 -x php,txt,html
[+] Url:                     http://10.67.167.186
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,html,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/login                (Status: 200) [Size: 7724]
/register             (Status: 200) [Size: 7773]
/basket               (Status: 200) [Size: 6081]
/checkout             (Status: 200) [Size: 3095]
/console              (Status: 200) [Size: 1563]
Progress: 873100 / 873104 (100.00%)
======================================
```
</code>

