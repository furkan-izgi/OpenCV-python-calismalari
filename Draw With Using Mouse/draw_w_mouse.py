import numpy as np
import cv2

def draw_circle(event, x, y, flags, param): #BGR not RGB
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0, 0, 255), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)
        
cv2.namedWindow(winname='Draw with mouse')
cv2.setMouseCallback('Draw with mouse', draw_circle)

img = np.zeros((512, 512, 3), dtype=np.int8)

while True:
    cv2.imshow("Draw with mouse", img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()