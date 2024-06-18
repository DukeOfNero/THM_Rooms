<code>

┌──(duke㉿kali)-[~/Documents/THM_Grep]
└─$ nmap  -sV -Pn -p-  10.10.133.182
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-18 04:20 CDT
Nmap scan report for 10.10.133.182
Host is up (0.036s latency).
Not shown: 65531 closed tcp ports (conn-refused)
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http     Apache httpd 2.4.41 ((Ubuntu))
443/tcp   open  ssl/http Apache httpd 2.4.41
51337/tcp open  http     Apache httpd 2.4.41
Service Info: Host: ip-10-10-133-182.eu-west-1.compute.internal; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 45.63 seconds



/public               (Status: 301) [Size: 307] [--> https://grep.thm/public/]
/api                  (Status: 301) [Size: 304] [--> https://grep.thm/api/]   
/javascript           (Status: 301) [Size: 311] [--> https://grep.thm/javascript/]
/phpmyadmin           (Status: 403) [Size: 274]                                   
/server-status        (Status: 403) [Size: 274] 


[+] Url:                     https://grep.thm/public
/index.php            (Status: 200) [Size: 0]
/html                 (Status: 301) [Size: 312] [--> https://grep.thm/public/html/]
/css                  (Status: 301) [Size: 311] [--> https://grep.thm/public/css/] 
/js                   (Status: 301) [Size: 310] [--> https://grep.thm/public/js/] 


[+] Url:                     https://grep.thm/api
/index.php            (Status: 200) [Size: 0]
/login.php            (Status: 200) [Size: 34]
/register.php         (Status: 200) [Size: 38]
/uploads              (Status: 301) [Size: 312] [--> https://grep.thm/api/uploads/]
/upload.php           (Status: 200) [Size: 39]                                     
/posts.php            (Status: 200) [Size: 25]                                     
/logout.php           (Status: 200) [Size: 42]                                     
/config.php           (Status: 200) [Size: 0]   

[+] Url:                     https://grep.thm/javascript
/jquery               (Status: 301) [Size: 318] [--> https://grep.thm/javascript/jquery/]

johncena
                                                               
  
</code>
