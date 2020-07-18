
import sys, os, PyQt5
from PyQt5 import QtWidgets, uic
import random

    #Генерация параметров
def Random_Gender(): #Случайный Пол  
    Spisok_Gender = open('Spisok/Gender.txt', 'r', encoding='utf-8')
    Gender = [line.strip() for line in Spisok_Gender]
    root.Gender.setText(str(random.choice(Gender)))

def Random_Animal(): #Случайное Животное  
    Spisok_Animal = open('Spisok/Animal.txt', 'r', encoding='utf-8')
    Animal = [line.strip() for line in Spisok_Animal]
    root.Animal.setText(str(random.choice(Animal)))

def Random_Pose(): #Случайная Поза 
    Spisok_Pose = open('Spisok/Pose.txt', 'r', encoding='utf-8')
    Pose = [line.strip() for line in Spisok_Pose]
    root.Pose.setText(str(random.choice(Pose)))

def Random_Emotion(): #Случайная Эмоция
    Spisok_Emotion = open('Spisok/Emotion.txt', 'r', encoding='utf-8')
    Emotion = [line.strip() for line in Spisok_Emotion]
    root.Emotion.setText(str(random.choice(Emotion)))

    #Добовление параметров в списки
def AddAnimal():
    AddText = str(root.AddText.text())
    my_file = open("Spisok/Animal.txt", 'a', encoding='utf-8')
    my_file.write('\n')
    my_file.write(AddText)
    my_file.close()
    print('Добавлено')

def AddPose():
    AddText = str(root.AddText.text())
    my_file = open("Spisok/Pose.txt", 'a', encoding='utf-8')
    my_file.write('\n')
    my_file.write(AddText)
    my_file.close()
    print('Добавлено') 

def AddEmotion():
    AddText = str(root.AddText.text())
    my_file = open("Spisok/Emotion.txt", 'a', encoding='utf-8')
    my_file.write('\n')
    my_file.write(AddText)
    my_file.close()
    print('Добавлено')


fn = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Program.ui")
app = QtWidgets.QApplication(sys.argv)  

root = uic.loadUi(fn)

root.AddAnimal.clicked.connect(AddAnimal)
root.AddEmotion.clicked.connect(AddEmotion)
root.AddPose.clicked.connect(AddPose)

root.Confirmation.clicked.connect(Random_Gender)
root.Confirmation.clicked.connect(Random_Animal)
root.Confirmation.clicked.connect(Random_Pose)
root.Confirmation.clicked.connect(Random_Emotion)

root.show()
sys.exit(app.exec_())