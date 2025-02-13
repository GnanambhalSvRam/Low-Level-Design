#pragma once

#include <iostream>
#include "driver.hpp"
#include "tripMetaData.hpp"

class DriverMatchingStrategy {
public:
    virtual Driver* findDriver(TripMetaData* metaData) = 0;
};