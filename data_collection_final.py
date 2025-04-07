import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import os
import traceback

# Initialize webcam
capture = cv2.VideoCapture(0)

# Initialize Hand Detectors
hd = HandDetector(maxHands=1)
hd2 = HandDetector(maxHands=1)

# Set dataset path
dataset_path = "I:\\Sign-Language-interpreter\\AtoZ_3.1\\"

# Ensure dataset folder exists
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# Initialize tracking variables
c_dir = 'A'  # Start with letter A
count = len(os.listdir(os.path.join(dataset_path, c_dir)))
offset = 15
step = 1
flag = False
suv = 0

# Create a white image for visualization
white = np.ones((400, 400), np.uint8) * 255
cv2.imwrite("I:\\Sign-Language-interpreter\\white.jpg", white)

while True:
    try:
        _, frame = capture.read()
        frame = cv2.flip(frame, 1)
        hands = hd.findHands(frame, draw=False, flipType=True)
        white = cv2.imread("I:\\Sign-Language-interpreter\\white.jpg")

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']

            # Ensure valid cropping boundaries
            y1, y2 = max(y - offset, 0), min(y + h + offset, frame.shape[0])
            x1, x2 = max(x - offset, 0), min(x + w + offset, frame.shape[1])
            image = np.array(frame[y1:y2, x1:x2])

            handz, imz = hd2.findHands(image, draw=True, flipType=True)
            if handz:
                hand = handz[0]
                pts = hand['lmList']

                # Center positioning
                os_x = ((400 - w) // 2) - 15
                os_y = ((400 - h) // 2) - 15

                # Draw hand skeleton
                for t in range(0, 4):
                    cv2.line(white, (pts[t][0] + os_x, pts[t][1] + os_y), (pts[t + 1][0] + os_x, pts[t + 1][1] + os_y), (0, 255, 0), 3)
                for t in range(5, 8):
                    cv2.line(white, (pts[t][0] + os_x, pts[t][1] + os_y), (pts[t + 1][0] + os_x, pts[t + 1][1] + os_y), (0, 255, 0), 3)
                for t in range(9, 12):
                    cv2.line(white, (pts[t][0] + os_x, pts[t][1] + os_y), (pts[t + 1][0] + os_x, pts[t + 1][1] + os_y), (0, 255, 0), 3)
                for t in range(13, 16):
                    cv2.line(white, (pts[t][0] + os_x, pts[t][1] + os_y), (pts[t + 1][0] + os_x, pts[t + 1][1] + os_y), (0, 255, 0), 3)
                for t in range(17, 20):
                    cv2.line(white, (pts[t][0] + os_x, pts[t][1] + os_y), (pts[t + 1][0] + os_x, pts[t + 1][1] + os_y), (0, 255, 0), 3)

                # Connect key landmarks
                cv2.line(white, (pts[5][0] + os_x, pts[5][1] + os_y), (pts[9][0] + os_x, pts[9][1] + os_y), (0, 255, 0), 3)
                cv2.line(white, (pts[9][0] + os_x, pts[9][1] + os_y), (pts[13][0] + os_x, pts[13][1] + os_y), (0, 255, 0), 3)
                cv2.line(white, (pts[13][0] + os_x, pts[13][1] + os_y), (pts[17][0] + os_x, pts[17][1] + os_y), (0, 255, 0), 3)
                cv2.line(white, (pts[0][0] + os_x, pts[0][1] + os_y), (pts[5][0] + os_x, pts[5][1] + os_y), (0, 255, 0), 3)
                cv2.line(white, (pts[0][0] + os_x, pts[0][1] + os_y), (pts[17][0] + os_x, pts[17][1] + os_y), (0, 255, 0), 3)

                # Draw circles on landmarks
                for i in range(21):
                    cv2.circle(white, (pts[i][0] + os_x, pts[i][1] + os_y), 2, (0, 0, 255), 1)

                # Display the processed hand skeleton
                cv2.imshow("Hand Skeleton", white)

        # Display the video feed with info
        frame = cv2.putText(frame, f"dir={c_dir}  count={count}", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow("Live Feed", frame)

        # Key press events
        interrupt = cv2.waitKey(1)

        # Exit on 'ESC' key
        if interrupt & 0xFF == 27:
            break

        # Move to next character folder
        if interrupt & 0xFF == ord('n'):
            c_dir = chr(ord(c_dir) + 1)
            if ord(c_dir) == ord('Z') + 1:
                c_dir = 'A'
            flag = False
            count = len(os.listdir(os.path.join(dataset_path, c_dir)))

        # Toggle data collection on 'a'
        if interrupt & 0xFF == ord('a'):
            flag = not flag
            suv = 0 if flag else suv

        print("=====", flag)

        # Save images when flag is True
        if flag:
            if suv == 180:
                flag = False
            if step % 3 == 0:
                save_path = os.path.join(dataset_path, c_dir, f"{count}.jpg")
                cv2.imwrite(save_path, white)
                count += 1
                suv += 1
            step += 1

    except Exception:
        print("== ERROR ==\n", traceback.format_exc())

# Release resources
capture.release()
cv2.destroyAllWindows()
