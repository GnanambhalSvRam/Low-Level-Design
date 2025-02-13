#include <iostream>
#include "rider.hpp"

using namespace std;

/*
What should a rider manager do? 
Store an unordered map of riders
Add new riders
Retrieve a specific rider
*/

class RiderManager {

    private:
        RiderManager(){}
        static RiderManager* riderManagerInstance;
        static mutex mtx;
        unordered_map<string, Rider*> ridersMap;

    public:
        static RiderManager* getRiderManager();
        void addRider(string riderName, Rider* rider);
        Rider* getRider(string riderName);
}