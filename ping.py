pytask
======
import ping, socket
try:
    ping.verbose_ping('www.google.com', count=3)
    delay = ping.Ping('www.wikipedia.org', timeout=2000).do()
except socket.error, 
else:
     print "Ping Error:", 
