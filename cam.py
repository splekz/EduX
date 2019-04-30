import cv2

def main():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)
    if vc.isOpened():
        rval,frame = vc.read()
    else:
        rval = False
    while rval:
        cv2.imshow("preview",frame)
        rval,frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: #press 'ESC' for exit
            cv2.destroyWindow("preview")
            break
    pass

if __name__ == '__main__':
    main()