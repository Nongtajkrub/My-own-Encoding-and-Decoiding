#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <fstream>
#include "json.hpp"

using json = nlohmann::json;

std::string getText();
std::string encode(std::string text);
json readJson(const std::string& filename);
std::string decode(std::string text);
void mainMenu();

json json_data = readJson("encodeanddecodedata.json");

//main
int main()
{

    mainMenu();

    return 0;

}

//encoding
std::string encode(std::string text)
{

    std::string result;

    for (char c : text) {
        result += json_data["encode"][std::string(1, c)];
    }

    return result;

}

//decoding
std::string decode(std::string encode_text)
{

    std::string result;
    std::string temp_string;

    for (int i = 1; i < encode_text.length() + 1; i++) {
        temp_string += encode_text[i - 1];  
        if (i % 3 == 0) {
            result += json_data["decode"][temp_string];
            temp_string = "";
        }
        
    } 

    return result;

}

//load json
json readJson(const std::string& filename)
{

    std::ifstream file(filename);

    if (!file.is_open()) {
        std::cerr << "File fail to open!\n";
        return json();
    }

    json jsonData;
    file >> jsonData;
    file.close();

    return jsonData;

}

//main menu
void mainMenu()
{
    while (true) {
        std::string text;
        int choice;

        std::cout << "Enter text: ";
        std::getline(std::cin, text);

        std::cout << "1 for Encoding\n2 for Decoding\n";
        std::cout << "Pick: ";
        std::cin >> choice;

        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        switch(choice) {
            case 1:
                std::cout << "Result: " << encode(text) << "\n";
                break;
            case 2:
                std::cout << "Result: " << decode(text) << "\n";
                break;
            default:
                std::cout << "Enter a valid choice\n";
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                break;
        }        

    }

}