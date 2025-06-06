# iomporting the required modules
import socket
import threading

HOST='127.0.0.1' # this is the like the target address where we need to connect so the target is our own computer
PORT=57815           # again the clinet can run to find a free port code or can use this particular port, its his/her choice
# notet he server port and client port should be same

def main():
    '''
        we created a socket class object where AF_INET says we will use the IPv4 addresss and sock stream says
        we will use tcp packets for communication
    
    '''
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # now connect to the server
    try:
        client.connect((HOST,PORT))
        print(f"Sucessfully connected to the server host: {HOST} and port: {PORT}")
    except:
        print(f"Unable to connect to server host: {HOST} and port: {PORT}")
    

if __name__=="__main__":
    main()