from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}

tfnet = TFNet(options)
it = 1
while(it < 25) :
	imgcv = cv2.imread("./test/"+str(it)+".jpg")
	it = it +2
	imgcv=cv2.resize(imgcv,(800,600))
	out = imgcv.copy()
	result = tfnet.return_predict(imgcv)
	for i in range (0,len(result)):
		if result[i]['label'] == 'person':
			cv2.rectangle(out, (result[i]['topleft']['x'],result[i]['topleft']['y']) ,(result[i]['bottomright']['x']
						,result[i]['bottomright']['y']),(0,0,255))
	print(it)
	cv2.imshow("detected persons",out)
	cv2.waitKey(0);
cv2.destroyAllWindows()
