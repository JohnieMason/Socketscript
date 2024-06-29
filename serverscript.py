import socket
import pickle
import cv2  # OpenCV for image processing
import numpy as np  # NumPy for array operations

# Function to process received image data
def process_image(image_data):
    # Decode the image data
    image_array = np.frombuffer(image_data, dtype=np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Perform image processing tasks (replace with your specific processing)
    # Example: Convert image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Example: Perform gesture recognition (replace with your actual logic)
    # This is a placeholder for gesture recognition, you should implement your model
    gesture = "unknown"
    # Example: Simulate gesture recognition based on image properties
    if np.mean(gray_img) > 100:
        gesture = "swipe_right"
    else:
        gesture = "swipe_left"

    return gesture

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)  # Replace with your server IP and port

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections (1 connection at a time)
server_socket.listen(1)

while True:
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()

    try:
        print(f"Connection from {client_address}")

        # Receive data from the client (assuming image data)
        data = b""
        while True:
            packet = connection.recv(4096)
            if not packet:
                break
            data += packet

        # Process received image data
        gesture = process_image(data)

        # Send the response back to the client (Raspberry Pi)
        connection.sendall(gesture.encode())

    finally:
        # Clean up the connection
        connection.close()
