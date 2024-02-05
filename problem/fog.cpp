#include <bits/stdc++.h>
using namespace std;

map<int, int> mults;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        mults.clear();
        for (int i = 0; i < n; i++)
        {
            int curr;
            cin >> curr;
            mults[curr] += 1;
        }
        int tot[200005] = {0};
        int ans = 0;
        for (int i = 1; i <= n; i++)
        {
            int currMult = i;
            while (currMult <= n)
            {
                tot[currMult] += mults[i];
                currMult += i;
            }

            ans = max(ans, tot[i]);
        }

        cout << ans << endl;
    }
    return 0;
}