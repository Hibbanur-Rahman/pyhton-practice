import cv2
# video_cap= cv2.VideoCapture(0)
# while True:
#     ret,video_data=video_cap.read()
#     cv2.imshow("video_live",video_data)
#     if cv2.waitKey(10)==ord("a"):
#         break
# video_cap.release()
import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime
from google.colab.patches import cv2_imshow


video_capture=cv2.VideoCapture(0)

jobs_image=face_recognition.load_image_file("Steve_Jobs_Headshot_2010-CROP_(cropped_2).jpg")
jobs_encoding=face_recognition.face_encodings(jobs_image)[0]
ratan_tata_image=face_recognition.load_image_file("Ratan_Tata_photo.jpg")
ratan_tata_encoding=face_recognition.face_encodings(ratan_tata_image)[0]
hibban_image=face_recognition.load_image_file("/content/hibban_photo .jpeg")
hibban_encoding=face_recognition.face_encodings(hibban_image)[0]

known_faces_encoding=[
    jobs_encoding,
    ratan_tata_encoding,
    hibban_encoding,
]

known_faces_names=[
    "jobs",
    "ratan tata",
    "hibban"
]

from face_recognition.api import face_encodings
students=known_faces_names.copy()

face_locations=[]
face_encodings=[]
faces_names=[]
s=True

now=datetime.now()
current_date=now.strftime("%Y-%m-%d")

f=open(current_date+'.csv','w+',newline='')
lnwriter=csv.writer(f)

while True:
  _,frame=video_capture.read()
  small_frame=cv2.resize(frame, (0,0),fx=0.25,fy=0.25)
  rgb_small_frame=small_frame[:,:,::-1]
  if s:
    face_locations=face_recognition.face_locations(rgb_small_frame)
    face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
    face_names=[]
    for face_encoding in face_encodings:
      matches=face_recognition.compare_faces(known_faces_encoding,face_encoding)
      name=""
      face_distance=face_recognition.face_distance(known_faces_encoding,face_encoding)
      best_match_index=np.argmin(face_distance)
      if matches[best_match_index]:
        name=known_faces_names[best_match_index]

      face_names.append(name)
      if name in known_faces_names:
        if name in students:
          students.remove(name)
          print(students)
          current_time=now.strftime("%H-%M-%S")
          lnwriter.writerow([name,current_time])
  cv2.imshow("attendence system",frame)
  if cv2.waitkey(1) & 0xFF==ord('q'):
    break
video_capture.release()
cv2.destroyAllWindows()
f.close()
