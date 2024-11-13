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
        print(f"client socket -> {client_socket}")
        while True:
            msg = input(f"enter some message or exit to break: ")
            # msg = b'hello from client'

            if msg.lower() == 'exit':
                print("closing connection")
                break
            # converting byte to string (user input)
            converted_str = bytes(msg, 'utf-8')
            client_socket.sendall(converted_str)
            print(converted_str)
            print(f"sending message")

            # response = client_socket.recv(1024)
            # print(f"received message{response}")
            # print(response.decode())
    except ConnectionResetError as e:
        print(f"{e}")

    except ConnectionRefusedError:
        print(f"connection refused")


send_message_from_client()
