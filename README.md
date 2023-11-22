# socket-programming
this is the github repository to explain the client server connection , explaining each line of code with proper and sufficient explanation
You wont need to go to second place to understand socket programming
this repo contains the example of the hash sending and verification
#the client reads a file , calculate its hash 
#send both the files to server 
#the server recieves the file and the client hash 
#the server calculate the file hash 
#and then server matches both the hash 
#we will be using the sha256 to calculate the hash here

address family internet , it uses IPV4 to communicate
#sock stream ->it is reliable , stream oriented connection 

#sock_stream refers to the tcp connection and af_net stands for type
#client_socket: This is a new socket object that is returned by the accept() method. This new socket is used exclusively for communication with the specific client that has just connected.
    #client_address: This is a tuple that contains information about the client that has connected. Typically, it includes the client's IP address and the port number on the client side that was used for the connection. It allows the server to identify which client is communicating with it.
#fernet = Fernet(key): In this line of code, a Fernet object named fernet is being created and initialized. The key variable is passed as an argument to the Fernet constructor. This key is used by the Fernet object for both encryption and decryption operations.
    #This line first encodes the message string into bytes using the encode() method, which converts the text into a binary representation according to a specific character encoding (usually UTF-8).
In the code server_socket.listen(1), the listen() method is used to make the server socket listen for incoming client connections. The argument 1 specifies the maximum number of queued connections that the server can handle at a time.
