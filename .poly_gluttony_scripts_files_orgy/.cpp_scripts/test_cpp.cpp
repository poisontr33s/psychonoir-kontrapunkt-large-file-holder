#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> greetings = {"Hello", "from", "C++", "with", "MSYS2!"};
    for (const auto& word : greetings) {
        std::cout << word << " ";
    }
    std::cout << std::endl;
    return 0;
}
