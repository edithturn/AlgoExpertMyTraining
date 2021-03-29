# Basic Commands System Design

## Client Server Model

<p align="center">
  <img width="460" height="460" src="img/client-server_model.png">
</p>


### Utilities
netcat  or nc, is command used to any operation in Linux to TCP, UDP, or UNIX domains sockets.

```console
edith@edithcp:~$ netcat -l 8081
edith@edithcp:~$ nc -l 8081

```
```bash
nc 127.0.0.1 8081
# nc   =>  netcat
# -l   => listen
# 8081 => port

```

## Network Protocols
IP [Internete Protocol], TCP [Transmition Control Protocol], HTTP [Hypertext Transfer Protocol ]


what are the two sections of the IP packages?
* Header : keeps the information in bites about source Ip address, destination IP address, total size of the package, and version of the internet protocol of the Internet Protocol.
* Data: 

Request: 
GET: Retrieve data from the server
POST: Provided date from the server
DELETE: Asking the server to delete some data

```console
edith@edithcp:~$ curl localhost:3000/hello
```

## Storage

* Write
* Read
* Disk
* Persistence
* Memory

If we write data in Disk It is going to be there 
If we save data in Memory and if our server crash we won{t save the data.

Why use memory instead of disk?

read/write data from memory is much faster than writing/read data from disk

## Latency and Throughput


### Latency
How long takes data to traverse a System

- hight latency : take more time
- Low latency : take less time


### Throughput
How many of requests can the server handle in a specific time.



## Availability
How resistant a system is to a failures. 

SLA (Service level agreement): agreament between server provider and the customers.
SLO: Server Level Objective, The garantee to provide a service.


* Single points of failure: it this fails all the system fail

* Redundancy: It is duplicated, triplicated a specific part of our system. 


## Caching

It is use to rspeed up the system and improve the **latency** of the system

### Write through cache:
Where when we write a pice of data, our system will write in the cache and in the data base at the same time.

### Write back cache:
Our server will update the cache and will back to the client, our system will asynchronously update the database with the values of the cache.


