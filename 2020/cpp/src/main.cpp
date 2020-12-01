#include "tools.hpp"

#include <iostream>

int main()
{
   auto lines = Tool::lines("../inputs/test.txt");
   for (const auto line : lines)
   {
      std::cout << line << std::endl;
   }

   return 0;
}
