#pragma once
#include <iostream>
#include <unordered_map>
#include "driver.hpp"

using namespace std;

class DriverManager {
    private:
        DriverManager(){}
        static DriverManager* driverManagerInstance;
        static mutex mtx;
        unordered_map<string, Driver*> driversMap;

    public:
        static DriverManager* getDriverManagerInstance() {}
        void addDriver(string name, Driver* driver);
        Driver* getDriver(string name);
        unordered_map<string,Driver*> getDriversList();
};