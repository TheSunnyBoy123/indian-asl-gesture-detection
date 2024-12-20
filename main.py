import cv2
from datetime import date
from optparse import OptionParser
from time import strftime, localtime
from colorama import Fore, Back, Style

GREEN = (0, 255, 0)

scale_factor = 1.3
min_neighbors = 5
cascade_file = "haarcascade_frontalface_default.xml"

status_color = {
	'+': Fore.GREEN,
	'-': Fore.RED,
	'*': Fore.YELLOW,
	':': Fore.CYAN,
	' ': Fore.WHITE,
}

def get_time():
	return strftime("%H:%M:%S", localtime())
def display(status, data):
	print(f"{status_color[status]}[{status}] {Fore.BLUE}[{date.today()} {get_time()}] {status_color[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}")

def get_arguments(*args):
	parser = OptionParser()
	for arg in args:
		parser.add_option(arg[0], arg[1], dest=arg[2], help=arg[3])
	return parser.parse_args()[0]

def draw_faces(image, faces):
    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), GREEN, 2)
def detect_faces(image, face_classifier, scale_factor, min_neighbors, localize=True):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, scaleFactor=scale_factor, minNeighbors=min_neighbors)
    if localize:
        draw_faces(image, faces)
    return faces

if __name__ == "__main__":
    data = get_arguments(('-i', "--image", "image", "Path to the Image file (If not specified, will take frame from Camera Stream)"),
                         ('-c', "--cascade", "cascade", f"Path to cascade File (Default={cascade_file})"),
                         ('-s', "--scale-factor", "scale_factor", f"Scale Factor (Default={scale_factor})"),
                         ('-m', "--min-neighbors", "min_neighbors", f"Minimum Neighbors (Default={min_neighbors})"))
    if not data.cascade:
        data.cascade = cascade_file
    if not data.scale_factor:
        data.scale_factor = scale_factor
    else:
        data.scale_factor = int(data.scale_factor)
    if not data.min_neighbors:
        data.min_neighbors = min_neighbors
    else:
        data.min_neighbors = int(data.min_neighbors)
    face_classifier = cv2.CascadeClassifier(cascade_file)
    if data.image:
        try:
            image = cv2.imread(data.image)
        except:
            display('-', f"Failed to read the Image : {Back.MAGENTA}{data.image}{Back.RESET}")
        faces = detect_faces(image, face_classifier, data.scale_factor, data.min_neighbors, localize=True)
        print(f"\r{Fore.CYAN}{Back.MAGENTA}{len(faces)}{Back.RESET} {Fore.GREEN}Faces Detected{Fore.RESET}", end='')
        cv2.imshow("Image", image)
        cv2.waitKey()
    else:
        video_capture = cv2.VideoCapture(0)
        while cv2.waitKey(1) != 113:
            ret, frame = video_capture.read()
            if not ret:
                display('-', "Failed to get Frame from the Camera")
                break
            faces = detect_faces(frame, face_classifier, data.scale_factor, data.min_neighbors, localize=True)
            print(f"\r{Fore.CYAN}{Back.MAGENTA}{len(faces)}{Back.RESET} {Fore.GREEN}Faces Detected{Fore.RESET}", end='')
            cv2.imshow("Camera", frame)
        video_capture.release()
        cv2.destroyAllWindows()
    print()