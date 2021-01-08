#!/usr/bin/env python

import rospy
from service.srv import service

def callandmultiple(multiple):
    rospy.loginfo("return [%s*%s]=%s" %(multiple.a,multiple.b,(multiple.a,multiple.b)))
    return (multiple.a*multiple.b)
def multiple_service():
    rospy.init_node('multiple_server_node')
    s=rospy.Service('multiple_service',service,callandmultiple)
    rospy.spin()

if __name__=='__main__':
    multiple_service()