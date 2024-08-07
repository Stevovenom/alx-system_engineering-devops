## WEB SERVERS
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png" alt="" loading="lazy" style="">
<strong>A SERVER IS like a central hub that other devices connect to inorder to acces services or resources</strong>, hence through this definition, the term <strong>WEB SERVER </strong> basically refers to a software or a computer program that delivers web pages or serve static contents to clients over the internet.For more information on the working of a web server, one can refer to <a href="https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server#:~:text=On%20the%20hardware%20side%2C%20a,devices%20connected%20to%20the%20web.">click here</a><br>
Physical servers are physical computers that are eithe installed in an organization premise to achieve a articular task i.e this could be either hhosting etc while virtual servers run on top of host machines.
In contrast to virtual servers, physical servers operate on specfic operating system and are capable of handling high loads of traffic and demanding workloads.

Examples of webservers
1. Apache HTTP servers
2. Nginx(engine x)
3. litespeed
4. Gunicorn

## Task 0
<header>how to transfer files to a server</header>

scp - it copies files securely to my root, since files within the network can be intercepted
have 4 parameters:

1. files location
2. Server's IP address
3. The user name
4. the path to my private key

Incase i dont use the 4 parameters, i get the error Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
how disable strict host checking

<code>

#!/usr/bin/env bash
#checking parameters for file transfer
#0-success, 1-error

if [ $# -lt 4 ]
then
	echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
	exit 1
fi

#asigning parameters to variables

path_to_file=$1
ip_address=$2
user_name=$3
path_to_ssh_key=$4

#disable strict host key checking

scp -o "StrictHostKeyChecking=no" -i "$path_to_ssh_key" "$path_to_file" "$username@$ip:~/"

#checking if the file transfer was successful

if [ $? -eq 0 ]
then
	echo "FILE TRANSFER SUCCESSFUL"
else
	echo "FILE TRANSFER NOT SUCCESSFUL"
</code>

## task 1
<header>how to install engine x(Nginx)</header>

First, we need to switch to our web-01 and hence to do that we use:<br>
<code>ssh -i ~/.ssh/school ubuntu@<ip-address></code>

The steps to follow through with are:<br>
1. first update
<code>sudo apt-get update</code>

<code>sudo apt-get install -y nginx</code>

The -y flag just means yes and it just removs the prompt of having to type yes. It is essential in most scenarios when trying to install an application without any prompts of acceptance or denial.

Then one can start the nginx is: <code>sudo service nginx start </code>.<br></br>


now back to the 0x0c-web_server, run the command

<code>scp -o "StrictHostKeyChecking no" -i "<path-to-the-ssh-key>" "<path-to-the-file-being-transferred>" "ubuntu@<ip-address>:~/"</code>

By now doing this, if you switch to the web-server, the named file has now been copied. That is, part of task 1.<br></br>

for task use the web-server to achieve this task

now cd /var then cd www then again cd html

take the ip address and in a new tab paste the ip address, youj should be able to see a welcome page to Nginx and now it should display hello world


in the html add echo "Hello World!" | sudo tee /var/www/html/index.html

then sudo nginx -t to test configuration

then now restart throgh 
<code>
sudo service nginx restart
sudo service nginx reload
</code>

now back to our sandbox,

first had used the command for the vim 1-install_ngix shown below:- <br>
<code>
#!/usr/bin/env bash
#commands for successful installation of nginx web server

sudo apt-get update
sudo apt-get install nginx
sudo ufw 'Nginx HTTP' # this is to enable the Nginx to use the firewall

echo "Hello World!" | sudo -tee /var/www/html/index.html

#this is testing nginx configuration
sudo nginx -t
sudo service nginx reload
</code>
though I had some issues with the last checker and hence debugged to: <br></br>
<code>
#!/usr/bin/env bash
#commands for successful installation of nginx web server

sudo apt-get update
sudo apt-get install -y nginx

sudo service nginx start
sudo ufw allow  'Nginx HTTP' # this is to enable the Nginx to use the firewall

echo "Hello World!" | sudo tee /var/www/html/index.html

#this is testing nginx configuration
sudo nginx -t
sudo service nginx reload
</code><br></br>

<strong>N/B:</strong>

port 22 is for SSH<br>
port 80 is for HTTP<br>

## Task 2
For this task, it involves teh reation of a new domain name from <strong>.tech</strong> adn using the details gotten to acheve the task. The basis for this is for DNS management and just a continuation is : <br></br>

# Access DNS Management:
Navigate to the DNS management section for your domain.
Then add an A Record:

#Create a new A record:
Host/Name: Leave this field empty or enter "@" (depending on the DNS provider) to point the root domain.<br>
Type: A(This could not be necessary since you could not be given this option as you had already chosen it while seleting the creation type of a new record.<br>
Value: Use the IP address of your 495864-web-01 server.<br>
TTL: Set the TTL (Time to Live) to the default value or a lower value like 300 seconds for faster propagation.
Save the DNS Settings:<br>

Save the changes and wait for DNS propagation. This can take from a few minutes to a couple of hours.

#Verify DNS Setup
Check DNS Propagation:

Use a DNS lookup tool like WhatsMyDNS or the dig command to verify the A record:

<code>
dig yourdomainname.tech
</code><br>
Ensure the output shows your domain pointing to your ip-address.<br>


#Verify Domain Registrar:

Go to Whois Lookup and enter your domain name.<br>
Check that the registrar name in the JSON response is "registrarName": "Dotserve Inc". If it has this, go to your intranet profile and add the link to teh doman i.e, the yourdomainname.tech as guided.<br>

#Final Note
It may take some time for the DNS changes to propagate fully. If you encounter any issues, ensure the DNS settings are correctly configured and check the propagation status after some time.



## continuation

# Redirections and Error Codes

status codes

1xx => Informational

100 - continue
101 - Switching protocol
102 - Processing
103 - Early Hints

2xx => Successful

200 - OK
201 - Created
202 - Accepted
203 - Non-Authoritative Information
204 - No content
205 - Reset content
206 - Partial content
207 - Multi-status
208 - Already reported
226 - IM used


3xx => Redirections

300 - Multiple choices
301 - Moved permanently
302 - found (previously "moved Temporarily")
303 - see other
304 - Not modified 
305 - Use proxy
306 - switch proxy
307 - Temporary Redirect
308 - permanent Redirect

4xx => Client Error

400 - Bad request
401 - Unauthorized
402 - Payment required
403 - forbidden
404 - not found
405 - method not allowed
406 - not acceptable
407   proxy authentication required
408 - request timeout
409 - conflict
410 - gone
411 - length required
412 - precondition failed
413 - payload too large

5xx => Server errors

500 - internal server error
501 - not implemented
502 - bad gateway
503 - service unavailable
504 - gateway timeout
505 - http version not supported
506 - variant also negotiates
507 - insufficient storage
511 - Network Authentication required


## Task 3

how to use the sed command, an example:


for this particular task, I ran numerous commands in the to try and create the redirection in my default folder in /etc/nginx/sites-enabled in my web-01 server, the scripts are :- <br></br>
<code>
#using sed command to perform redirection

#string_for_replacement="server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/stevovenom permanent;"

#perform teh replacement using sed
#sudo sed -i "s/server_name _;/$string_for_replacement/" /etc/nginx/sites-enabled/default

#Define the string for replacement using echo and escape sequences
#string_for_replacement=$(echo -e "server_name _;\n\trewrite ^/redirect_me https://github.com/stevovenom permanent;")

#Perform the replacement using sed
#sudo sed -i "s|server_name _;|$string_for_replacement|" /etc/nginx/sites-enabled/default

#string_for_replacement=$(cat <<'EOF'
#server_name _;
#rewrite ^/redirect_me https://github.com/stevovenom permanent;
#EOF
#)

#Perform the replacement using sed
#sudo sed -i "s|server_name _;|$string_for_replacement|" /etc/nginx/sites-enabled/default
#
#Define the replacement string using a heredoc and save it to a temporary file
#cat <<'EOF' > /tmp/replacement.txt
#server_name _;
#rewrite ^/redirect_me https://github.com/stevovenom permanent;
#EOF

#Read the replacement string from the temporary file
#string_for_replacement=$(cat /tmp/replacement.txt)

#Perform the replacement using sed
#sudo sed -i "s|server_name _;|$string_for_replacement|" /etc/nginx/sites-enabled/default

#Clean up the temporary file
#rm /tmp/replacement.txt
#
#Define the replacement string directly in the script
#string_for_replacement='server_name _;
 #   rewrite ^/redirect_me https://github.com/stevovenom permanent;'

#Perform the replacement using sed
#sed -i "s|server_name _;|$string_for_replacement|" /etc/nginx/sites-enabled/default



#!/usr/bin/env bash

#Define the replacement string directly in the script
string_for_replacement='server_name _;rewrite ^/redirect_me https://github.com/stevovenom permanent;'

#Perform the replacement using sed
sudo sed -i "s|server_name _;|$string_for_replacement|" /etc/nginx/sites-enabled/default
</code><br></br>

All the comments are the scripts that i was trying to run but kept seeing an error output on executing the file: <br></br>
<code>
ubuntu@495864-web-01:~$ ./redirection
sed: -e expression #1, char 31: unterminated `s` command
ubuntu@495864-web-01:~$ sudo vim redirection

</code><br>

New_string = "GIVES BACK;\n404;\n using sed command\n;"
sed -i "s/GIVES BACK;/$NEW_string/" /root/file


now for task 3, switch to our web server

ssh -i ~/.ssh/school ubuntu@<ip-address>

now sudo vim redirections

# using sed command to perform redirections

string_for_replacememt = "server_name _i\n\trewrite ^\/\/github.com\/bestor permanent;"
sudo sed -i "s/server_name_:/$string_for_replacement/" /etc/nginx/sites-enabled/default


try to switch to this file

/etc/nginx/sites-enabled

sudo vim default:- copy and paste it somewhere for recovery so that if anything is not rigth, we can come back and install easily


now back to web-01, execute ./redirections

then cd /etc/nginx/sites-enabled then sudo vim default

then sudo nginx -t
then sudo service nginx restart

cd ..

cd /var/www/html
create another file that contains the redirect URL

sudo vim redirect_me

	this is the content to this particular file:-	https://github.com/besthorIgbe

then sudo nginx -t

then restart:   sudo service nginx restart
repeat

exit or one can just use logout

now create a script for entirely everything

curl -sI <ip address>/redirect_me

now

vim 3-redirect

<code>

#!/usr/bin/env bash
# performing a 301 move permanently

sudo apt-get update
sudo apt-get install -y nginx

echo "Hello World!" | sudo tee /var/www/html/index.html

string_for_replacement = "server_name _:\n\trewrite ^\/redirect_me https:\/\/github.com\/besthor permanent;"

sudo sed -i "s/server_name _:/$string_for_replacement/" /etc/nginx/sites-enabled/default

sudo service nginx  restart

</code>


one can install shellcheck to check the script

sudo apt-get install shellcheck

then shellcheck 3-redirection

then chmod u+x 3-redirection

then git add && git commit -m and git push


task 4

integration of an error page, error 404

switch to the web server

then sudo vim error_page {any name can do}

string_for_replacement="listen 80 default_server:\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var/www/html;\n\tinternal;\n\t}"

sudo sed -i "s/listen 80 default_server:/@string_for_replacement/" /etc/nginx/sites-enabled/default

then sudo chmod +x error_page

then cd /etc/nginx/sites-enabled

you can an update of the default file incase anything goes wrong

then come back to the web-01 then run the ./error_page

test the script
 
sudo nginx -t

then cd var/www/html

then sudo vim 404.html

	this is not the page

then sudo nginx -t

then sudo service nginx restart

then logout


then i can go the web browser then put your <ip-address>/<any page of choice eg bsbd> then it should bring a 404 error page, retry again


then come back to the system dev-ops, in web-servers

then

cp -r 3-redirection 4-not_found_page_404

then add a new line before sudo service nginx restart

echo "This is not a page" | sudo tee /var/www/html/404.html
string_for_replace="listen 80 default_server:\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\troot \/var/www/html;\n\t\tinternal;\n\t}"

sudo sed -i "s/listen 80 default_server:/$string_for_replacement/" /etc/nginx/sites-enabled/default


then make it executable then git add . ...




task 5

the installation of puppet to automate our work to save on time

now the puppet manifest will be 


<code>

# automating my work using puppet

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path => '/etc/nginx/sites-enabled/default',
  after => 'listen 80 default_server:',
  line => 'rewrite ^/redirect_me https://www.github.com/stevovenom permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure => running,
  require => package['nginx'],
}


</code>

make it executable then git add git commit ...


The resources for this particular task can be accessed in:

1. <a href="https://intranet.alxswe.com/rltoken/6TI3HiyFdwrbXWKVF24Gxw">How_the_ WEB_works</a><br>
2. <a href="https://intranet.alxswe.com/rltoken/vkVMGlaf39j2DWAQWzo6EA">Nginx</a><br>
3. <a href="https://intranet.alxswe.com/rltoken/zKrpVxWuUHVdW4URAjdFbw">How to configure Nginx</a><br>
4. <a href="https://intranet.alxswe.com/rltoken/Ar18u5sRis1fkvkVgzdcqg">Child process concept page</a><br>
5. <a href="https://intranet.alxswe.com/rltoken/xi3peVqYl02PfpHHHlCtxQ">Root and subdomain</a>
6. <a href="https://intranet.alxswe.com/rltoken/sBrrP4EAmI3NoYjIgZrUhw">HTTP request</a>
7. <a href="https://intranet.alxswe.com/rltoken/Eaa4ZuKvye941hTkP8VlBQ">HTTP Redirections</a>
8. <a href="https://intranet.alxswe.com/rltoken/eJSp2QFTY6jqqNtz8OVDEw">NOT found HTTP response CODE</a>
9. <a href="https://intranet.alxswe.com/rltoken/7WMNY5CWD-CBrxmQrdmfPg">LOG FILES on Linux</a>
