

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
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://gallery.thm:8080 -x .txt,.php,html
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://gallery.thm:8080
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,html,txt
[+] Timeout:                 10s
===============================================================
2024/01/17 04:09:50 Starting gobuster in directory enumeration mode
===============================================================
Error: the server returns a status code that matches the provided options for non existing urls. http://gallery.thm:8080/2b526247-78bc-4acb-a809-fbb1c006d055 => 200 (Length: 15757). To continue please exclude the status code, the length or use the --wildcard switch
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Gallery]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://gallery.thm -p 8080 -x .txt,.php,html
Error: error on parsing arguments: pattern file "8080" does not exist: stat 8080: no such file or directory
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Gallery]
└─$ gobuster --help                                                                                                             
Usage:
  gobuster [command]

Available Commands:
  dir         Uses directory/file enumeration mode
  dns         Uses DNS subdomain enumeration mode
  fuzz        Uses fuzzing mode
  help        Help about any command
  s3          Uses aws bucket enumeration mode
  version     shows the current version
  vhost       Uses VHOST enumeration mode

Flags:
      --delay duration    Time each thread waits between requests (e.g. 1500ms)
  -h, --help              help for gobuster
      --no-error          Don't display errors
  -z, --no-progress       Don't display progress
  -o, --output string     Output file to write results to (defaults to stdout)
  -p, --pattern string    File containing replacement patterns
  -q, --quiet             Don't print the banner and other noise
  -t, --threads int       Number of concurrent threads (default 10)
  -v, --verbose           Verbose output (errors)
  -w, --wordlist string   Path to the wordlist

Use "gobuster [command] --help" for more information about a command.
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Gallery]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://gallery.thm:8080 -x .txt,.php,html   
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://gallery.thm:8080
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php,html
[+] Timeout:                 10s
===============================================================
2024/01/17 04:10:31 Starting gobuster in directory enumeration mode
===============================================================
Error: the server returns a status code that matches the provided options for non existing urls. http://gallery.thm:8080/ac637471-f42f-44ce-a1d0-513623f422b1 => 200 (Length: 15757). To continue please exclude the status code, the length or use the --wildcard switch
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Gallery]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://gallery.thm:8080 -x .txt,.php,html
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://gallery.thm:8080
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php,html
[+] Timeout:                 10s
===============================================================
2024/01/17 04:11:03 Starting gobuster in directory enumeration mode
===============================================================
Error: the server returns a status code that matches the provided options for non existing urls. http://gallery.thm:8080/53c547a3-0e55-4e38-944f-140ecaf33f59 => 200 (Length: 15757). To continue please exclude the status code, the length or use the --wildcard switch
                                                                                                                                                                                                                                           
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
