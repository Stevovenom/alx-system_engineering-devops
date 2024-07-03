This task is mainly for SSH. it mainly focuses on rhe creation of a new server which will be used for the future projects.

#Task 0
It involves the creation of a bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.
The basic command is:

	ssh ubuntu -i ~/.ssh/school where -i specifies the identity to be used


#Task 1
For this particular task, the first work is mainly done in the root terminal where first one is too delete any .ssh file which is either existing so that it wont conflict intcase in the creation of a new public key.
I tried to run the command:
	ssh-keygen -t rsa -b 4096 -p <preferred password> -f ~/.ssh/school

but when i ran it in the root, the error i received was that too many arguments were passed and so simplified the command by using:
	ssh-keygen -t rsa -b 4096 -f ~/.ssh/school -N '<preferred password>'

By running this the RSA key pair having the private and the public keys were created.

#Task 2
The configuration files for this particular task are located in etc folder and hence use <strong>cd /etc</strong> and then cd into the ssh files where the configuration files are located. Then use the <strong>ssh_config</strong> by using <strong>sudo vim ssh_config</strong> to enable editing and complete the task.

#Task 3
get our public key, that is in cd /root/.ssh/school_pub and paste it in the profile to achieve task 3

after all this, go to the  "YOUR SERVERS" and click on it and then ask for a new server only after doing the 4 tasks, that is from 0 to 3

incase of permission denied

name a file web-01 and give it execution rights and try to execute it

!#/usr/bin/env bash
# server-01 login
eval $("ssh-agent")
ssh-add ~/.ssh/school

ssh ubuntu@<ip-address>

after this, you will be able to login in into the newly created web server adn using the cd .ssh
copy the public key in task 3 and paste it in the file named authorized keys


Also, one can use <strong>ssh -i ~/.ssh/school ubuntu@your_server_ip</strong> for easier access where the i[ address is ip address assigned when requesting for a new server.

#Task 4
Learn PUPPET!

Though made a chage to the puppet code, but this can asslo be used in place of the code'

<code>
# using puppet to make changes to our configuration file

file { 'etc/ssh/config':
  ensure  => present,
  content => "
  #ssh user configuration
  host*
  IdentifyFile ~/.ssh/school
  PasswordAuthentication no
  ",
}
</code>
