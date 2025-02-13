#pragma once
#include "common.hpp"

using namespace std;

class Rider {

    private:
        string name;
        RATING rating;

    public:
        Rider(string rname, RATING rRating) : name(rname), rating(rRating) {}

        string getRiderName() {
            return name;
        }

        RATING getRiderRating() {
            return rating;
        }
};