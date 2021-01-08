/*talk_node
by Aref Rahimi
*/

#include "ros/ros.h"
#include "std_msgs/String.h"
#include "sstream"

int main(int argc,char **argv){
    ros::init(argc,argv,"talker");
    ros::NodeHandle n;
    ros::Publisher pub=n.advertise<std_msgs::String>("chatter",1000);
    ros::Rate rate(0.5);
    int  count=0;

    while(ros::ok()){

        std_msgs::String msg;
        std::stringstream ss;
        ss<<"Hi I am Aref rahimi"<<count;
        msg.data=ss.str();
        ROS_INFO("I heard: [%s}\n", msg.data.c_str());

        pub.publish(msg);
        rate.sleep();
        count++;
    }
    return 0;
}