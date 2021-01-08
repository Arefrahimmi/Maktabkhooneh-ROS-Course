#include "ros/ros.h"
#include "service/service.h"

bool multiple(service::service::Request  &req,
         service::service::Response &res)
{
  res.sum = req.a * req.b;
  ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
  ROS_INFO("sending back response: [%ld]", (long int)res.sum);
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "multiple_two_ints_server");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("multiple_two_ints", multiple);
  ROS_INFO("Ready to multiple two ints.");
  ros::spin();

  return 0;
}
