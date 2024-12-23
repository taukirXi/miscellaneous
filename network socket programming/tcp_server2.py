# tcp server 1

# THIS IS  a connection oriented sserver which accepts single connection at a time and resoponds with hi message

import socket


def server_process():

    try:

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 9999                 # 0-102 are well known ports
        # 1024 - 49151 are reserved for user server application
        # 49152 - 65535 are reserved for clients

        print(f"server socket information: {server_socket}")

        server_socket.bind((host, port))
        print("server is ready....")

        print(f"setting time out for 60 s")
        server_socket.settimeout(5)

        server_socket.listen()
        print(f"listening to the socket for the connection......")

        conn, addr = server_socket.accept()
        print(f"connected with address {addr}")
        msg = b"hi...."
        conn.sendall(msg)
        conn.close()
    except TimeoutError as e:
        print(f"connection closed. {e}")


if __name__ == '__main__':
    server_process()
