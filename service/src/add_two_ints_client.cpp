#include "ros/ros.h"
#include "service/service.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "multiple_two_ints_client");
  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<service::service>("multiple_two_ints");
  service::service srv;
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);
  if (client.call(srv))
  {
    ROS_INFO("multiple: %ld", (long int)srv.response.sum);
  }
  else
  {
    ROS_ERROR("Failed ");
    return 1;
  }

  return 0;
}