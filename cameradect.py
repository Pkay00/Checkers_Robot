import cv2
import numpy as np
import time

# Define the camera
cap = cv2.VideoCapture(0)

# Set the width and height of the frame
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the color ranges for red and blue
lower_red = np.array([0, 70, 50])
upper_red = np.array([10, 255, 255])
lower_blue = np.array([80, 50, 50])
upper_blue = np.array([130, 255, 255])

# Define the dimensions of the chess board
rows = 8
cols = 8

# Define the cell size of the chess board
cell_size = 50

# Define the start time
start_time = time.time()

while True:
    # Get the current time
    current_time = time.time()
    
    # Check if 5 seconds have elapsed
    if current_time - start_time >= 7:
        # Reset the start time
        start_time = current_time
        
        # Read a frame from the camera
        ret, img = cap.read()
        
        # Convert the image to HSV color space
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Threshold the image to get only red and blue colors
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        
        # Apply the Hough circle transform to detect circles
        circles_red = cv2.HoughCircles(mask_red, cv2.HOUGH_GRADIENT, dp=2.5, minDist=40, param1=40, param2=40, minRadius=15, maxRadius=26)
        circles_blue = cv2.HoughCircles(mask_blue, cv2.HOUGH_GRADIENT, dp=2.5, minDist=40, param1=40, param2=40, minRadius=15, maxRadius=26)
        
        # Check if circles were found
        if circles_red is not None:
            # Draw the circles on the image
            circles_red = np.uint16(np.around(circles_red))
            for i in circles_red[0, :]:
                cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)

                # Determine the position of the circle on the chess board
                row = int(i[1] / cell_size)
                col = int(i[0] / cell_size)

                # Print the position of the circle on the chess board
                print(f'Red coin detected at position ({row}, {col})')

        if circles_blue is not None:
            # Draw the circles on the image
            circles_blue = np.uint16(np.around(circles_blue))
            for i in circles_blue[0, :]:
                cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)

                # Determine the position of the circle on the chess board
                row = int(i[1] / cell_size)
                col = int(i[0] / cell_size)

                # Print the position of the circle on the chess board
                print(f'Blue coin detected at position ({row}, {col})')

       # Draw the chess board grid on the image
for i in range(rows):
    for j in range(cols):
        x = j * cell_size
        y = i * cell_size
        if (i + j) % 2 == 0:
            cv2.rectangle(img, (x, y), (x + cell_size, y + cell_size), (255, 255, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + cell_size, y + cell_size), (0, 0, 0), -1)

# Display the resulting image
cv2.imshow("Chess Board", img)

# Wait for 5 seconds before capturing the next image
cv2.waitKey(5000)