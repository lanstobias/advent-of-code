#include <iostream>
#include <vector>
#include <fstream>

namespace Tool {

std::vector<int> lines(const std::string filename)
{
   std::vector<int> data;
   std::ifstream input{filename};

   int value;
   while (input >> value)
   {
      data.push_back(value);
   }
   input.close();

   return data;
}

} // namespace Parser
