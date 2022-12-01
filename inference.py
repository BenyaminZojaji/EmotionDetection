import argparse
import cv2
from deepface import DeepFace

def main(args):
        info = DeepFace.analyze(img_path = args.img_path, actions = ['emotion'])
        img = cv2.imread(args.img_path)
        img = cv2.rectangle(img, (info['region']['x'], info['region']['y']), (info['region']['x'] + info['region']['w'], info['region']['y'] + info['region']['h']), (0, 0, 255), 4) # bbox
        img = cv2.putText(img, info['dominant_emotion'], (info['region']['x'], info['region']['y']), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255)) # text
        cv2.imwrite('output.png', img)


if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--img_path', type=str, help='image path')
        args = parser.parse_args()
        main(args)
