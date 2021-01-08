#!/usr/bin/env python

import rospy
import sys
from service.srv import service
def multiple_client(a,b):
    rospy.wait_for_service('multiple_service')
    try:
        multiple_tow_int=rospy.ServiceProxy('multiple_service',service)
        mul=multiple_tow_int(a,b)
        return (mul.sum)

    except rospy.ServiceException as e:
        print("fail")


if __name__=='__main__':
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    print("multiple %s*%s"%(a,b))
    s=multiple_client(a,b)
    print("%s*%s=%s" %(a,b,s))