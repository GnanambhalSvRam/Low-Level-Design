#include <iostream>
#include <mutex>

#include "strategyManager.hpp"

using namespace std;

StrategyManager* StrategyManager::strategyManagerInstance = nullptr;
mutex StrategyManager::mtx;

StrategyManager* StrategyManager::getStrategyManagerInstance() {
    if (strategyManagerInstance == nullptr) {
        mtx.lock();
        if (strategyManagerInstance == nullptr) {
            strategyManagerInstance = new StrategyManager();
        }
        mtx.unlock();
    }
    return strategyManagerInstance;
}

DriverMatchingStrategy* StrategyManager::determineDriverMatchingStrategy(TripMetaData* metaData) {
    cout<<"\nMatching you with the best driver based on your trip's metadata...";
    int choice = 1; //choose 1 or 2 for now

    switch(choice) {
        case 1: return new RatingBasedMatchingStrategy();
        case 2: return new NearestMatchingStrategy();
        default: return nullptr;
    }
}

PricingStrategy* StrategyManager::determinePricingStrategy(TripMetaData* metaData) {
    cout<<"\nCalculating price based on your trip's metadata...";
    int choice = 2; //choose 1 or 2 for now

    switch(choice) {
        case 1: return new RatingBasedPricingStrategy();
        case 2: return new DefaultPricingStrategy();
        default: return nullptr;
    }
}

int main() 
{
    cout<<"Successfully running without any errors!!!";
}