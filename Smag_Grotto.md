<code>

  ### Service Enumeration - nmap  gobuster nikto 
  
┌──(duke㉿kali)-[~/Documents/THM_Smag_Grotto]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.19.178     

[+] Url:                     http://10.10.19.178
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s

/mail                 (Status: 301) [Size: 311] [--> http://10.10.19.178/mail/]
/server-status        (Status: 403) [Size: 277]                                
                                                                               
2024/03/19 05:15:15 Finished
                                                                                                                   
┌──(duke㉿kali)-[~/Documents/THM_Smag_Grotto]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://development.smag.thm -x .php, .txt
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
[+] Url:                     http://development.smag.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s
2024/03/19 05:16:48 Starting gobuster in directory enumeration mode
/login.php            (Status: 200) [Size: 1035]
/admin.php            (Status: 302) [Size: 0] [--> login.php]
/server-status        (Status: 403) [Size: 285]              

┌──(duke㉿kali)-[~/Documents/THM_Smag_Grotto]
└─$ nikto  -h http://development.smag.thm
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.19.178
+ Target Hostname:    development.smag.thm
+ Target Port:        80
+ Start Time:         2024-03-19 06:38:17 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ OSVDB-3268: /: Directory indexing found.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS 
+ Cookie PHPSESSID created without the httponly flag
+ OSVDB-3268: /./: Directory indexing found.
+ /./: Appending '/./' to a directory allows indexing
+ OSVDB-3268: //: Directory indexing found.
+ //: Apache on Red Hat Linux release 9 reveals the root directory listing by default if there is no index page.
+ OSVDB-3268: /%2e/: Directory indexing found.
+ OSVDB-576: /%2e/: Weblogic allows source code or directory listing, upgrade to v6.0 SP1 or higher. http://www.securityfocus.com/bid/2513.
+ OSVDB-3268: ///: Directory indexing found.
+ OSVDB-119: /?PageServices: The remote server may allow directory listings through Web Publisher by forcing the server to show all files via 'open directory browsing'. Web Publisher should be disabled. http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0269.
+ OSVDB-119: /?wp-cs-dump: The remote server may allow directory listings through Web Publisher by forcing the server to show all files via 'open directory browsing'. Web Publisher should be disabled. http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-1999-0269.
+ OSVDB-3268: ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////: Directory indexing found.
+ OSVDB-3288: ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////: Abyss 1.03 reveals directory listing when         /'s are requested.
+ OSVDB-3233: /icons/README: Apache default file found.
+ /login.php: Admin login page/section found.
+ 7863 requests: 0 error(s) and 20 item(s) reported on remote host
+ End Time:           2024-03-19 06:44:21 (GMT-5) (364 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested


in /mail found

<a>To: netadmin@smag.thm</a>
<a>Cc: uzi@smag.thm</a>
<!-- <a>Bcc: trodd@smag.thm</a> -->
<a>From: jake@smag.thm</a>


username=helpdesk&password=cH4nG3M3_n0w

### Subdomain Enumeration

                                                                                                                                                                                                                                          
┌──(duke㉿kali)-[~/Documents/THM_Smag_Grotto]
└─$ ffuf -w ../../www/wordlists/Subdomain.txt -H "HOST: FUZZ.smag.thm" -u http://smag.thm

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://smag.thm
 :: Wordlist         : FUZZ: ../../www/wordlists/Subdomain.txt
 :: Header           : Host: FUZZ.smag.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

media                   [Status: 200, Size: 402, Words: 69, Lines: 13, Duration: 40ms]
ftp                     [Status: 200, Size: 402, Words: 69, Lines: 13, Duration: 40ms]
wap                     [Status: 200, Size: 402, Words: 69, Lines: 13, Duration: 40ms]
ns1                     [Status: 200, Size: 402, Words: 69, Lines: 13, Duration: 40ms]

#### Filter size 402
                                                                                                                                                                                                                                           
┌──(duke㉿kali)-[~/Documents/THM_Smag_Grotto]
└─$ ffuf -w ../../www/wordlists/Subdomain.txt -H "HOST: FUZZ.smag.thm" -u http://smag.thm -fs 402

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://smag.thm
 :: Wordlist         : FUZZ: ../../www/wordlists/Subdomain.txt
 :: Header           : Host: FUZZ.smag.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 402
________________________________________________

development             [Status: 200, Size: 1176, Words: 76, Lines: 18, Duration: 32ms]
development             [Status: 200, Size: 1176, Words: 76, Lines: 18, Duration: 31ms]


<\code>
