<code>
https://tryhackme.com/r/room/bypass





### found in /mail
From: steve@cctv.thm
To: mark@cctv.thm
Subject: Important Credentials

Hey Mark,

I have completed all the formalities for securing our CCTV web panel (cctv.thm:443). I have installed Suricata to automatically detect any invalid connection and enabled two-layer protection for the web panel. I will SMS you the passwords but incase if you misplace them, there is no possibility for recovery. 

We can recover the password only if we send some specially crafted packets 	
-	Make a UDP request to the machine with source port number 5000. Once done, you can fetch the flag through /fpassword.php?id=1
-	Make a TCP request to fpassword.php?id=2 with user-agent set as "I am Steve Friend". Once done, you can fetch the flag through /fpassword.php?id=2
-	Send a ping packet to the machine appearing as Mozilla browser (Hint: packet content with user agent set as Mozilla). Once done, you can fetch the flag through /fpassword.php?id=3
-	Attempt to login to the FTP server with content containing the word "user" in it. Once done, you can fetch the flag from /fpassword.php?id=4
-	Send TCP request to flagger.cgi endpoint with a host header containing more than 50 characters. Once done, you can fetch the flag from /fpassword.php?id=5

After receiving all the flags, you can visit the MACHINE IP that will ask you for the password. The first password will be concatenated values of all five flags you have received above.

For the second layer of security, I have enabled a wholly sandboxed login environment with no connection to the database and no possibility of command execution. The username is the computer's hostname, and the password is the same as the previous password. I will SMS you the details as well.


See ya soon

Steve
Dev Ops Engineer

<\code>
