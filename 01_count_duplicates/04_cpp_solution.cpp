#include <bits/stdc++.h>

size_t duplicateCount(const char* in)
{
    int hmp[128] {0}; // create an array with the range of all possible alphanumeric characters
    auto duplicates = std::size_t{0}; 
    while (*in) //iterate over string
    {
        auto lower_c = std::tolower(*in); // convert current letter to lower
        ++hmp[lower_c]; // increment int value of char by 1 (kinda works like a hash map)
        if (hmp[lower_c] == 2) ++duplicates; // increment duplicates if value is 2
        ++in; 
    }
    return duplicates;
}