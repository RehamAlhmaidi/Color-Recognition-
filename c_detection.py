import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert frame to HSV
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Get the pixel value at the center of the frame
    pixel_center = hsv_frame[cy, cx]
    h, s, v = pixel_center  # Hue, Saturation, and Value

    # Default color
    color = "UnKnown"

    # Detect white, black, and gray
    if v < 40:  
        color = "BLACK"  # Very low brightness = Black
    elif s < 30 and v > 200:  
        color = "WHITE"  # Low saturation + high brightness = White
    elif s < 30:
        color = "GRAY"  # Low saturation + medium brightness = Gray
    else:
        # Detect main colors using Hue
        if h < 7:
            color = "RED"
        elif h < 21:
            color = "ORANGE"
        elif h < 35:
            color = "YELLOW"
        elif h < 80:
            color = "GREEN"
        elif h < 129:
            color = "BLUE"
        elif h < 145:
            color = "PURPLE"
        elif h < 168:
            color = "PINK"
        else:
            color = "RED"

    # Get the BGR color of the center pixel
    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    # Draw a rectangle for the text background (Top Left Corner)
    cv2.rectangle(frame, (10, 10), (250, 80), (255, 255, 255), -1)  # White background
    cv2.putText(frame, color, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (b, g, r), 3)  # Display color name

    # Draw a small circle at the center of the frame
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:  # Exit on 'Esc' key
        break

cap.release()
cv2.destroyAllWindows()
