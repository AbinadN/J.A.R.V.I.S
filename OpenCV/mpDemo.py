import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=max_hands, min_detection_confidence=detection_confidence,
                                         min_tracking_confidence=tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, image, draw=True):
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(image, landmarks, self.mp_hands.HAND_CONNECTIONS)

        return image


def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()

    cv2.namedWindow("Hand Tracking", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Hand Tracking", 600, 450)  # Set your desired size here

    while True:
        success, img = cap.read()
        img = tracker.find_hands(img)

        cv2.imshow("Hand Tracking", img)

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
