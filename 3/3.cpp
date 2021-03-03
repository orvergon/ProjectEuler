#include <iostream>
#include <cmath>
#include <vector>

std::vector<u_long> primes = {2};

u_long getNextPrime()
{
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
    return next;
}

int main()
{
    u_long num = 600851475143;
    u_long primo = primes.back();
    while(num > 1)
    {
        primo = getNextPrime();
        if(num % primo == 0)
            num = num / primo;
    }
    std::cout << primo;
}

