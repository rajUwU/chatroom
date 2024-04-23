import socket

# Server configuration
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345      # Port to listen on

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)  # Listen for only one connection

print(f"Server is listening on {HOST}:{PORT}")

# Accept incoming connection
client_socket, client_address = server_socket.accept()

print(f"Connected to {client_address}")

# Receive data from client
data = client_socket.recv(1024)
print(f"Received data from client: {data.decode()}")

# Close the connection
client_socket.close()
server_socket.close()