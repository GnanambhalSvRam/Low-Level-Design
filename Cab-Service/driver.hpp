#pragma once
#include "common.hpp"

using namespace std;

class Driver {
    private:
        string name;
        RATING rating;
        bool availability;

    public:
        Driver(string dName, RATING dRating) : name(dName), rating(dRating) {}

        bool isAvailable() {
            return availability;
        }

        string getDriverName() {
            return name;
        }

        void setRating(RATING dRating) {
            rating = dRating;
        }

        RATING getDriverRating() {
            return rating;
        }

};
