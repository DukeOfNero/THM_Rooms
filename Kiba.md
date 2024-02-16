link: https://tryhackme.com/room/kiba
<code>
** Enumaration
┌──(duke㉿kali)-[~/Documents/THM_Kiba]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.124.166 -x .txt,.php,html
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.124.166
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php,html
[+] Timeout:                 10s
===============================================================
2024/02/16 02:48:08 Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 1291]
/server-status        (Status: 403) [Size: 278] 
                                                
===============================================================
2024/02/16 03:43:29 Finished
===============================================================
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Kiba]
└─$ nmap  -p- -Pn 10.10.124.166
Starting Nmap 7.92 ( https://nmap.org ) at 2024-02-16 03:57 CST
Nmap scan report for 10.10.124.166
Host is up (0.036s latency).
Not shown: 65531 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
5044/tcp open  lxi-evntsvc
5601/tcp open  esmagent

Nmap done: 1 IP address (1 host up) scanned in 23.05 seconds

** found Kibana Version: 6.5.4

</code>
