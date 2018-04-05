#!/usr/bin/env python
# -*- coding: utf-8 -*-
## File "keyreader.py" che legge da tastiera i comandi, e invia il comando al nodo shower tramite
## il topic 'keychat'

import signal
import sys
import rospy
from std_msgs.msg import String


def signal_term_handler(signal, frame):
    rospy.logerr("Utente ha lanciato interrupt da tastiera")
    sys.exit(1)

signal.signal(signal.SIGINT, signal_term_handler)

comandi = ('a','n','e','c')	#comandi disponibili

def talker():
    pub = rospy.Publisher('keychat', String, queue_size=10)
    rospy.init_node('keyreader', anonymous=True)
    messaggio = 'a'
    rospy.loginfo("Elenco comandi:\n\t'a' mostra tutto\n\t'n' mostra il nome\n\t'e' mostra l'età\n\t'c' mostra il corso di laurea\n")
    while not rospy.is_shutdown():
        c = str(raw_input(" > Inserisci comando: "))
        c = c.lower()
        if c not in comandi:
            rospy.loginfo("Comando non valido")	# ...e messaggio rimane con il vecchio c
        else:
            messaggio = c
        pub.publish(messaggio)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
