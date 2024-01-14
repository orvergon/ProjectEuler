#include <iostream>
#include <cmath>
#include <string>

int main()
{
    int maior = 0;
    for(int x = 111; x <= 999; x++)
    {
        for(int y = 111; y <= 999; y++)
        {
            std::string s = std::to_string(x*y);
            bool palindrome = true;
            for(int i = 0; i <= s.size()/2; i++)
            {
                if(s[i] != s[s.size()-(i+1)])
                {
                    palindrome = false;
                }
            }
            if(palindrome)
                if(x*y > maior)
                    maior = x*y;
        }
    }
    std::cout << maior;
}
