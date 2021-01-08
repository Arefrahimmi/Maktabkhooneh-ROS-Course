#talkernode for maktabkhooneh project


import rospy
from my_sensore.msg import depth

def callback(depth_msg):
    rospy.loginfo("depth is:(%d, %s,%2f, %2f)",depth_msg.id,depth_msg.name,depth_msg.x,depth_msg.y)

def listener():
    rospy.init_node('listener')
    rospy.Subscribe("depth_topic",depth,callback)
    rospy.spin()
    ros

if __name__=='__main__':
    try:
        listener()
    except:
        pass