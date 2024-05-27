import socket

# Server configuration
SERVER_HOST = 'IP'  # Public IP of the server
SERVER_PORT = 12345                # Port the server is listening on

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send data to the server
message = "Hello from client"
client_socket.send(message.encode())

# Close the connection
client_socket.close()