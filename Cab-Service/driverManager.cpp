#include "driverManager.hpp"
#include <iostream>

DriverManager* DriverManager::driverManagerInstance = nullptr;
mutex DriverManager::mtx;

DriverManager* DriverManager::getDriverManagerInstance() {

    if (driverManagerInstance == nullptr){
        mtx.lock(); 
            if (driverManagerInstance == nullptr) {
                driverManagerInstance = new DriverManager();
            }
        mtx.unlock();
    }
    return driverManagerInstance;
}

void DriverManager::addDriver(string name, Driver* driver) {
    driversMap[name] = driver;
}

Driver* DriverManager::getDriver(string name) {
    return driversMap[name];
}

unordered_map<string,Driver*> DriverManager::getDriversList() {
    return driversMap;
}