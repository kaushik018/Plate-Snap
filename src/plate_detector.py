import cv2
import os

# get the absolute path of the project root directory
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# use the absolute path to load the cascade classifier file
harcascade = os.path.join(base_path, "models/haarcascade_russian_plate_number.xml")

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) #height

min_area = 500
count = 0
img_roi = None

plate_cascade = cv2.CascadeClassifier(harcascade)
if plate_cascade.empty():
    print("Error loading cascade file")
    exit()

while True:
    success, img = cap.read()

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)


    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s') and img_roi is not None:
        output_path = os.path.join(base_path, "output/plates/scaned_img_" + str(count) + ".jpg")
        cv2.imwrite(output_path, img_roi)
        cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results",img)
        cv2.waitKey(500)
        count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()