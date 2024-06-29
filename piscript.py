import socket
import pickle
import cv2  # OpenCV for capturing and encoding images

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)  # Replace with your server IP and port

# Connect the socket to the server
client_socket.connect(server_address)

try:
    # Capture an image (example using OpenCV)
    cap = cv2.VideoCapture(0)  # Replace with your camera index or file path if reading from a file
    ret, frame = cap.read()

    # Convert the image to bytes
    encoded_img = cv2.imencode('.jpg', frame)[1].tobytes()

    # Send the image data to the server
    client_socket.sendall(encoded_img)

    # Receive the gesture response from the server
    gesture_response = client_socket.recv(1024)

    print(f"Received gesture: {gesture_response.decode()}")

finally:
    # Clean up the connection
    client_socket.close()
    cap.release()
