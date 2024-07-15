##0x10-https_ssl
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png">

1. <a href="https://intranet.alxswe.com/rltoken/XT1BAiBL3Jpq1bn1q6IYXQ">What is HTTPS</a>
2. <a href="https://intranet.alxswe.com/rltoken/STj5WkAPACBxOvwB77Ycrw">What are the two main elements that SSL is providing</a>
3. <a href="https://intranet.alxswe.com/rltoken/asrMHTWJxWQ2x-Sn6snHow">HAPROXY SSL termination on ubuntu 16.0</a>
4. <a href="https://intranet.alxswe.com/rltoken/CKUICfppIWI6UC0coEMB8g">SSL termination</a>
5. <a href="https://intranet.alxswe.com/rltoken/zPjZ7-eSSQsLFsGA16C1HQ">BASH functions</a>
<br>
<strong>A TLS termination proxy (or SSL termination proxy,[1] or SSL offloading[2])</strong> is a proxy server that acts as an intermediary point between client and server applications, and is used to terminate and/or establish TLS (or DTLS) tunnels by decrypting and/or encrypting communications. This is different from TLS pass-through proxies that forward encrypted TLS traffic between clients and servers without terminating the tunnel.

<br>Uses</br>
TLS termination proxies can be used to:<br>

1. secure plaintext communications over untrusted networks by tunnelling them in TLS,
2. allow inspection of encrypted traffic by an intrusion detection system to detect and block malicious activities,
3. allow network surveillance and analyze encrypted traffic,
4. enable otherwise unsupported integration with other applications that provide additional capabilities such as content filtering or Hardware security module,
enable TLS protocol versions, extensions, or capabilities (e.g. OCSP stapling, ALPN, DANE, CT validation, etc.) unsupported by client or server applications to enhance their compatibility and/or security, work around buggy/insecure TLS implementations in client or server applications to improve their compatibility and/or security,
6. provide additional certificate-based authentication unsupported by server and/or client applications or protocols,
7. provide an additional defence-in-depth layer for centralised control and consistent management of TLS configuration and associated security policies
8. reduce the load on the main servers by offloading the cryptographic processing to another machine.
<br>
#Types
TLS termination proxies can provide three connectivity patterns:<br>

1. <strong>TLS Offloading</strong> of inbound encrypted TLS connection from a client and forwarding communications over a plain text connection to the server.<br>
2. <strong>TLS Encryption</strong> of inbound plaintext connection from a client and forwarding communications over an encrypted TLS connection to the server.<br>
3. <strong>TLS Bridging</strong> of two encrypted TLS connections to allow inspection and filtering of encrypted traffic by decrypting inbound TLS connection from a client and re-encrypting it with another TLS connection to the server.

#Task 0
For this particular task, we need to Configure our domain zone so that the subdomain www points to your load-balancer IP (lb-01). Also, <br>
Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)
1. Add the subdomain lb-01 to your domain, point it to your lb-01 IP
2. Add the subdomain web-01 to your domain, point it to your web-01 IP
3. Add the subdomain web-02 to your domain, point it to your web-02 IP<br>
