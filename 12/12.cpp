#include <iostream>
#include <set>

#define N_DIVISORS 500

int main()
{
    long natural = 1;
    long triangular = 0;
    std::set<long> divisores;
    do
    {
        divisores = {};
        triangular += natural;
        auto aux = triangular;
        for (int i = 1; i <= aux; ++i)
        {
            if(aux % i == 0)
            {
                for(auto divisor : divisores)
                {
                    if(triangular % (i * divisor) == 0)
                    {
                        divisores.insert(i*divisor);
                    }
                }
                divisores.insert(i);
                aux = aux/i;
            }
        }
        natural++;
        if(natural % 1000 == 0)
        {
            std::cout << triangular << ": " << divisores.size() << std::endl;
        }
    }
    while (divisores.size() <= N_DIVISORS);
    std::cout << triangular << ": " << divisores.size() << std::endl;
}
