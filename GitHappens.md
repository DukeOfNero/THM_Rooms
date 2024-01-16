<code>
  
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
