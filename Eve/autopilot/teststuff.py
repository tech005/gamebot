import cv2 as cv
import numpy

# test files used
samplescreen = "C:/Users/ryans/OneDrive/PROGRAMMING/gamebot/Eve/autopilot/sample.PNG"
gate = "C:/Users/ryans/OneDrive/PROGRAMMING/gamebot/Eve/autopilot/gate.PNG"

haystack_img = cv.imread(samplescreen, cv.IMREAD_UNCHANGED)
needle_img = cv.imread(gate, cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystack_img,needle_img, cv.TM_CCOEFF_NORMED)

# get best match
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('best match top left position: %s' % str(max_loc))
print('best match confidence: %s' % max_val)

threshold = 0.8
if max_val >= threshold:
    print("found needle")
    # dimentions of needle
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(haystack_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    cv.imshow('Result',haystack_img)
    cv.waitKey()
else:
    print("needle not found.")