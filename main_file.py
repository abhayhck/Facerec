import cv2
from simple_facerec import SimpleFacerec
import csv
from deepface import DeepFace
from statistics import mean
import os
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
clear = lambda: os.system('cls')

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

def start():
    # Load Camera
    cap = cv2.VideoCapture(0)
    l = []
    emotion=[]
    age=[]
    gender=[]
    face_names=[]
    n = 4  # accuracy
    while n:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)

        if len(face_names)==1:
            l.append(*(face_names))

            #print(predictions['dominant_emotion'])
            if face_names == ['Unknown'] :
                predictions = DeepFace.analyze(frame, actions=["emotion", "age", "gender"])
                emotion.append(predictions['dominant_emotion'])
                age.append(predictions['age'])
                gender.append(predictions['gender'])
            else:
                predictions = DeepFace.analyze(frame, actions=["emotion"])
                emotion.append(predictions['dominant_emotion'])
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        cv2.imshow("Frame", frame)
        if len(face_names)!=0:
            n = n-1
    return l,emotion,age,gender
def work(l, emotion, age, gender):
    #getting unique name
    z=set(l)
    m=0
    for i in z:
        if m<l.count(i):
            m=l.count(i)
            final_name=i


    #if the person is unknown

    if final_name=='Unknown':
        print("The person is identified as : Unknown ")
        avg = mean(age)
        print("The approximate age of the person is ", round(avg, 2))
        m=0
        genderset=set(gender)
        for i in genderset:
            if m < gender.count(i):
                m = gender.count(i)
                genderfinal = i
        print("Their gender is: ",genderfinal)
        lis=[]
        emoset = set(emotion)
        emoset = list(emoset)
        m = 0
        for j in emoset:
            if m < emotion.count(j):
                m = emotion.count(j)
                final_emotion = j
        print("Emotion of the person  : ", final_emotion)
        lis="Unknown Person,"+" Age : "+str(avg)+", Gender : "+genderfinal+", Emotion : "+final_emotion
        return lis




    with open('data.csv','r') as f:
        fread=csv.DictReader(f)
        emoset = set(emotion)
        emoset = list(emoset)
        m = 0
        for j in emoset:
            if m < emotion.count(j):
                m = emotion.count(j)
                final_emotion = j
        print("Emotion of the person  : ", final_emotion)
        for i in fread:
            if i['id']==final_name:

                if i[' designation']=='student':

                    print(f"\nPerson identified as : {i[' name']} ")
                    '''img = mpimg.imread(os.path.join('images/', final_name + '.jpg'))
                    imgplot = plt.imshow(img)
                    plt.show(block=False)
                    plt.pause(3)
                    plt.close()'''
                    print(f"\nThe Age is : {i[' age']}\nThe ID is : {i['id']}\nDesignation : {i[' designation']}\nEmail : {i[' email']}")
                    print(f"The identified person is studying in {i['semester']} semester, {i['year']} year in {i['Department']} department ")
                    i["Emotions"] = final_emotion
                    return i
                else:
                    print(f"\nPerson identified as : {i[' name']} ")
                    img = mpimg.imread(os.path.join('images/', final_name + '.jpg'))
                    imgplot = plt.imshow(img)
                    plt.show(block=False)
                    plt.pause(3)
                    plt.close()
                    print(f"\nThe Age is : {i[' age']}\nThe ID is : {i['id']}\nDesignation : {i[' designation']}\nEmail : {i[' email']}")
                    print(f"The identified person teaches in  {i['year']} year in {i['Department']} department ")
                    i["Emotions"] = final_emotion
                    return i
    del l

def main():
    try:
        while 1:
            l, emotion, age, gender = start()
            clear()
            d=work(l, emotion, age, gender)
            time.sleep(6)
            return d
    except ValueError:
        main()
#if __name__=='__main__':
    #main()

#cap.release()
cv2.destroyAllWindows()