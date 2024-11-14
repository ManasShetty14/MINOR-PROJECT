# sudo apt-get update
# sudo apt-get install python3-picamera


from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()

def capture_image(file_name="image.jpg"):
    camera.start_preview()
    sleep(2)  
    image_path = os.path.join("/home/pi/images", file_name)  
    camera.capture(image_path)  
    camera.stop_preview()
    return image_path

image_file = capture_image()
print(f"Image saved at: {image_file}")

#scp pi@<Raspberry Pi's IP adress>:~/test_image.jpg~/Downloads>(Codes to pull image on rasp pi to mac on terminal)
