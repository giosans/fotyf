# Use AWS keys
AWS KEYS
- User name	Password	Access key ID	Secret access key	Console login link					
- giosans		<YOURACCESSKEYID>	<YOURSECRETACCESSKEY>	<https://YOURURL.signin.aws.amazon.com/console>		

# Initialize EBS
(fotyf) giosans@ubuntu:~/website/prj$ eb init --interactive 

    Select a default region
    ...
    3) us-west-2 : US West (Oregon)
    4) eu-west-1 : EU (Ireland)
    5) eu-central-1 : EU (Frankfurt)
    6) ap-south-1 : Asia Pacific (Mumbai)
    ...
    (default is 3): 4

    Select an application to use
    1) fotyf
    2) [ Create new Application ]
    (default is 2): 1

    It appears you are using Python. Is this correct?
    (Y/n): Y

    Select a platform version.
    1) Python 3.6
    ...

    (default is 1): 1
    Cannot setup CodeCommit because there is no Source Control setup, continuing with initialization
    Do you want to set up SSH for your instances?
    (Y/n): n

# Check EBS
(fotyf) giosans@ubuntu:~/website/prj$ eb status # this should give the actual status of the application.
...

# Deploy on EC2. Move to AWS interface.
(fotyf) giosans@ubuntu:~/website/prj$ eb deploy
    Creating application version archive "app-181023_155615".
    Uploading: [##################################################] 100% Done...
    2018-10-23 13:56:19    INFO    Environment update is starting.      
    2018-10-23 13:56:23    INFO    Deploying new version to instance(s).
    2018-10-23 13:56:57    INFO    New application version was deployed to running EC2 instances.
    2018-10-23 13:56:57    INFO    Environment update completed successfully.
