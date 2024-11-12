# show message from client


import socket


def server_process3():

    try:
        server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # to specify a connection
        # print(f"{server_socket}")
    # except Exception as e:
    #     print(f"error occured: {e}")
        host = socket.gethostname()
        print(host)
        port = 9999
        # bidning the socket with ip address and port number
        server_socket.bind((host, port))
        print(f"server is ready")

        server_socket.listen()

        print(f"setting time out for 30 s")
        server_socket.settimeout(30)
        conn, addr = server_socket.accept()

        print(f"receiving message")

        msg = server_socket.recv(1024)
        print(msg.decode())

        # server_socket.sendall(msg)
        conn.close()
    except TimeoutError as e:
        print(f"{e} connection closed")


server_process3()
