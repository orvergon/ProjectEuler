#include <iostream>
#include <cmath>
#include <vector>

std::vector<u_long> primes = {2};

u_long getNextPrime()
{
    u_long prime = primes.back();
    u_long next = primes.back();
    bool divisible = true;
    while(divisible != false)
    {
        next++;
        divisible = false;
        for(u_long i = 0; i < primes.size(); i ++)
        {
            if(next % primes[i] == 0)
            {
                divisible = true;
            }
        }
    }
    primes.push_back(next);
    return prime;
}

int main()
{
    for(int x = 0; x < 10002; x++)
    {
        std::cout << x+1 << ": " << getNextPrime() << std::endl;
    }
}

