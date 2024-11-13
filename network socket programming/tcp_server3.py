import socket


def server_process3():
    try:
        # Set up server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 9999

        # Bind and start listening for connections
        server_socket.bind((host, port))
        server_socket.listen()
        print("Server is ready and listening on port", port)

        while True:
            # Accept a new client connection
            conn, addr = server_socket.accept()
            print(f"Connected to client at {addr}")

            try:
                # Handle messages from this client
                while True:
                    msg = conn.recv(1024)
                    if not msg:
                        print("Client has disconnected.")
                        break

                    # Print and send the received message back to the client

                    # server can also reply the text
                    print("Received message:", msg.decode())
                    msg = input("write your reply: ")
                    msg = bytes(msg, 'utf-8')

                    conn.sendall(msg)
                    print("Echoed message back to client.")
            except Exception as e:
                print("An error occurred while handling client messages:", e)
            finally:
                # Close the connection with the current client
                conn.close()
                print("Closed connection with client.")

    except Exception as e:
        print("An error occurred with the server:", e)
    finally:
        # Close the server socket when done
        server_socket.close()
        print("Server socket closed.")


server_process3()
