#include "riderManager.hpp"
using namespace std;

RiderManager* RiderManager::riderManagerInstance = nullptr;
mutex RiderManager::mtx; 

RiderManager* RiderManager::getRiderManager() {

    if (riderManagerInstance == nullptr) {
        mtx.lock();
        if (riderManagerInstance == nullptr) {
            riderManagerInstance = new RiderManager();
        }
        mtx.unlock();
    }

    return riderManagerInstance;
}

void RiderManager::addRider(string riderName, Rider* rider) {
    ridersMap[riderName] = rider;
}

Rider* RiderManager::getRider(string riderName) {
    return ridersMap[riderName];
}