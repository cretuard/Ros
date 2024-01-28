#!/usr/bib/env pyhton3
import rospy
if __name__== "__main__":
     rospy.init_node("test_node")

     rospy.loginfo("Hello from test node.")
     rospy.logwarn("this is a warning")
     rospy.logerr("this is an error")
     
     rospy.sleep(1.0)

     rospy.loginfo("End of program")
     