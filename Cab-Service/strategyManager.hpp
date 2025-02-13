#pragma once
#include <iostream>
using namespace std;
#include <mutex>

//Driver Matching Strategies
#include "nearestMatchingStrategy.cpp"
#include "ratingBasedMatchingStrategy.cpp"

//Pricing Strategies
#include "ratingBasedPricingStrategy.cpp"
#include "defaultPricingStrategy.cpp"

class StrategyManager {
    private:
        StrategyManager() {}
        static StrategyManager* strategyManagerInstance;
        static mutex mtx;
    
    public:
        static StrategyManager* getStrategyManagerInstance();
        DriverMatchingStrategy* determineDriverMatchingStrategy(TripMetaData* metaData);
        PricingStrategy* determinePricingStrategy(TripMetaData* metaData);

};