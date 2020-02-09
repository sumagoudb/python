# python

## Task2

### prerequisites
1. `apt install -y python python-pip`
2. `pip install bs4`

### output

```
~/PlayGround/python   master  python task2/task2_console.py
B       Beatrice         Team Assistant  Bea rules the company’s daily executive machinery. Your chaos will not survive a neat and tidy Bea checklist. While you still collect things you maybe need to get done at some point
D       Daniel   DevOps Engineer         Daniel joined Endocode to get started in the IT industry and to support and contribute to the FOSS community. With a background in landscape planning
F       Felina   Team Assistant  Felina is our yoga loving Team Assistant. She takes care of the feel good management and HR. Preparing fancy team events are her specialty. In her free time
G       Giasemi  Software Engineer        Giasemi is a software engineer at Endocode. She loves developing algorithms
G       Gregor   DevOps Engineer         Gregor is the one cyclist in our team who will survive us all because he is clever enough to wear a helmet. To improve our survival chances
I       Ingrid   Open Source Compliance Software Engineer        Ingrid is a cat mother and a coffee lover. She is passionate about development and when she is not transforming coffee into algorithms
J       Johannes         DevOps Engineer         Johannes is polifacetic from dev-to-ops and back. He likes to write clean code and documentation. And when he leaves his computer after having produced pretty and clean things that leave chaos monkeys in awe
J       Jorge    DevOps Engineer         Jorge is an experienced engineer who will not be shaken by your latest crisis. He will keep a cool head
K       Katharina        Workshop \x26 Teacher Coordinator       Katha holds all the strings when it comes to coordinating Endocode\x27s workshops. She makes sure that every teacher
L       Lisa     CEO     Lisa is our CEO by day and a Star Wars-loving human rights activist by night. Her journey at Endocode moved from PR
M       Markus   Senior Software Developer       Markus is a Software Developer. Not just because that is his job title
M       Mirko    Director        Open Source Governance and Compliance
N       Nikolas  DevOps Engineer         Nikolas’ playground is the DevOps and automation world. He’s fantastic at finding and understanding the trouble at hand. And he is just as good in breaking it down and simplifying problems until they are solvable for everyone. And the ‘everyone’ is essential here. Because he believes that technology and knowledge should be shared and accessible for everyone. Then open source way.
S       Sebastian        CTO     Sebastian is one of the founders of Endocode and our CTO. He dislikes bios on websites
T       Thomas   Cloud Wizard    Thomas is not really here. He is speaking at a conference. Or at a meetup. Or is giving a workshop. And when he doesn’t spread the word about modernizing IT infrastructures
Y       Yotam    DevOps Engineer         Yotam’s nature is about as sunny as Berlin’s summer in 2018. If you stroll through our office and can’t find him at his desk
```

## Task3

### prerequisites
1. `apt install -y python python-pip python-git`

### building and running the container
1. docker build .
2. docker run --rm -v $PWD:/work -p 8080:8080 <container_id> --name my_container

### output

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

### logging

```
('Started httpserver on port ', 8080)
127.0.0.1 - - [07/Feb/2020 16:40:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [07/Feb/2020 16:40:45] "GET /helloworld HTTP/1.1" 200 -
127.0.0.1 - - [07/Feb/2020 16:41:17] "GET /helloworld/name=AlfredENeumann HTTP/1.1" 200 -
127.0.0.1 - - [07/Feb/2020 16:41:47] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [07/Feb/2020 16:41:54] "GET /helloworld HTTP/1.1" 200 -
127.0.0.1 - - [07/Feb/2020 16:42:11] "GET /helloworld?name=AlfredENeumann HTTP/1.1" 200 -
127.0.0.1 - - [07/Feb/2020 16:42:19] "GET /helloworld?name=SumaGoudB HTTP/1.1" 200 -
127.0.0.1 - - [07/Feb/2020 16:42:34] "GET /helloworld?name=JeffConSe HTTP/1.1" 200 -
127.0.0.1 - - [07/Feb/2020 16:45:37] "GET /versionz HTTP/1.1" 200 -
^C^C received, shutting down the web server

```