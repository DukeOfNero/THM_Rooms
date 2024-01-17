Link: https://tryhackme.com/room/gallery666
<code>

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
</code>
