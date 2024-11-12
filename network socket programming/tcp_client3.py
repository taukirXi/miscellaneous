# write a tcp client to send message to server and receive the same message
# from the server


import socket


def send_message_from_client():
    try:
        client_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # to specify a connection
        host = socket.gethostname()
        port = 9999

        client_socket.connect((host, port))

        # msg = input(f"enter some message: ")
        msg = b'hello from client'

        print(f"sending message")
        client_socket.sendall(msg)

        # print(f"reciving message")
        # response = client_socket.recv(1024)
        # print(response.decode())

    except ConnectionRefusedError:
        print(f"connection refused")


send_message_from_client()
