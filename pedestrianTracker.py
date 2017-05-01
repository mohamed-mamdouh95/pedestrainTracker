import dlib
from darkflow.net.build import TFNet
import cv2
import time

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}
tfnet = TFNet(options)
it= 1
img = cv2.imread("./test/"+str(it)+".jpg")
result = tfnet.return_predict(img)
points = []
for i in range (0,len(result)):
    if result[i]['label'] == 'person' :
        points.append(( result[i]['topleft']['x'],result[i]['topleft']['y'],result[i]['bottomright']['x']
			,result[i]['bottomright']['y']))
print points
if not points:
    print "ERROR: No object to be tracked."
    exit()
tracker = [dlib.correlation_tracker() for _ in xrange(len(points))]
[tracker[i].start_track(img, dlib.rectangle(*rect)) for i, rect in enumerate(points)]

while it < 112:
   
    img = cv2.imread("./test/"+str(it)+".jpg")
    x = 1
    for i in xrange(len(tracker)):
            tracker[i].update(img)
            # Get the position of th object, draw a 
            # bounding box around it and display it.
            rect = tracker[i].get_position()
            pt1 = (int(rect.left()), int(rect.top()))
            pt2 = (int(rect.right()), int(rect.bottom()))
            cv2.rectangle(img, pt1, pt2, (255, 255, 255), 3)
            cv2.putText(img,str(x),pt1,cv2.FONT_HERSHEY_SIMPLEX, 2,(255,255,255),2)
            x = x+1 
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:
        break
    time.sleep(0.2)
    it = it +2
cv2.destroyAllWindows()


