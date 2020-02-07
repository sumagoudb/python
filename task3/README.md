# Task2

## prerequisites
1. `apt install -y python python-pip python-git`

## output

```
~/PlayGround/python   master  curl http://localhost:8080 
Hey you are are suppose to use '/helloworld' or '/helloworld?FirstnameMiddlenameLastname'

~/PlayGround/python   master  curl http://localhost:8080/helloworld
Hello Stranger

 ~/PlayGround/python   master  curl http://localhost:8080/helloworld\?name=AlfredENeumann
Hello Alfred E

~/PlayGround/python   master  curl http://localhost:8080/helloworld\?name=SumaGoudB     
Hello Suma Goud

~/PlayGround/python   master  curl http://localhost:8080/helloworld\?name=JeffConSe
Hello Jeff Con

~/PlayGround/python   master  curl http://localhost:8080/versionz                  
{'hash': 'b4389e43468724b67737f29c7835c9431c87cf51', 'repo_name': 'python'}

```