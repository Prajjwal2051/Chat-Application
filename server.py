''' Implements a simple chat server where multiple clients can connect, send messages, and receive messages from 
others in real time using TCP sockets '''


# import required modules
import socket       # for making a low level netwroking interface
import threading    # handels ,multiple clinet operations at one time

# now i will provide the server host and port for the communication
HOST='127.0.0.1'    # this means our own local machine is used as a server for the communication
PORT=57815  # we can use any port for our use cases
LISTENER_LIMIT=5

# main fucntion
def main():
    '''
        we created a socket class object where AF_INET says we will use the IPv4 addresss and sock stream says
        we will use tcp packets for communication
    
    '''
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Server is running...")

    # now creating a try and catch block

    try:
        '''
        now we need to provide the address to the server in the form of hostip and which port it is going to use
        '''
        server.bind((HOST,PORT))
        print(f"server is running at host: {HOST} and port: {PORT}")
    except:
        print(f"Unable to bind with the host {HOST} and port {PORT}")

    '''
    now we will set the server limit this is necessary so that more load doesn't come to our 
    computer so we will set the limit how many clinet can connect to our server at a time 
    '''
    server.listen(LISTENER_LIMIT)

    ''' now we will create a while loop that will continously listen to clinet connections'''

    while True:
        client,address=server.accept()  # we created two varaibles that contain the clinet socket using and what is the address of it
        print(f"Sucessfully connected to client {address[0]} {address[1]}") 
        # here address is the tuple so address[0] will print the host and address[1] will print the port which is using



if __name__=="__main__":
    main()