#include "select.hpp"
#include <algorithm>

int base_case(std::vector<int> &arr, int p, int r, int i);
int random_partition(std::vector<int> &arr, int p, int r);
int random_select(std::vector<int> &arr, int p, int r, int i);

int random_select(std::vector<int> &arr, int p, int r, int i)
{
    if (p == r)
        return arr[p];
    int q = random_partition(arr, p, r);
    int k = q - p + 1;
    if (i == k)
        return arr[q];
    else if (i < k)
        return random_select(arr, p, q - 1, i);
    else
        return random_select(arr, q + 1, r, i - k);
}

int randomized_select(std::vector<int> &arr, int i)
{
    int n = arr.size();
    return random_select(arr, 0, n - 1, i);
}


int random_partition(std::vector<int> &arr, int p, int r)
{
    std::random_device rd;
    std::mt19937 mt(rd);
    std::uniform_int_distribution dist(p, r);
    int i = dist(mt);
    std::swap(arr[i], arr[r]);

    return partition(arr, p, r);
}

int partition(std::vector<int> &arr, int p, int r)
{
    int x = arr[r];
    int i = p - 1;
    for (int j = p; j < r; ++j)
    {
        if (arr[j] <= x)
        {
            i = i + 1;
            std::swap(arr [i], arr[j]);
        }
    }
    std::swap(arr [i + 1], arr[r]);
    return i + 1;

}

int linear_select(std::vector<int> &arr, int i)
{
    int n = arr.size();
    // return linear_select_rec(arr, 0, n - 1, i);
    return 1;
}

int linear_select_rec(std::vector<int> &arr, int p, int r, int i)
{
    std::vector<int> medians;
    if (r - p < 5)
        return arr[base_case(arr, p, r, i)];
    for (int j = p; r - j > 0; j += 5)
        medians.push_back(base_case(arr, p, j - 1, 3));

    int x = (r - p) - ((r - p) / 5) * 5;

    int n = medians.size();
    int M = linear_select_rec(medians, 0, n - 1, n / 2);
    // swap(, M, p);
    partition(medians, 0, n - 1);

    return 0;
}

int base_case(std::vector<int> &arr, int p, int r, int i)
{
    int ans;
    for (int _i = 0; _i < i; ++_i)
    {
        int count = 0;
        ans = arr[p + _i];
        for (int j = p; j <= r; ++j)
        {
            if (ans <= arr[j])   
                count++;
        }
        if (count == i)
            return p + _i;
    }
}
bool check(std::vector<int> &arr, int i, int x) 
{ 
    std::sort(arr.begin(), arr.end());
    if (arr[i] == x)
        return true;
    else return false;
}
