#in this code we are just sending the file and a hash code to ensure the authenticity of the file 
#the client reads a file , calculate its hash 
#send both the files to server 
#the server recieves the file and the client hash 
#the server calculate the file hash 
#and then server matches both the hash 
import socket
import hashlib
def calculate_hash(file_content):
    # Calculate the SHA-256 hash of the file content
    hash_object = hashlib.sha256()
    hash_object.update(file_content)
    return hash_object.hexdigest()#returns hexadecimal string
def main():
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#we have defined the socket object here
    client_socket.connect(("YOUR IPv4 ADDRESS",12345))#taking tuple as an arguement
    filename="example.txt"
    with open(filename,"rb") as file:# rb stands for reading, binary (non text)
        file_content=file.read()
    client_hash=calculate_hash(file_content)
    client_socket.sendall(file_content)
    client_socket.sendall(client_hash.encode('utf-8'))
    print(f"sent{filename} and its hash to the server")
if __name__=="__main__":
    main()