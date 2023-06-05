#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cmath>
// 定义轨迹数据采样点的结构
struct Point
{
    int OID;
    int timestamp;
    double longitude;
    double latitude;
};

// 定义对象类定义轨迹数据类
class Object
{
public:
    int ID;
    std::vector<Point> trajectory;
    Object(int id) : ID(id) {}
};

 

// 密接模式挖掘函数

void mineCloseContacts(const std::vector<Object> &objects, int sourceID, double alpha, double beta)
{
    //密接模式挖掘函数????
    //
    //
    //
    const Object &source = objects[sourceID];
    std::vector<int> closeContacts;

    std::cout << "Close contacts for object " << sourceID << ":\n";
    for (int contact : closeContacts)
    {
        std::cout << contact << " ";
    }
    std::cout << std::endl;
}

// 主函数
int main()
{
    // 读取数据集文件

    std::ifstream inputFile("data.txt");
    if (!inputFile.is_open())
    {
        std::cerr << "Failed to open data file!" << std::endl;
        return 1;
    }
    std::vector<Object> objects;
    int numObjects = 0;
    objects[0].trajectory.push_back({0, 0, 0, 0});
    std::string line;
    while (std::getline(inputFile, line))
    {
        std::istringstream iss(line);
        std::string token;
        std::vector<std::string> tokens;

        while (std::getline(iss, token, ','))
        {
            tokens.push_back(token);
        }

        if (tokens.size() != 4)
        {
            std::cerr << "Invalid data format!" << std::endl;
            return 1;
        }
        int objectID = std::stoi(tokens[0]);
        int timestamp = std::stoi(tokens[1]);
        double longitude = std::stod(tokens[2]);
        double latitude = std::stod(tokens[3]);
        if (objectID > numObjects)
        {
            objects.emplace_back(objectID);
            numObjects = objectID;
        }
        objects[objectID].trajectory.push_back({objectID, timestamp, longitude, latitude});
        std::cout<<objects[objectID].ID<<endl;
    }
    inputFile.close();

    // 测试参数
    int sourceID1 = 121;
    int sourceID2 = 436;
    double alpha = 3;
    double beta = 400;

    // 挖掘与给定感染源之间存在密接关系的对象
    //mineCloseContacts(objects, sourceID1, alpha, beta);
    //mineCloseContacts(objects, sourceID2, alpha, beta);

    return 0;
}
