#importing necessary modules
import cv2
import pytesseract as ptr

ptr.pytesseract.tesseract_cmd = 'E:/Python_Files/tesseract/tesseract.exe'
#reading the image file
tst_img = cv2.imread('Test_img.jpg')

tst_img = cv2.cvtColor(tst_img, cv2.COLOR_BGR2RGB)

#print(ptr.image_to_string(tst_img))

#print(ptr.image_to_boxes(tst_img))
height_img, width_img,_ = tst_img.shape
data = ptr.image_to_data(tst_img)
# print(boxes)

for x, c in enumerate(data.splitlines()):
    #print(b)
    if x!= 0:
        c = c.split()
        #print(c)
        if len(c) == 12:
            x, y, w, h = int(c[6]), int(c[7]), int(c[8]), int(c[9])
            
            cv2.rectangle(tst_img, (x, y), (w + x, h + y), (0, 0, 255), 2)
            #cv2.rectangle(tst_img, (x, height_img - y), (w, height_img-h ), (255, 0, 255), 2)
            #cv2.putText(tst_img, b[0], (x, height_img - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
            cv2.putText(tst_img, c[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2) 


cv2.imshow('Result', tst_img)
cv2.waitKey(0)