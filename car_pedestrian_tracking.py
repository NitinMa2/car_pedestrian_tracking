import cv2

# the video
video = cv2.VideoCapture('test_video.mp4')

# pre-trained classifiers
car_classifier_file = 'cars.xml'
person_classifier_file = 'haarcascade_fullbody.xml'

# create classifiers
car_detector = cv2.CascadeClassifier(car_classifier_file)
person_detector = cv2.CascadeClassifier(person_classifier_file)

# tracking
while True:
    # read a video frame
    read_success, frame = video.read()

    if read_success:
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # detect cars & people at any scale
    cars = car_detector.detectMultiScale(grayscale)
    people = person_detector.detectMultiScale(grayscale)

    # draw squares around the identified objects
    for (x,y,w,h) in cars:
        # blue sqaure
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    for (x,y,w,h) in people:
        # red square
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    # display the image with the squares
    cv2.imshow('Car & Pedestrian Detector', frame)

    # wait for 1 ms
    key = cv2.waitKey(1)

    # if q or esc is pressed
    if key in [27,113]:
        break

# release the VideoCapture object
video.release()
