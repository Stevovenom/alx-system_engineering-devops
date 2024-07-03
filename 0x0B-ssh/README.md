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
