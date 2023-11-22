import socket
import hashlib 
def calculate_hash(file_content):
    #we will be using the sha256 to calculate the hash here
    hash_object=hashlib.sha256()
    hash_object.update(file_content)
    return hash_object.hexdigest()#this returns the hash as an hexadecimal string representation
def main():
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #address family internet , it uses IPV4 to communicate
    #sock stream ->it is reliable , stream oriented connection 
    #mostly used to show TCP connection 
    server_socket.bind(("YOUR IPv4 IP ADDRESS",12345))#IP address and port number
    server_socket.listen(1)#allowing upto one connection
    #This is an IP address. In this case, it's the loopback address, which is a special address that represents the local machine (the server itself)
    #Ports are used to distinguish di   fferent services or processes running on the same machine
    print("server is listening for incoming connections....")
    while True:#this actually starts the infinite loop 
        client_socket,client_address=server_socket.accept()
        #the client_socket,client_address will not be the same as that of the server 
        #these simply represent the client socket and address after the server accepts an incomming connection
        print(f"accepted connection from {client_address}")
        with client_socket:
            '''When the with block is entered, it typically does two things:

                It calls the __enter__() method of the object referenced by client_socket. This method is used to set up the resource or perform any necessary setup before entering the block.

                It ensures that the __exit__() method of the object will be called when exiting the block. This method is used to perform any cleanup or resource release when the block is exited, even if an exception is raised during the execution of the block.
'''
            file_content=b""#it is used to read the b type content(b-binary)
            while True:
                data=client_socket.recv(1024)
                if not data:
                    break
                file_content+=data
            client_hash=client_socket.recv(64).decode('utf-8')#we are recieving the client hash here
            server_hash=calculate_hash(file_content)#calculating the server's hash
            if client_hash==server_hash:
                print("data integrity verified. The hash value matches")
            else:
                print("hash value dont match . breach in the authenticity")
if __name__=="__main__":
    main()
