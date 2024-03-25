<code>
  
### Enumeration nmap, gobuster
  
┌──(duke㉿kali)-[~/Documents/THM_LessonLearned]
└─$ nmap  -sV -Pn 10.10.177.226
Starting Nmap 7.92 ( https://nmap.org ) at 2024-03-22 03:57 CDT
Nmap scan report for 10.10.177.226
Host is up (0.035s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
80/tcp open  http    Apache httpd 2.4.54 ((Debian))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.38 seconds

┌─(duke㉿kali)-[/Documents/THM_LessonLearned]
└$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.177.226 -x .php, .txt, .html

Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

[+] Url:                     http://10.10.177.226
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s

2024/03/22 03:59:43 Starting gobuster in directory enumeration mode

/index.php            (Status: 200) [Size: 1223]
/manual               (Status: 301) [Size: 315] [--> http://10.10.177.226/manual/]
/server-status        (Status: 403) [Size: 278]                                   
                                                                                  

2024/03/22 04:38:45 Finished

### sql injection ' or 1=1

Oops! It looks like you injected an OR 1=1 or similar into the username field. This wouldn't have bypassed the login because every row in the users table was returned, and the login check only proceeds if one row matches the query.

However, your injection also made it into a DELETE statement, and now the flag is gone. Like, completely gone. You need to reset the box to restore it, sorry.

OR 1=1 is dangerous and should almost never be used for precisely this reason. Not even SQLmap uses OR unless you set --risk=3 (the maximum). Be better. Be like SQLmap.

Lesson learned?

P.S. maybe there is less destructive way to bypass the login...

##  1' union select null -- -
  
</code>
