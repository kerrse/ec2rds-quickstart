# ec2rds-quickstart
# TLDR :rabbit:
## EC2 Steps :ladder:
Launch instance :arrow_right: Set name to __ec2-instance__ :arrow_right: Set key pair name to __keypair__ :arrow_right: Allow SSH traffic/HTTPS traffic/HTTP traffic :arrow_right: Take note of *Instance ID* :arrow_right: Take note of __Public DNS__
## RDS Steps :ladder:
Create a database :arrow_right: Select __MariaDB__ :arrow_right: Set *DB instance identifier* to __sample__ :arrow_right: Set *Master username* to __admin__ :arrow_right: Create *Master password* :arrow_right: Connect to an EC2 compute resource using the *Instance ID* :arrow_right: Take note of __Endpoint__ 

# Full Length Tutorial
## EC2
<figure>
  <ol start="1"><li><figcaption>Click on <i>Launch instance</i></figcaption></li></ol>
  <img alt="Launch instance" src="steps/ec2-steps/step-1.png" width="40%" title="Click on Launch instance"/>
</figure>
<figure>
  <ol start="2"><li><figcaption>Under <i>Name</i>, type <b>ec2-instance</b></figcaption></li></ol>
  <img alt="Name the instance ec2-instance" src="steps/ec2-steps/step-2.png" width="60%" title="Type in ec2-instance"/>
</figure>
<figure>
  <ol start="3"><li><figcaption>Under the <i>Key pair (login)</i> section, click on <i>Create new key pair</i></figcaption></li></ol>
  <img alt="Create a new key pair" src="steps/ec2-steps/step-3a.png" width="60%" title="Select create a new key pair"/>
  <ol start="3"><li><figcaption>In the <i>Key pair name</i> field, type in <b>keypair</b> and then click on <i>Create key pair</i></figcaption></li></ol>
  <img alt="Type in keypair" src="steps/ec2-steps/step-3b.png" width="40%" title="Type in keypair"/>
</figure>
