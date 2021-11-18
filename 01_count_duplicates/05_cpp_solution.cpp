// similar to py solutions 1 and 3

#include <bits/stdc++.h>

size_t duplicateCount(const char *in)
{
  if (in == NULL)
    return 0;

  std::string in_s(in);
  std::map<char, int> dups;
  size_t ret_size = 0;

  for (auto &it : in_s)
    dups[tolower(it)]++;

  for (auto &it : dups)
  {
    if (it.second > 1)
      ret_size++;
  }

  return ret_size;
}