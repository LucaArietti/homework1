#!/usr/bin/env python
# -*- coding: utf-8 -*-
## File "publisher.py" che pubblica 1 volta al secondo un messaggio
## contenente un nome, una età, e un corso di laurea. Pubblica nel topic 'cyberchat'


import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('cyberchat', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(1) # 1hz ovvero una volta al secondo
    while not rospy.is_shutdown():
        messaggio = "Luca Arietti.21.Informatica"
        rospy.loginfo(messaggio)
        pub.publish(messaggio)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
