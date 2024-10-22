#include "rclcpp/rclcpp.hpp"
#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include "nav_msgs/msg/occupancy_grid.hpp"
#include "geometry_msgs/msg/point.hpp"
#include <vector>
#include <CGAL/Simple_cartesian.h>
#include <CGAL/convex_hull_2.h>


using namespace std::chrono_literals;
using namespace std::placeholders;

class OccupancyGridToPoseGraph : public rclcpp::Node
{
    public:
        OccupancyGridToPoseGraph()
        : Node("occupancy_grid_to_pose_graph_converter_node"), count_(0)
        {

            occupancy_grid_from_slam_subscriber = this->create_subscription<nav_msgs::msg::OccupancyGrid>("/map", 10, std::bind(&OccupancyGridToPoseGraph::obstacles_callback, this, std::placeholders::_1));
            

        }

    private:

        void obstacles_callback(const nav_msgs::msg::OccupancyGrid::SharedPtr msg) 
        {


            nav_msgs::msg::OccupancyGrid obstacles;
            
            obstacles.data = msg->data;
            obstacles.info = msg->info;
            obstacles.header = msg->header;
            

            for (size_t k = 0; k < obstacles.data.size(); k++) {
                if (obstacles.data[k] == 100) {
                    geometry_msgs::msg::Point point;
                    point.x = ((k%obstacles.info.width)*obstacles.info.resolution) + obstacles.info.origin.position.x;
                    point.y = ((k/obstacles.info.width)*obstacles.info.resolution) + obstacles.info.origin.position.y;
                    this->my_vector.push_back(point);
                    RCLCPP_INFO(this->get_logger(), "Point: x = %f, y = %f", point.x, point.y);
                }
            }

            
           

            // nav_msgs::msg::OccupancyGrid test_message;
            // test_message.header = msg->header;
            // test_message.info = msg->info;
            // test_message.data = msg->data;
            
            // int width = test_message.info.width;
            // int height = test_message.info.height;
            // int test_number_of_cells = width*height;
            // int array2D[width][height];
            // int count = 0;
            // for (size_t i = 0; i < width; i++) {
            //     for (size_t j = 0; j < height; j++) {
            //         array2D[i][j] = test_message.data.at(count);
            //         count++;
            //     }
            // }

            //  // Log the 2D array using RCLCPP_INFO
            // RCLCPP_INFO(this->get_logger(), "Occupancy Grid 2D Array:");
            // for (size_t i = 0; i < height; ++i)
            // {
            //     std::string row_str = "[";
            //     for (size_t j = 0; j < width; ++j)
            //     {
            //         row_str += std::to_string(array2D[i][j]);
            //         if (j < width - 1)
            //         {
            //             row_str += ", ";
            //         }
            //     }
            //     row_str += "]";
            //     RCLCPP_INFO(this->get_logger(), "Row %zu: %s", i, row_str.c_str());
            // }
            /*
            size_t length = test_message.data.size();
            int count = 0;
            int count2 = 0;
            int count3 = 0;
            int count4 = 0;
            for (size_t i = 0; i < length; ++i) {
                if (test_message.data.at(i) == 100) {
                    count++;
                } else if (test_message.data.at(i) == -1) {
                    count2++;
                } else if (test_message.data.at(i) == 0) {
                    count3++;
                } 
                
                count4++;
            }
            RCLCPP_INFO(this->get_logger(), "The Number of points with 100 is:  %d", count);
            RCLCPP_INFO(this->get_logger(), "The Number of points with -1 is:  %d", count2);
            RCLCPP_INFO(this->get_logger(), "The Number of points with 0 is:  %d", count3);
            RCLCPP_INFO(this->get_logger(), "The Number of total points is:  %d", count4);
            RCLCPP_INFO(this->get_logger(), "The Number of total points is:  %d", test_number_of_cells);
            */
            
        
        }   
        
        int count_;
        std::vector<geometry_msgs::msg::Point> my_vector;
        rclcpp::Subscription<nav_msgs::msg::OccupancyGrid>::SharedPtr occupancy_grid_from_slam_subscriber;




};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<OccupancyGridToPoseGraph>());
    rclcpp::shutdown();
    return 0;
}
