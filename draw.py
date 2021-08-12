import cv2
cap=cv2.imread('ph1.jpg',cv2.IMREAD_COLOR)
cv2.rectangle(cap,(15,25),(200,300),(0,255,0),3)
cv2.line(cap,(200,250),(30,300),(0,0,0),3)
#cv2.line(cap,(15,25),(200,300),(255,255,0),5)
cv2.circle(cap,(430,310),45,(255,255,0),3)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(cap,'spyder!',(255,300),font,1,(234,0,9),2)
cv2.waitKey(0)
cv2.imshow('image',cap)
cv2.destroyAllwindows()
