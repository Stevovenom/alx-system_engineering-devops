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
3. Add the subdomain web-02 to your domain, point it to your web-02 IP<br>i

Also the 0-world_trial file also achieves teh said task. Though it is short, brief and precise and achieves the said task efficiently. <br>
# Task 1
for the completono of this task, folow through with this one: <a href="https://gbeminiyi.hashnode.dev/installing-certbot-in-your-haproxy-load-balancer-server">Installing Certbot in HAProxy</a>.<br>

By following the steps in the link above, I made configuartions to teh haproxy files and reached a deadend<br>
<code>
ubuntu@495864-lb-01:~$ ls
appending_the_config  installation  snap
ubuntu@495864-lb-01:~$ sudo service haproxy start
Job for haproxy.service failed because the control process exited with error code.
See "systemctl status haproxy.service" and "journalctl -xe" for details.
ubuntu@495864-lb-01:~$ systemctl status haproxy.service
● haproxy.service - HAProxy Load Balancer
     Loaded: loaded (/lib/systemd/system/haproxy.service; enabled; vendor preset: enabled)
     Active: failed (Result: exit-code) since Mon 2024-07-15 09:55:09 UTC; 16s ago
       Docs: man:haproxy(1)
             file:/usr/share/doc/haproxy/configuration.txt.gz
    Process: 84613 ExecStartPre=/usr/sbin/haproxy -Ws -f $CONFIG -c -q $EXTRAOPTS (code=exited, status=1/FAILURE)

Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:55:09 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 5.
Jul 15 09:55:09 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Start request repeated too quickly.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:55:09 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
ubuntu@495864-lb-01:~$ journalctl -xe
-- Defined-By: systemd
-- Support: http://www.ubuntu.com/support
-- 
-- A start job for unit haproxy.service has finished with a failure.
-- 
-- The job identifier is 19109 and the job result is failed.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 5.
-- Subject: Automatic restarting of a unit has been scheduled
-- Defined-By: systemd
-- Support: http://www.ubuntu.com/support
-- 
-- Automatic restarting of the unit haproxy.service has been scheduled, as the result for
-- the configured Restart= setting for the unit.
Jul 15 09:55:09 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
-- Subject: A stop job for unit haproxy.service has finished
-- Defined-By: systemd
-- Support: http://www.ubuntu.com/support
-- 
-- A stop job for unit haproxy.service has finished.
-- 
-- The job identifier is 19192 and the job result is done.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Start request repeated too quickly.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
-- Subject: Unit failed
-- Defined-By: systemd
-- Support: http://www.ubuntu.com/support
-- 
-- The unit haproxy.service has entered the 'failed' state with result 'exit-code'.
Jul 15 09:55:09 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
-- Subject: A start job for unit haproxy.service has failed
-- Defined-By: systemd
-- Support: http://www.ubuntu.com/support
-- 
-- A start job for unit haproxy.service has finished with a failure.
-- 
-- The job identifier is 19192 and the job result is failed.
...skipping...
-- Defined-By: systemd
-- Support: http://www.ubuntu.com/support
-- 
ubuntu@495864-lb-01:~$ cd /etc/haproxy
ubuntu@495864-lb-01:/etc/haproxy$ ls
certs  errors  haproxy.cfg
ubuntu@495864-lb-01:/etc/haproxy$ sudo vim haproxy.cfg
ubuntu@495864-lb-01:/etc/haproxy$ sudo service haproxy start
ubuntu@495864-lb-01:/etc/haproxy$ sudo journalctl -u haproxy.service --since "10 minutes ago"
-- Logs begin at Thu 2024-07-11 07:51:57 UTC, end at Mon 2024-07-15 09:59:31 UTC. --
-- Logs begin at Thu 2024-07-11 07:51:57 UTC, end at Mon 2024-07-15 09:59:31 UTC. --
Jul 15 09:50:24 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:50:24 495864-lb-01 haproxy[84411]: [ALERT] 196/095024 (84411) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:50:24 495864-lb-01 haproxy[84411]: [ALERT] 196/095024 (84411) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:50:24 495864-lb-01 haproxy[84411]: [ALERT] 196/095024 (84411) : Fatal errors found in configuration.
Jul 15 09:50:24 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:50:24 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:24 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:25 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 1.
Jul 15 09:50:25 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:50:25 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:50:25 495864-lb-01 haproxy[84413]: [ALERT] 196/095025 (84413) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:50:25 495864-lb-01 haproxy[84413]: [ALERT] 196/095025 (84413) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:50:25 495864-lb-01 haproxy[84413]: [ALERT] 196/095025 (84413) : Fatal errors found in configuration.
Jul 15 09:50:25 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:50:25 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:25 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:25 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 2.
Jul 15 09:50:25 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:50:25 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:50:25 495864-lb-01 haproxy[84415]: [ALERT] 196/095025 (84415) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:50:25 495864-lb-01 haproxy[84415]: [ALERT] 196/095025 (84415) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:50:25 495864-lb-01 haproxy[84415]: [ALERT] 196/095025 (84415) : Fatal errors found in configuration.
Jul 15 09:50:25 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:50:25 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:25 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:25 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 3.
Jul 15 09:50:25 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:50:25 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:50:25 495864-lb-01 haproxy[84417]: [ALERT] 196/095025 (84417) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:50:25 495864-lb-01 haproxy[84417]: [ALERT] 196/095025 (84417) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:50:25 495864-lb-01 haproxy[84417]: [ALERT] 196/095025 (84417) : Fatal errors found in configuration.
Jul 15 09:50:25 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:50:25 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:25 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:26 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 4.
Jul 15 09:50:26 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:50:26 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:50:26 495864-lb-01 haproxy[84419]: [ALERT] 196/095026 (84419) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:50:26 495864-lb-01 haproxy[84419]: [ALERT] 196/095026 (84419) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:50:26 495864-lb-01 haproxy[84419]: [ALERT] 196/095026 (84419) : Fatal errors found in configuration.
Jul 15 09:50:26 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:50:26 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:26 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:26 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 5.
Jul 15 09:50:26 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:50:26 495864-lb-01 systemd[1]: haproxy.service: Start request repeated too quickly.
Jul 15 09:50:26 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:26 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:37 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:50:37 495864-lb-01 haproxy[84424]: [ALERT] 196/095037 (84424) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:50:37 495864-lb-01 haproxy[84424]: [ALERT] 196/095037 (84424) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:50:37 495864-lb-01 haproxy[84424]: [ALERT] 196/095037 (84424) : Fatal errors found in configuration.
Jul 15 09:50:37 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:50:37 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:37 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:37 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 1.
Jul 15 09:50:37 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:50:37 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:50:37 495864-lb-01 haproxy[84426]: [ALERT] 196/095037 (84426) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:50:37 495864-lb-01 haproxy[84426]: [ALERT] 196/095037 (84426) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:50:37 495864-lb-01 haproxy[84426]: [ALERT] 196/095037 (84426) : Fatal errors found in configuration.
Jul 15 09:50:37 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:50:37 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:37 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:37 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 2.
Jul 15 09:50:37 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:50:37 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:50:37 495864-lb-01 haproxy[84428]: [ALERT] 196/095037 (84428) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:50:37 495864-lb-01 haproxy[84428]: [ALERT] 196/095037 (84428) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:50:37 495864-lb-01 haproxy[84428]: [ALERT] 196/095037 (84428) : Fatal errors found in configuration.
Jul 15 09:50:37 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:50:37 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:37 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:38 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 3.
Jul 15 09:50:38 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:50:38 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:50:38 495864-lb-01 haproxy[84430]: [ALERT] 196/095038 (84430) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:50:38 495864-lb-01 haproxy[84430]: [ALERT] 196/095038 (84430) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:50:38 495864-lb-01 haproxy[84430]: [ALERT] 196/095038 (84430) : Fatal errors found in configuration.
Jul 15 09:50:38 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:50:38 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:38 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:38 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 4.
Jul 15 09:50:38 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:50:38 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:50:38 495864-lb-01 haproxy[84432]: [ALERT] 196/095038 (84432) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:50:38 495864-lb-01 haproxy[84432]: [ALERT] 196/095038 (84432) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:50:38 495864-lb-01 haproxy[84432]: [ALERT] 196/095038 (84432) : Fatal errors found in configuration.
Jul 15 09:50:38 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:50:38 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:38 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:50:38 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 5.
Jul 15 09:50:38 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:50:38 495864-lb-01 systemd[1]: haproxy.service: Start request repeated too quickly.
Jul 15 09:50:38 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:50:38 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:53:12 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:53:12 495864-lb-01 haproxy[84449]: [ALERT] 196/095312 (84449) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:53:12 495864-lb-01 haproxy[84449]: [ALERT] 196/095312 (84449) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:53:12 495864-lb-01 haproxy[84449]: [ALERT] 196/095312 (84449) : Fatal errors found in configuration.
Jul 15 09:53:12 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:53:12 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:53:12 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 1.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:53:13 495864-lb-01 haproxy[84451]: [ALERT] 196/095313 (84451) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:53:13 495864-lb-01 haproxy[84451]: [ALERT] 196/095313 (84451) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:53:13 495864-lb-01 haproxy[84451]: [ALERT] 196/095313 (84451) : Fatal errors found in configuration.
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 2.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:53:13 495864-lb-01 haproxy[84453]: [ALERT] 196/095313 (84453) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:53:13 495864-lb-01 haproxy[84453]: [ALERT] 196/095313 (84453) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:53:13 495864-lb-01 haproxy[84453]: [ALERT] 196/095313 (84453) : Fatal errors found in configuration.
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 3.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:53:13 495864-lb-01 haproxy[84455]: [ALERT] 196/095313 (84455) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:53:13 495864-lb-01 haproxy[84455]: [ALERT] 196/095313 (84455) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:53:13 495864-lb-01 haproxy[84455]: [ALERT] 196/095313 (84455) : Fatal errors found in configuration.
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 4.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:53:13 495864-lb-01 haproxy[84457]: [ALERT] 196/095313 (84457) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:53:13 495864-lb-01 haproxy[84457]: [ALERT] 196/095313 (84457) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:53:13 495864-lb-01 haproxy[84457]: [ALERT] 196/095313 (84457) : Fatal errors found in configuration.
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:53:13 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:53:13 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:53:14 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 5.
Jul 15 09:53:14 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:53:14 495864-lb-01 systemd[1]: haproxy.service: Start request repeated too quickly.
Jul 15 09:53:14 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:53:14 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:55:07 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:55:07 495864-lb-01 haproxy[84605]: [ALERT] 196/095507 (84605) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:55:07 495864-lb-01 haproxy[84605]: [ALERT] 196/095507 (84605) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:55:07 495864-lb-01 haproxy[84605]: [ALERT] 196/095507 (84605) : Fatal errors found in configuration.
Jul 15 09:55:07 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:55:07 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:55:07 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:55:08 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 1.
Jul 15 09:55:08 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:55:08 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:55:08 495864-lb-01 haproxy[84607]: [ALERT] 196/095508 (84607) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:55:08 495864-lb-01 haproxy[84607]: [ALERT] 196/095508 (84607) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:55:08 495864-lb-01 haproxy[84607]: [ALERT] 196/095508 (84607) : Fatal errors found in configuration.
Jul 15 09:55:08 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:55:08 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:55:08 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:55:08 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 2.
Jul 15 09:55:08 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:55:08 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:55:08 495864-lb-01 haproxy[84609]: [ALERT] 196/095508 (84609) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:55:08 495864-lb-01 haproxy[84609]: [ALERT] 196/095508 (84609) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:55:08 495864-lb-01 haproxy[84609]: [ALERT] 196/095508 (84609) : Fatal errors found in configuration.
Jul 15 09:55:08 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:55:08 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:55:08 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:55:08 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 3.
Jul 15 09:55:08 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:55:08 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:55:08 495864-lb-01 haproxy[84611]: [ALERT] 196/095508 (84611) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:55:08 495864-lb-01 haproxy[84611]: [ALERT] 196/095508 (84611) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:55:08 495864-lb-01 haproxy[84611]: [ALERT] 196/095508 (84611) : Fatal errors found in configuration.
Jul 15 09:55:08 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:55:08 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:55:08 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 4.
Jul 15 09:55:09 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:55:09 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:55:09 495864-lb-01 haproxy[84613]: [ALERT] 196/095509 (84613) : parsing [/etc/haproxy/haproxy.cfg:38] : 'bind *:443' : unable to load SSL >
Jul 15 09:55:09 495864-lb-01 haproxy[84613]: [ALERT] 196/095509 (84613) : Error(s) found in configuration file : /etc/haproxy/haproxy.cfg
Jul 15 09:55:09 495864-lb-01 haproxy[84613]: [ALERT] 196/095509 (84613) : Fatal errors found in configuration.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Control process exited, code=exited, status=1/FAILURE
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:55:09 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Scheduled restart job, restart counter is at 5.
Jul 15 09:55:09 495864-lb-01 systemd[1]: Stopped HAProxy Load Balancer.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Start request repeated too quickly.
Jul 15 09:55:09 495864-lb-01 systemd[1]: haproxy.service: Failed with result 'exit-code'.
Jul 15 09:55:09 495864-lb-01 systemd[1]: Failed to start HAProxy Load Balancer.
Jul 15 09:58:42 495864-lb-01 systemd[1]: Starting HAProxy Load Balancer...
Jul 15 09:58:42 495864-lb-01 haproxy[84637]: Proxy stevovenom_frontend started.
Jul 15 09:58:42 495864-lb-01 haproxy[84637]: Proxy stevovenom_frontend started.
Jul 15 09:58:42 495864-lb-01 haproxy[84637]: Proxy stevovenom_backend started.
Jul 15 09:58:42 495864-lb-01 haproxy[84637]: Proxy stevovenom_backend started.
Jul 15 09:58:42 495864-lb-01 haproxy[84637]: [NOTICE] 196/095842 (84637) : New worker #1 (84639) forked
Jul 15 09:58:42 495864-lb-01 systemd[1]: Started HAProxy Load Balancer.
</code><br>
For easier debugging and getting on track, follow through here:<br>
<a href="https://chatgpt.com/share/0451db47-19f6-47d9-a3ae-bc7ba7b4a8a4">Debugging and getting back on track</a>
