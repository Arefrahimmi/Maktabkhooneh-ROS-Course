


#include"ros/ros.h"
#include "std_msgs/String.h"

void callback(const std_msgs::String&msg){
        ROS_INFO("I heard: [%s}\n", msg.data.c_str());
 }

int main(int argc,char **argv){
    ros::init(argc,argv,"litener");
    ros::NodeHandle nl;
    ros::Subscriber pub=nl.subscribe("chatter",1000,callback);
    ros::spin();
}