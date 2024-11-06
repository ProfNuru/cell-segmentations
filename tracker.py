import cv2

TrDict = {
    #"csrt": cv2.TrackerCSRT_create,
    #"kcf": cv2.TrackerKCF_create,
    #"boosting": cv2.TrackerBoosting_create,
    "mil": cv2.TrackerMIL_create,
    #"tld": cv2.TrackerTLD_create,
    #"medianflow": cv2.TrackerMedianFlow_create,
    #"mosse": cv2.TrackerMOSSE_create
}

tracker = TrDict["mil"]()

v = cv2.VideoCapture("movies/movie1.avi")
ret, frame = v.read()

cv2.imshow("Frame", frame)
roi = cv2.selectROI("Frame", frame)
#ok = tracker.init(frame, roi)

print(roi)
