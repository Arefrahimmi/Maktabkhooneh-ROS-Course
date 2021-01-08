#!/usr/bin/env python
# talkernode for maktabkhooneh project


import rospy
from my_sensore.msg import depth


def talker():
    pub = rospy.Publisher('depth_topic', depth, queue_size=10)
    rospy.init_node('talker')
    rate = rospy.Rate(1)  # hz
    i=1
    while not rospy.is_shutdown():
        depth_msg=depth()
        depth_msg.id=i
        depth_msg.name="depth_sensor"
        depth_msg.x=52
        depth_msg.y=23
        rospy.loginfo("depth is:")
        rospy.loginfo(depth_msg)
        pub.publish(depth_msg)
        rate.sleep()
        i=i+1


if __name__ == '__main__':
    try:
        talker()
    except:
        pass
