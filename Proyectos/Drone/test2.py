from djitellopy import Tello
import cv2
import queue
import time
import threading
q = queue.Queue()

drone = Tello()
drone.connect()
drone.streamon()


def receive():
    print("start Receive")
    c = drone.get_frame_read()
    cap = cv2.imread(c)
    ret, frame = cap.read()
    q.put(frame)
    while ret:
        ret, frame = cap.read()
        q.put(frame)


def display():
    print("Start Displaying")
    while True:
        if not q.empty():
            frame = q.get()
            cv2.imshow("frame1", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    p1 = threading.Thread(target=receive)
    p2 = threading.Thread(target=display)
    p1.start()
    p2.start()
