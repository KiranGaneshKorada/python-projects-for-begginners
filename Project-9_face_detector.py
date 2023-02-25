import cv2

"""
 OpenCV uses machine learning algorithms to search for faces within a picture. Because faces are so complicated, there isn’t one simple test that will tell you if it found a face or not. Instead, there are thousands of small patterns and features that must be matched. The algorithms break the task of identifying the face into thousands of smaller, bite-sized tasks, each of which is easy to solve. These tasks are also called classifiers.

For something like a face, you might have 6,000 or more classifiers, all of which must match for a face to be detected (within error limits, of course). But therein lies the problem: for face detection, the algorithm starts at the top left of a picture and moves down across small blocks of data, looking at each block, constantly asking, “Is this a face? … Is this a face? … Is this a face?” Since there are 6,000 or more tests per block, you might have millions of calculations to do, which will grind your computer to a halt.

"""

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# this xml file contains data of open cv to detect objects i.e data of stages and tests to detect face

"""
OpenCV uses cascades. What’s a cascade or classifiers? The best answer can be found in the dictionary: “a waterfall or series of waterfalls.”

Like a series of waterfalls, the OpenCV cascade breaks the problem of detecting faces into multiple stages. For each block, it does a very rough and quick test. If that passes, it does a slightly more detailed test, and so on. The algorithm may have 30 to 50 of these stages or cascades, and it will only detect a face if all stages pass.
"""

img=cv2.imread("img.jpg")  #takes image from folder

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# converting color picture to gray shaded picture makes opencv to detect face or make tests easily

faces = face_cascade.detectMultiScale(gray,1.1,4)

# Detects objects where The function returns a list of rectangles in which it believes it found a face of different sizes in the input image. The detected objects are returned as a list of rectangles.

# gray=" specifies to return objects of gray color"
# 1.1=" scale factor " , 4="mineneighbours" explore more

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)

# This function returns 4 values: the x and y location of the rectangle, and the rectangle’s width and height (w , h).We use these values to draw a rectangle in image img using the built-in rectangle() function.


cv2.imshow("img", img)  # displays image draw by rectangle function above co-ordinates returned as objects by detectmultiscale function which used inputted image and xml-file(data to detect face)

cv2.waitKey() # displays and waits until we press any key

cv2.imwrite("face_detected.jpg",img) 
# replaces inputed pic with face_detected picture(border around face)


