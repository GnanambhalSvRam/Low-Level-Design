#include <iostream>
#include "pricingStrategy.hpp"

class DefaultPricingStrategy : public PricingStrategy {
    double calculatePrice(TripMetaData* metaData) {
        return 0.0;
    }
};