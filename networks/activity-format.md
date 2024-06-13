# Routing Nodes

## Introduction

In this activity we're going to build our own little computer network. Recall that routers store some information about where to send packets of information in the internet. This is particularly useful if two network nodes need to talk to each other but aren't directly connected. In this activity we'll build a small network of interconnected **Nodes**, each node may be connected to multiple other nodes in the network, but won't necessarily be connected to every other node - or even the node that it wants to talk to. In order for each node to be able to communicate with each other node, these nodes will need a way to pass messages along from one node to the next. This is the essence of **Routing**.

## Overview

### Step 1: Node Setup

The first thing we'll do is start working on the `Node` class. Each instance in this class will represent a node in a computer network. Each node will have an address - we'll keep this simple for now and just give each node a capital letter name. Each node will also have a list of connected nodes, and a routing table. The routing table will store information about which connections lead to which node.

For this step, create a class called `Node` which initializes with three variables:
- address: a string representing the address / name of the node.
- connections: a list of nodes this node is connected to.
- routing table: a dictionary mapping node addresses to connections.

```py
class Node:
    def __init__(self, address):
        self.address = address
        # initialize connections
        # initialize routing_tables
```

#### Test Code

If you set up your class correctly you should be able to run the following test code and get the output below:


Test Code: 
```py
a = Node('A')
print(type(a.connections))
print(type(a.routing_tables))
```

Output:
```
<class 'list'>
<class 'dict'>
```

#### Solution

```py
class Node:
    def __init__(self, address):
        self.address = address
        self.connections = [] # list of connected nodes
        self.routing_table = {} # dictionary of address and connections
```

### Step 2: Connect

Step 2: Connecting nodes together. To make sure we connect nodes together properly, we'll create a new method for the `Node` class called `connect` that takes in another node for this node to connect to. This method will do two things:

- Add the new node to the connections list
- Add an entry to the routing table. This entry will use the address of the other node as the key, and the node itself as the value.

```py
def connect(self, node):
    # add node to connections
    # add entry to routing table
```

#### Test Code

To make sure we have the `connect` method all set up we can run the following test code:

```py
a = Node('A')
b = Node('B')

a.connect(b)
# print node a's connections
for connection in a.connections:
    print(type(connection))
    print(connection.address)
```

The test above should return:

```
<class '__main__.Node'>
B
```

To test the routing table setup you can run this code:

```py
for route in a.routing_table:
    print(route, a.routing_table[route])
```

This will print the key for each route, and the value associated with that key (which should be a node).

The output should look like this:

```
B <__main__.Node object at 0x104dd6d00>
```

#### Solution

```py
class Node:
    def __init__(self, address):
        self.address = address
        self.connections = [] # list of connected nodes
        self.routing_table = {} # dictionary of address and connections

    def connect(self, node):
        self.connections.append(node)
        self.routing_table[node.address] = node
```

### Step 3: Get Connection

When it comes time to send a message, the first thing our nodes need to do is to figure out which connection to send their message to. Before we write the send and receive logic, we'll create another method called `get_connection()`. This method will take in a `target` parameter and attempt to find a connection to that target. If it doesn't have a connection it will return `None`.

```py
def get_connection(self, target):
    # check if target (address of target node) is in the routing table
    # if target is in routing table, return the node from the routing table
    # if target is not in the routing table return None
```

#### Test Code

```py
a = Node('A')
b = Node('B')

a.connect(b)
print(a.get_connection('B'))
print(a.get_connection('C'))
```

The output of this test code should look something like this:

```
<__main__.Node object at 0x104acdbb0>
None
```

#### Solution

```py
def get_connection(self, target):
    if target in self.routing_table:
        return self.routing_table[target]
    else:
        return None
```

### Step 4: Send and Receive 

In this next step we'll create the `send()` and `receive()` methods. The `send()` method will allow a node to send a message to another node and the `receive()` method will allow nodes to receive incoming messages.

To make our lives easier let's also make sure to add some print statements to our methods.

The `send()` method will include print statements for if the sender managed to send the message and if the sender did not manage to send it.

The `receive()` method will include a print statement for when the receiver receives a message.

```py
def send(self, message, receiver):
    # get the connection to the receiver
    # if there is a connection send the message using the receive method
    # if there is not a connection do not send the message
    # print what happened

def receive(self, message, sender, receiver):
    # receive a message from sender
    # print what happened
```

#### Test code

```py
a = Node('A')
b = Node('B')

a.connect(b)
a.send('Hello, B!', 'B')
a.send('Hello, C?', 'C')
```

Output:

```
Sender A sent message "Hello, B!" to receiver B
B received "Hello, B! from A to B"
Cannot send message. No connection to C
```

#### Solution

```py
def send(self, message, receiver):
    connection = self.get_connection(receiver)
    if not connection: 
        print(f'Cannot send message. No connection to {receiver}')
        return
    print(f'Sender {self.address} sent message "{message}" to receiver {receiver}')
    connection.receive(message, self.address, receiver)

def receive(self, message, sender, receiver):
    print(f'{self.address} received "{message} from {sender} to {receiver}"')
    if (self.address != receiver):
        self.send(message, receiver)
```

### Step 5: Ping Routing

At this point we have two nodes which can talk to each other! But what if A is connected to B, and B is connected to C, and A wants to talk to C? A is going to need to be able to route its message through B to get to C. The essence of routing!

To do this we'll create a method called `ping()`. The `ping` method is going to allow one node to ask a connected node if it knows how to reach a third node. Since this can get a little bit messy, we'll provide the code for this below and walk through it together.

After we implement this, Node A will ping Node B. If Node B is the target then Node A will send its message to Node B. If Node B has the target in its routing table, Node B will tell Node A that it knows how to reach the target. 

Finally if Node B does not yet know how to reach the target, it will ping its connections (but not Node A) and see if any of them know how to reach the target node.

```py
def ping(self, sender, receiver):
        print(f'Node {self.address} received ping from node {sender} looking for node {receiver}')
        if (receiver == self.address):
            # The node we're searching for!
            return True
        if (receiver in self.routing_table):
            # The node already exists in this node's routing table
            return True
        else:
            for node in self.connections:
                if node.address != sender:
                    # Ask other nodes if they know how to reach the receiver
                    if node.ping(self.address, receiver):
                        self.routing_table[receiver] = node
                        return True 
        return False
```

### Step 6: Updating `get_connection()`

Now that we have the `ping()` method setup, we need to make a change to our `get_connection()` method which will cause it to `ping()` the connected nodes if knows how to reach the target:

Updated method:

```py
def get_connection(self, target):
    if target in self.routing_table:
        return self.routing_table[target]
    # Ping the connected nodes        
    for connection in self.connections:
        if (connection.ping(self.address, target)):
            self.routing_table[target] = connection
            return self.routing_table[target]
    return None
```

To test this out let's create a new node called `C` that is only connected to `B` and see if we can reach it from `A`:

#### Test Code

```py 
a = Node('A')
b = Node('B')
c = Node('C')

a.connect(b)
b.connect(c)
a.send('Hello, C?', 'C')
```

Output:

```
Node B received ping from node A looking for node C
Sender A sent message "Hello, C?" to receiver C
B received "Hello, C? from A to C
Sender B sent message "Hello, C?" to receiver C
C received "Hello, C? from B to C
```

In the output above we can see that a few things happened in order:

1. `A` pinged `B` looking for `C` and since `B` already knew where `C` was it returned `True`
2. `A` sent the message to `C` but the message was routed through `B`
3. `B` received the message and then sent it to `C`
4. Finally `C` received the message!

### Step 7: Establish Connection

In order to test our code we've been establishing one-way connections, but we want to make sure that each of these connections allows traffic to go back and forth between nodes. To make sure these connections are set up correctly we'll create a method outside of the `Node` class called `establish_connection` which will connect two nodes:

```py
def establish_connection(a, b):
    a.connect(b)
    b.connect(a)
```

#### Test Code 

```py
a = Node('A')
b = Node('B')
c = Node('C')

establish_connection(a, b)
establish_connection(b, c)

a.send('Hello, C?', 'C')
c.send('Hi from C', 'A')
```

The code above should establish a connection between `A` and `B`, and another one between `B` and `C`, and if everything goes according to plan we should see somehing like this in our ourput:

```
Node B received ping from node A looking for node C
Sender A sent message "Hello, C?" to receiver C
B received "Hello, C?" from A to C
Sender B sent message "Hello, C?" to receiver C
C received "Hello, C?" from B to C
Node B received ping from node C looking for node A
Sender C sent message "Hi from C" to receiver A
B received "Hi from C" from C to A
Sender B sent message "Hi from C" to receiver A
A received "Hi from C" from B to A
```

#### Full Solution

```py
class Node:
    def __init__(self, address):
        self.address = address
        self.connections = [] # list of connected nodes
        self.routing_table = {} # dictionary of address and connections

    def connect(self, node):
        self.connections.append(node)
        self.routing_table[node.address] = node

    def get_connection(self, target):
        if target in self.routing_table:
            return self.routing_table[target]
        # Ping the connected nodes        
        for connection in self.connections:
            if (connection.ping(self.address, target)):
                self.routing_table[target] = connection
                return self.routing_table[target]
        return None

    def send(self, message, receiver):
        connection = self.get_connection(receiver)
        if not connection: 
            print(f'Cannot send message. No connection to {receiver}')
            return
        print(f'Sender {self.address} sent message "{message}" to receiver {receiver}')
        connection.receive(message, self.address, receiver)
        

    def receive(self, message, sender, receiver):
        print(f'{self.address} received "{message}" from {sender} to {receiver}')
        if (self.address != receiver):
            self.send(message, receiver)

    def ping(self, sender, receiver):
        print(f'Node {self.address} received ping from node {sender} looking for node {receiver}')
        if (receiver == self.address):
            return True
        if (receiver in self.routing_table):
            return True
        else:
            for node in self.connections:
                if node.address != sender:
                    # Ask other nodes if they know how to reach the receiver
                    if node.ping(self.address, receiver):
                        self.routing_table[receiver] = node
                        return True 
        return False
    

def establish_connection(a, b):
    a.connect(b)
    b.connect(a)

        
a = Node('A')
b = Node('B')
c = Node('C')

a.connect(b)
b.connect(c)
a.send('Hello, C?', 'C')
```