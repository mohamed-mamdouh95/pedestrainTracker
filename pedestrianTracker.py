import dlib
from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}
tfnet = TFNet(options)
it= 1
img = cv2.imread("./test/"+str(it)+".jpg")
result = tfnet.return_predict(img)
points = []
points.append(( result[1]['topleft']['x'],result[1]['topleft']['y'],result[1]['bottomright']['x']
			,result[1]['bottomright']['y']))
print points
if not points:
    print "ERROR: No object to be tracked."
    exit()
tracker = dlib.correlation_tracker()
tracker.start_track(img, dlib.rectangle(*points[0]))

while it < 112:
   
    img = cv2.imread("./test/"+str(it)+".jpg")
    tracker.update(img)
    rect = tracker.get_position()
    pt1 = (int(rect.left()), int(rect.top()))
    pt2 = (int(rect.right()), int(rect.bottom()))
    cv2.rectangle(img, pt1, pt2, (255, 255, 255), 3)
    print "Object tracked at [{}, {}] \r".format(pt1, pt2),
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    print it
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:
        break
    it = it +2
cv2.destroyAllWindows()


