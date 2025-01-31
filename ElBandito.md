<code>

https://tryhackme.com/r/room/elbandito

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
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://elbandito.thm:8080
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
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
===============================================================
Finished
===============================================================
                                                                     

</code>
