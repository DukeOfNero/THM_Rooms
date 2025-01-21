<Code>

## LIGHT

https://tryhackme.com/r/room/lightroom

### Enumeration
  
┌──(kali㉿kali)-[~/Documents/THM]
└─$ nmap -sV -A -Pn  -p- 10.10.78.225
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-21 13:27 CET
Nmap scan report for 10.10.78.225
Host is up (0.038s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 61:c5:06:f2:4a:20:5b:cd:09:4d:72:b0:a5:aa:ce:71 (RSA)
|   256 51:e0:5f:fa:81:64:d3:d9:26:24:16:ca:45:94:c2:00 (ECDSA)
|_  256 77:e1:36:3b:95:9d:e0:3e:0a:56:82:b2:9d:4c:fe:1a (ED25519)
1337/tcp open  waste?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Kerberos, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServerCookie, X11Probe: 
|     Welcome to the Light database!
|     Please enter your username:
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, RTSPRequest: 
|     Welcome to the Light database!
|     Please enter your username: Username not found.
|_    Please enter your username:
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port1337-TCP:V=7.94SVN%I=7%D=1/21%Time=678F9806%P=x86_64-pc-linux-gnu%r
SF:(NULL,3B,"Welcome\x20to\x20the\x20Light\x20database!\nPlease\x20enter\x
SF:20your\x20username:\x20")%r(GenericLines,6B,"Welcome\x20to\x20the\x20Li
SF:ght\x20database!\nPlease\x20enter\x20your\x20username:\x20Username\x20n
SF:ot\x20found\.\nPlease\x20enter\x20your\x20username:\x20")%r(GetRequest,
SF:6B,"Welcome\x20to\x20the\x20Light\x20database!\nPlease\x20enter\x20your
SF:\x20username:\x20Username\x20not\x20found\.\nPlease\x20enter\x20your\x2
SF:0username:\x20")%r(HTTPOptions,6B,"Welcome\x20to\x20the\x20Light\x20dat
SF:abase!\nPlease\x20enter\x20your\x20username:\x20Username\x20not\x20foun
SF:d\.\nPlease\x20enter\x20your\x20username:\x20")%r(RTSPRequest,6B,"Welco
SF:me\x20to\x20the\x20Light\x20database!\nPlease\x20enter\x20your\x20usern
SF:ame:\x20Username\x20not\x20found\.\nPlease\x20enter\x20your\x20username
SF::\x20")%r(RPCCheck,3B,"Welcome\x20to\x20the\x20Light\x20database!\nPlea
SF:se\x20enter\x20your\x20username:\x20")%r(DNSVersionBindReqTCP,3B,"Welco
SF:me\x20to\x20the\x20Light\x20database!\nPlease\x20enter\x20your\x20usern
SF:ame:\x20")%r(DNSStatusRequestTCP,3B,"Welcome\x20to\x20the\x20Light\x20d
SF:atabase!\nPlease\x20enter\x20your\x20username:\x20")%r(Help,6B,"Welcome
SF:\x20to\x20the\x20Light\x20database!\nPlease\x20enter\x20your\x20usernam
SF:e:\x20Username\x20not\x20found\.\nPlease\x20enter\x20your\x20username:\
SF:x20")%r(SSLSessionReq,3B,"Welcome\x20to\x20the\x20Light\x20database!\nP
SF:lease\x20enter\x20your\x20username:\x20")%r(TerminalServerCookie,3B,"We
SF:lcome\x20to\x20the\x20Light\x20database!\nPlease\x20enter\x20your\x20us
SF:ername:\x20")%r(TLSSessionReq,3B,"Welcome\x20to\x20the\x20Light\x20data
SF:base!\nPlease\x20enter\x20your\x20username:\x20")%r(Kerberos,3B,"Welcom
SF:e\x20to\x20the\x20Light\x20database!\nPlease\x20enter\x20your\x20userna
SF:me:\x20")%r(SMBProgNeg,3B,"Welcome\x20to\x20the\x20Light\x20database!\n
SF:Please\x20enter\x20your\x20username:\x20")%r(X11Probe,3B,"Welcome\x20to
SF:\x20the\x20Light\x20database!\nPlease\x20enter\x20your\x20username:\x20
SF:")%r(FourOhFourRequest,6B,"Welcome\x20to\x20the\x20Light\x20database!\n
SF:Please\x20enter\x20your\x20username:\x20Username\x20not\x20found\.\nPle
SF:ase\x20enter\x20your\x20username:\x20");


┌──(kali㉿kali)-[~]
└─$ nc 10.10.78.225 1337
Welcome to the Light database!
Please enter your username: smokey
Password: vYQ5ngPpw8AdUmL



<\Code>
