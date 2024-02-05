#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a[150005];
    int temp, pre = 0;
    int i, n, k;
    scanf("%d %d", &n, &k);
    for (i = 0; i < n; i++)
    {

        scanf("%d", &temp);
        a[i] = temp + pre;
        pre = a[i];
    }
    int mi = a[k - 1], seat = 0;
    for (i = 0; i < n - k; i++)
    {
        int w = a[i + k] - a[i];
        // printf("%d %d\n",mi,w);
        if (mi > w)
        {
            mi - w;
            seat = i + 1;
        }
    } // printf("#%d %d\n",mi,w);
    printf("%d\n", seat + 1);
    return 0;
}