<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Comments Pipeline with Airflow</title>
</head>
<body>

<h1>YouTube Comments Pipeline with Airflow</h1>
<p>This project demonstrates how to extract comments from a YouTube video using the YouTube API and Apache Airflow to automate the process.</p>

<h2>Architecture Diagram</h2>
<img src="screenshots2\workflowDiagram.png" alt="Architectural workflow diagram">

<h2>Steps for Setup and Execution</h2>

<h3>1. Acquire YouTube API Key</h3>
<p>To extract comments from a YouTube video, you need to acquire a YouTube API key. Follow this guide to get your API key:</p>
<ul>
    <li><a href="https://developers.google.com/youtube/v3/getting-started">YouTube API Guide</a></li>
</ul>
<p>After getting your API key, download the keys file:</p>
<img src="screenshots/image.png" alt="API key image">
<img src="screenshots/image-1.png" alt="Download API key image">

<h3>2. Connect to Airflow Instance via SSH</h3>
<p>If you're using Windows, change the permissions of the .pem key pair file you downloaded. For assistance, you can follow this YouTube video:</p>
<ul>
    <li><a href="https://www.youtube.com/watch?v=hDE3Io5CIbc&ab_channel=TapanDubey">Change PEM Permissions on Windows</a></li>
</ul>

<h3>3. Update Your Instance</h3>
<p>Update your instance to ensure the latest packages are installed:</p>
<pre><code>sudo apt update && sudo apt upgrade -y</code></pre>

<h3>4. Install Required Dependencies</h3>
<p>Airflow requires Python and some additional packages. Run the following command to install them:</p>
<pre><code>sudo apt install -y python3-pip python3-venv libpq-dev</code></pre>

<h3>5. Create a Virtual Environment</h3>
<p>To avoid interfering with the system Python environment, create a virtual environment for Airflow:</p>
<pre><code>python3 -m venv airflow-venv</code></pre>
<p>Activate the virtual environment:</p>
<pre><code>source airflow-venv/bin/activate</code></pre>

<h3>6. Install Apache Airflow</h3>
<p>Install Apache Airflow within the virtual environment:</p>
<pre><code>pip install apache-airflow</code></pre>

<h3>7. Verify Airflow Installation</h3>
<p>To ensure Airflow is installed correctly, run:</p>
<pre><code>airflow version</code></pre>

<h3>8. Install Required Libraries</h3>
<p>Next, install the necessary libraries as per the commands provided in the <code>yt_etl.ssh</code> file. You can refer to these images for the installation process:</p>
<img src="screenshots\image-1.png" alt="Library installation image 1">
<img src="screenshots\image-3.png" alt="Library installation image 2">

<h3>9. Install Libraries in the Virtual Environment</h3>
<p>For example, to install <code>pandas</code> and other dependencies, run:</p>
<pre><code>pip install pandas</code></pre>
<p>For reference, see the screenshots:</p>
<img src="screenshots\image-4.png" alt="Pandas installation image">

<h3>10. Start Airflow Server</h3>
<p>Run the command to start the Airflow webserver:</p>
<pre><code>airflow standalone</code></pre>

<h3>11. Airflow Not Running? Check Security Group</h3>
<p>If Airflow isn't running, you might need to update the security group of your instance. Go to:</p>
<ul>
    <li>Instance → Security → Edit Inbound Rules</li>
    <li>Add a rule with <strong>Type: All traffic</strong>, <strong>Protocol: Anywhere</strong>, or use <strong>MyIP</strong>.</li>
</ul>
<p>Allow all traffic and IPv4 anywhere.</p>
<img src="screenshots2/image-2.png" alt="Security group image">

<h3>12. Access Airflow Web UI</h3>
<p>Use the public IPv4 DNS to access the Airflow UI. The URL will look like this:</p>
<pre><code>ec2-51-20-131-224.eu-north-1.compute.amazonaws.com:8080</code></pre>
<p>Use <code>:8080</code> to access the Airflow UI.</p>

<h3>13. Create an Airflow Admin User</h3>
<p>If you can’t find the username and password in your Airflow logs, you can create a new user by running:</p>
<pre><code>flask fab create-admin --username areeb02 --firstname areebb --lastname ahmad --email admin11@example.com --password admin</code></pre>
<p>This will allow you to log into the Airflow UI.</p>
<img src="screenshots2/image-5.png" alt="Airflow login image">

<h3>14. Configure Airflow DAG Folder</h3>
<p>On your Airflow instance, go to the <code>/airflow</code> directory and open the <code>airflow.cfg</code> file:</p>
<pre><code>sudo nano airflow.cfg</code></pre>
<p>Change the <code>dags_folder</code> path to the <code>yt_comments_dag</code> (or the folder relevant to your project). It should look something like this:</p>
<img src="screenshots2/image-7.png" alt="DAG folder configuration image">

<h3>15. Copy Files to DAG Folder</h3>
<p>Use the following commands to copy your project files into the <code>yt_comments_dags</code> folder.</p>
<pre><code>sudo nano &lt;filename&gt;</code></pre>
<p>Refer to the screenshots for file details:</p>
<img src="screenshots2/image-8.png" alt="Copying files image 1">
<img src="screenshots2/image-9.png" alt="Copying files image 2">

<h3>16. Check Airflow UI</h3>
<p>Go to the Airflow UI and ensure that the folder name in <code>airflow.cfg</code> matches the DAG folder name. Your DAG should now appear.</p>

<h3>17. IAM Role Setup for S3 Bucket Access</h3>
<p>If your DAG fails because of a missing IAM role for S3 access, follow these steps:</p>
<ol>
    <li>Choose the instance you want to attach the IAM role to.</li>
    <li>Select <strong>Actions → Security → Modify IAM role</strong>.</li>
    <li>Select the IAM instance profile and click <strong>Update IAM role</strong>.</li>
    <li>Create an IAM role with <strong>Full S3 bucket permissions</strong>.</li>
</ol>
<img src="screenshots2/image-10.png" alt="IAM role image">

<h3>18. Refresh Airflow UI and Check Logs</h3>
<p>After refreshing the Airflow UI, the DAG should now appear, and you can check the logs for the execution details.</p>
<img src="screenshots2/image-11.png" alt="Airflow DAG logs image">

<h3>19. Verify CSV Upload to S3 Bucket</h3>
<p>Finally, ensure that the CSV file has been successfully uploaded to the specified S3 bucket.</p>
<img src="screenshots2/image-13.png" alt="S3 bucket CSV image">

</body>
</html>





Here is the architecture diagram for the project

![Architectural workflow diagram](screenshots2\workflowDiagram.png)

first you have to acquire youtube api key for extracting the commments from the youtube video that you want
here is the guide for getting the youtube api key
here is the guide for that
https://developers.google.com/youtube/v3/getting-started

![alt text](screenshots/image.png)
download the keys
![alt text](screenshots/image-1.png)

connect to airflow instance and connect to ssh client
if you are using windows first change the permissions of the .pem of key pair file that you have downloaded
i am leaving a yt video for the help https://www.youtube.com/watch?v=hDE3Io5CIbc&ab_channel=TapanDubey

Update Your Instance

sudo apt update && sudo apt upgrade -y 3. Install Required Dependencies
Airflow requires Python and some additional packages:

sudo apt install -y python3-pip python3-venv libpq-dev

4. Create a Virtual Environment
   To avoid interfering with the system Python environment, create an isolated virtual environment for Airflow:

python3 -m venv airflow-venv

Activate the virtual environment:

source airflow-venv/bin/activate 5. Install Apache Airflow
Install Airflow within the virtual environment:

pip install apache-airflow

6. Verify the Installation
   Ensure Airflow was installed correctly:

airflow version

then install the libraries from commands given in the yt_etl.ssh file
![alt text](screenshots\image-1.png)
![alt text](screenshots\image-3.png)

installing on python virtual environment
![alt text](<screenshots\installing s3fs.jpg>)
![alt text](screenshots\image-3.png)
pandas installing
![alt text](screenshots\image-4.png)

![airflow server running](screenshots2/image-1.png)

run command to runn airflow
airflow standalone

airflow not running? go into security groups in your instance
intace -> security -> edit inbound rules -> add rule with type all traffic with protocol anywhere or MyIP
![alt text](screenshots2/image-2.png)
allow all the traffic and ipv4 anywhere
![alt text](screenshots2/image-3.png)

now use this public ipv4 dns for running airfow instace
![alt text](screenshots2/image-4.png)
use link with endpoint :8080 with ipv4 public DNS
e.g ec2-51-20-131-224.eu-north-1.compute.amazonaws.com:8080

if you cant find the username and password in airflow logs on your cmd

create a new user using command
like mine:

flask fab create-admin --username areeb02 --firstname areebb --lastname ahmad -
-email admin11@example.com --password admin

![alt text](screenshots2/image-5.png)

you would be able to login the airflow
![alt text](screenshots2/image-6.png)

on your airflow ssh client go to /airflow
do sudo nano ariflow.cfg
and change the dags folder form dags to yt_comments dag or whatever suits your project
it will be someting like this
![alt text](screenshots2/image-7.png)

now copy the next 2 files using sudo nano commands in the yt_comments_dags folder
just like the commands shown below

![alt text](screenshots2/image-8.png)
![alt text](screenshots2/image-9.png)

now go to airflow UI
make sure the folder name in airflow directory for dags and the name of folder in path in airflow.cfg file is same.

now its possible that you your dag will give you error because you are trying to acceess the s3 bucket but you dont have iam role assigned to it you can do is

Choose the instance you want to attach the IAM role to
Select Actions, then Security, then Modify IAM role
Select the IAM instance profile
Select Update IAM role
and create iam role and give full s3 bucket permissions to it
![alt text](screenshots2/image-10.png)

now refresh your airflow UI
the dag appears dag appears like this
![alt text](screenshots2/image-11.png)

you cn check the logs for the print here in the logs tab
![alt text](screenshots2/image-12.png)

the csv has also been loaded to the specified s3 bucket
![alt text](screenshots2/image-13.png)



