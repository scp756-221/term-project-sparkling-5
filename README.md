[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7082888&assignment_repo_type=AssignmentRepo)
# CMPT 756 Term Project - For Sparkling 5
SFU CMPT 756 Term Project

1. Technology setup - Deploying in cloud environment
- AWS EKS is used in our project, with Kubernetes providing a high degree of portability across the clouds.
- AWS DynamoDB is used for backend database - checks on whether it is accessible/running.

Please ensure AWS DynamoDB is accessible/running
Regardless of where your cluster will run, it uses AWS DynamoDB for its backend database. Check that you have the necessary tables installed by running

$ aws dynamodb list-tables
The resulting output should include tables User and Music.

2. Working model
- Working in a team environment following the scrum methodology
- Using a distributed source control system for collaboration

3. Development of 3 public micro-services
    a. Music - extension
    b. Users - extension
    c. Playlist - create
4. Performance test: Run your application with various loads and measure/observe its behaviour.
5. Exploring how the system handles failures and approaches to remediate the error

## Commands for Reference

### To Start 

Clone the repo and copy your own `cluster/tpl-vars.txt` and `cluster/ghcr.io-token.txt` to the corresponding location. 

### Instantiate the templates

~~~
make -f k8s-tpl.mak templates
~~~

### Start the tools container

~~~
tools/shell.sh
~~~

### Start the EKS cluster

~~~
make -f eks.mak start
~~~

### Provision the cluster 
Create a namespace c756ns and set it as the default:

~~~
kubectl create ns c756ns
kubectl config set-context --current --namespace=c756ns
~~~

Deploy the services:

~~~
make -f k8s.mak provision
~~~

### Create load using gatling

~~~
tools/gatling.sh USERS SIM_NAME
~~~

For example, simulate 2 users to query music microservice

~~~
tools/gatling.sh 2 ReadMusicSim
~~~

### Grafana Url

~~~
make -f k8s.mak grafana-url
~~~

### Prometheus Url

~~~
make -f k8s.mak prometheus-url
~~~


### Kiali Url

~~~
make -f k8s.mak kiali-url
~~~
