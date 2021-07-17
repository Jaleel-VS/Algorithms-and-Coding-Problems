#include <bits/stdc++.h>
 
// void tokenize(string s, string del = " ")
// {
//     int start = 0;
//     int end = s.find(del);
//     while (end != -1) {
//         cout << s.substr(start, end - start) << endl;
//         start = end + del.size();
//         end = s.find(del, start);
//     }
//     cout << s.substr(start, end - start);
// }

#include <bits/stdc++.h>
using namespace std;
 
// A quick way to split strings separated via spaces.
string simple_tokenizer(string s)
{
    stringstream ss(s);
    vector<int> myNumbers;
    string word;
    while (ss >> word) {
      myNumbers.push_back(stoi(word));      
    }

    string maxMin = to_string(*max_element(myNumbers.begin(), myNumbers.end())) + " " + to_string(*min_element(myNumbers.begin(), myNumbers.end()));

    return maxMin;
}

