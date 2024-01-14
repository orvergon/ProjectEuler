#include <iostream>
#include <unordered_map>
#include <vector>
#include <map>
#include <algorithm>

#define MAX 1000000
#define Collatz(x) (x%2 == 0) ? (x/2) : ((3*x) + 1)

template <class T, class X>
bool SetContains(std::unordered_map<T, X>& set, T value)
{
    return set.count(value) != 0;
}

struct Chain
{
    long number;
    long size;
};

int main()
{
    Chain biggest = {0, 0};
    std::unordered_map<long, long> chain_lengths = {{2, 2}};
    std::vector<long> breadcrumbs;
    for (int i = MAX; i >= 2; --i)
    {
        breadcrumbs = {};
        long aux = i;
        long length = 0;
        do
        {
            if(SetContains(chain_lengths, aux))
            {
                if(breadcrumbs.empty())
                {
                    aux = 1;
                    continue;
                }
                length = chain_lengths[aux];
                std::reverse(breadcrumbs.begin(), breadcrumbs.end());
                for (long & breadcrumb : breadcrumbs)
                {
                    chain_lengths[breadcrumb] = ++length;
                }
                aux = 1;
            }
            else
            {
                breadcrumbs.emplace_back(aux);
                aux = Collatz(aux);
            }
        } while(aux != 1);

        if(length > biggest.size)
        {
            biggest = Chain{i, length};
        }
        if(i == 5)
        {
            std::cout << i << std::endl;
        }
    }
    std::cout << biggest.number;
}
