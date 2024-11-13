# show message from client


import socket


def server_process3():

    try:
        server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # to specify a connection
        host = socket.gethostname()
        print(host)
        port = 9999
        # bidning the socket with ip address and port number
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"server is ready-------------------")

        # print(f"setting time out for 30 s-------------")
        # server_socket.settimeout(30)
        conn, addr = server_socket.accept()
        print(f"conn: {conn} addr: {addr}")

        while True:
            msg = conn.recv(1024)
            if not msg:
                print("Client has disconnected.")
                break

            # if not msg:
            #     if_server_wants_to_close_the_conn = input("want to agree with client server decision: y/n")
            #     if if_server_wants_to_close_the_conn == 'y':
            #         break
            print(f"message decoded: {msg.decode()}")

            try:
                conn.sendall(msg)
                print("Echoed message back to client.")
            except Exception as e:
                print(f"{e}")
                break
        # conn.close()
    except TimeoutError as e:
        print(f"{e} connection closed")
    finally:
        conn.close()
        server_socket.close()
        print("Server socket closed.")


server_process3()
