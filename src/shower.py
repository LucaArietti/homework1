#!/usr/bin/env python
# -*- coding: utf-8 -*-
## File "shower.py" che mostra a video la parte del messaggio selezionata. È "subscraibato"
## ad entrambi i nodi "keyreader" e "publisher" (ovvero ai topic keychat e cyberchat)


import rospy
from std_msgs.msg import String

filtro = 'a'
b = []

def parsa(s):
    global b
    b = []		#pulisce la lista
    b = s.split(".")	#splitta la stringa e mette nella lista man mano parsa

def k_callback(data):
    global filtro
    filtro = data.data	#il filtro è la lettera letta dal topic keychat. Finché non viene aggiornata, si mantiene quella vecchia

def c_callback(data):
    global filtro
    parsa(data.data)
    
    if filtro == 'a':
        rospy.loginfo(b[0] + ", " + b[1] + ", " + b[2])
    elif filtro == 'n':
        rospy.loginfo(b[0])
    elif filtro == 'e':
        rospy.loginfo(b[1])
    elif filtro == 'c':
        rospy.loginfo(b[2])


def listener():

    rospy.init_node('shower', anonymous=True)

    rospy.Subscriber('keychat', String, k_callback)
    rospy.Subscriber('cyberchat', String, c_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
