#pragma once
#include <iostream>

using namespace std;

enum class RATING {
    UNASSIGNED,
    ONE_STAR,
    TWO_STARS,
    THREE_STARs,
    FOUR_STARS,
    FIVE_STARS
};

struct Location
{
    int x,y;
};
