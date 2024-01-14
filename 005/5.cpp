#include <iostream>

int main()
{
    int n = 2520;
    bool divide;
    do
    {
        divide = true;
        for(int i = 1; i <= 20; i++)
        {
            if(n == 232792561)
                std::cout << n;
            if(n%i != 0)
                divide = false;
            if(n%10000 == 0)
            {}
        }
        n++;
    } while (!divide);
    n--;
    std::cout << n;
}