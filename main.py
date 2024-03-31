import cv2

image = cv2.imread("man.jpg")

classNames = []
classFile = 'miscs\coco.names'
labels = []

with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'miscs\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'miscs\\frozen_inference_graph.pb'

Cimg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

classIds, confs, bbox = net.detect(Cimg, confThreshold=0.5)
print(classIds, confs, bbox)

if len(classIds) > 0:
    for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
        cv2.rectangle(image, box, color=(0, 255, 0), thickness=2)
        cv2.putText(image, classNames[classId-1], (box[0]+10, box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        labels.append(classNames[classId - 1])

cv2.imshow("Output", image)
