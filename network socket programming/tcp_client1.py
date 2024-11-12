# tcp client code to sent a connection request to server and receive a hi....add()


import socket


def client_process():

    try:
        client_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # to specify a connection
        host = socket.gethostname()
        port = 9999

        print(f"client socket: {client_socket}")

        client_socket.connect((host, port))
        print(
            f"----------------------client is connected with the server-------------------")
        print(f"peer name: {client_socket.getpeername()}")
        print(f"socket   : {client_socket.getpeername}")

        response = client_socket.recv(1024)
        print(response.decode())
    except ConnectionRefusedError as e:
        # print(f"{e}")
        print(f"server process is not running")


if __name__ == '__main__':
    client_process()
