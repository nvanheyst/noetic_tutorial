#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

i=0

def callback_count(msg):
    global i
    #rospy.loginfo("Message received. Total count is: ")
    i+=msg.data
    #rospy.loginfo(str(i))
    new_msg = Int64()
    new_msg.data = i
    pub.publish(new_msg)
      
    
    
if __name__ == '__main__':
    rospy.init_node('number_counter')
    
    sub = rospy.Subscriber("/number", Int64, callback_count)
    pub = rospy.Publisher("/number_count", Int64, queue_size=10)
    
    
    rospy.spin()
