#pragma once

#include <iostream>
using namespace std;
#include "tripMetaData.hpp"

//This is an interface
//The core functionality of a pricing strategy is to calculate the price.

class PricingStrategy {
public:
    virtual double calculatePrice(TripMetaData* metaData) = 0;

};