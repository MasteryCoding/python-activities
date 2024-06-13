

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

establish_connection(a, b)
establish_connection(b, c)

a.send('Hello, C?', 'C')
c.send('Hi from C', 'A')