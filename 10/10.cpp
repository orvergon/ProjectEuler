#include <iostream>
#include <cstring>

bool *numeros;
size_t tam = 2000000;
int last_prime = 0;

inline void sieve()
{
    while(!numeros[++last_prime]);

    auto primo = last_prime;
    for(int i = 2*primo; i < tam; i += primo)
    {
        numeros[i] = false;
    }
}

int main()
{
    numeros = new bool[tam];
    for(int i = 0; i < tam; i++)
    {
        numeros[i] = true;
    }
    numeros[0] = false;
    numeros[1] = false;
    last_prime = 1;
    while(last_prime <= tam) sieve();

    long soma = 0;
    for(int i = 0; i < tam; i++)
        if(numeros[i])
        {
            std::cout << i << std::endl;
            soma += i;
        }
    std::cout << soma << std::endl;
}
