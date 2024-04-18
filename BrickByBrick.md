https://tryhackme.com/r/room/tryhack3mbricksheist

Note: Add 10.10.207.101 bricks.thm to your /etc/hosts file.

└─$ nmap  -sV -Pn  bricks.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-04-18 07:13 CDT
Nmap scan report for bricks.thm (10.10.207.101)
Host is up (0.041s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     WebSockify Python/3.8.10
443/tcp  open  ssl/http Apache httpd
3306/tcp open  mysql    MySQL (unauthorized)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
└─$ nmap  -sV -Pn  bricks.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-04-18 07:13 CDT
Nmap scan report for bricks.thm (10.10.207.101)
Host is up (0.041s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     WebSockify Python/3.8.10
443/tcp  open  ssl/http Apache httpd
3306/tcp open  mysql    MySQL (unauthorized)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.92%I=7%D=4/18%Time=66210E70%P=x86_64-pc-linux-gnu%r(GetR
SF:equest,291,"HTTP/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nServer:\x20
SF:WebSockify\x20Python/3\.8\.10\r\nDate:\x20Thu,\x2018\x20Apr\x202024\x20
SF:12:13:36\x20GMT\r\nConnection:\x20close\r\nContent-Type:\x20text/html;c
SF:harset=utf-8\r\nContent-Length:\x20472\r\n\r\n<!DOCTYPE\x20HTML\x20PUBL
SF:IC\x20\"-//W3C//DTD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\"http://www\.w3\.org/TR/html4/strict\.dtd\">\n<html>\n\x20\x20\x2
SF:0\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20http-equiv=\"Cont
SF:ent-Type\"\x20content=\"text/html;charset=utf-8\">\n\x20\x20\x20\x20\x2
SF:0\x20\x20\x20<title>Error\x20response</title>\n\x20\x20\x20\x20</head>\
SF:n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>Error\x20r
SF:esponse</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code:\x20405<
SF:/p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Message:\x20Method\x20Not\x20Al
SF:lowed\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code\x20explan
SF:ation:\x20405\x20-\x20Specified\x20method\x20is\x20invalid\x20for\x20th
SF:is\x20resource\.</p>\n\x20\x20\x20\x20</body>\n</html>\n")%r(HTTPOption
SF:s,2B9,"HTTP/1\.1\x20501\x20Unsupported\x20method\x20\('OPTIONS'\)\r\nSe
SF:rver:\x20WebSockify\x20Python/3\.8\.10\r\nDate:\x20Thu,\x2018\x20Apr\x2
SF:02024\x2012:13:36\x20GMT\r\nConnection:\x20close\r\nContent-Type:\x20te
SF:xt/html;charset=utf-8\r\nContent-Length:\x20500\r\n\r\n<!DOCTYPE\x20HTM
SF:L\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x20\x
SF:20\x20\x20\x20\"http://www\.w3\.org/TR/html4/strict\.dtd\">\n<html>\n\x
SF:20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20http-equ
SF:iv=\"Content-Type\"\x20content=\"text/html;charset=utf-8\">\n\x20\x20\x
SF:20\x20\x20\x20\x20\x20<title>Error\x20response</title>\n\x20\x20\x20\x2
SF:0</head>\n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>E
SF:rror\x20response</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code
SF::\x20501</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Message:\x20Unsupporte
SF:d\x20method\x20\('OPTIONS'\)\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>
SF:Error\x20code\x20explanation:\x20HTTPStatus\.NOT_IMPLEMENTED\x20-\x20Se
SF:rver\x20does\x20not\x20support\x20this\x20operation\.</p>\n\x20\x20\x20
SF:\x20</body>\n</html>\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


┌──(duke㉿kali)-[~/Documents/THM_BrickByBrick]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u https://bricks.thm -x .php, .txt, .html -k | egrep -v "Status: 301"
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://bricks.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s
===============================================================
2024/04/18 07:24:48 Starting gobuster in directory enumeration mode
===============================================================
/login                (Status: 302) [Size: 0] [--> https://bricks.thm/wp-login.php]
/login.php            (Status: 302) [Size: 0] [--> https://bricks.thm/wp-login.php]
/admin                (Status: 302) [Size: 0] [--> https://bricks.thm/wp-admin/]                 
/wp-login.php         (Status: 200) [Size: 4042]                                                 
/dashboard            (Status: 302) [Size: 0] [--> https://bricks.thm/wp-admin/]  


