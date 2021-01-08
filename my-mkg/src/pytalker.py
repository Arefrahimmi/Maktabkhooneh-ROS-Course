#!/usr/bin/env python
# talkernode for maktabkhooneh project


import rospy
from std_msgs.msg import String


def talker():

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker')
    rate = rospy.Rate(1)  # hz

    while not rospy.is_shutdown():
        massage = "heloo,I am Aref Rahimi %s" % rospy.get_time()
        rospy.loginfo(massage)
        pub.publish(massage)
        rate.sleep()



if __name__ == '__main__':
    try:
        talker()
    except:
        pass
