import socket

PORT = 8888

# Socket creation
# socket.AF_INET = IPv4 (AdressFamily)
# socket.SOCK_STREAM = TCP (SocketKind) 
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Add socket options
# SOL_SOCKET = Socket level option
# SO_REUSEADDR = reusable even if occupied
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associate the socket to an adress/port
# '' = 0.0.0.0 --> linked to every local interface
listen_socket.bind(('', PORT))

# Socket in passive mode
listen_socket.listen()

print(f'Serving HTTP on port {PORT} ...')

while True:
    # While listening, accept a connection by creating a new socket
    client_connection, client_address  = listen_socket.accept()
    # Receive messages from a socket in TCP connected mode
    request_data = client_connection.recv(1024)
    
    # Log the request
    print(request_data.decode('utf-8'))

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    # Send the entire buffer (call of send() until everything sent or error)
    client_connection.sendall(http_response)

    # Sockt closing
    client_connection.close()