#include<iostream>
#include<cmath>
#include<unordered_map>
#include<gmp.h>
#include<gmpxx.h>
#include<string>

using namespace std;

typedef mpz_class ll;

ll alpha, beta, N;

ll mod_pow(ll num, ll pow, ll mod)
{
	ll test;
	for (test = 1; pow; pow >>= 1)
	{
		if (pow % 2 == 1)
			test = (test * num) % mod;
		num = (num * num) % mod;
	}
	return test;
}

int main() {
	cin >> alpha >> beta >> N;
	ll m = sqrt(N) + 1;
	unordered_map<string, ll> table;
	ll k = 1;
	for (ll i = 0; i < m; i++) {
		table[k.get_str()] = i;
		k *= alpha;
		k %= N;
	}
	ll y = beta;
	ll am = mod_pow(alpha, N - m - 1, N);
	for (ll i = 0; i < m; i++) {
		if (table.find(y.get_str()) != table.end()) {
			cout << i * m + table[y.get_str()] << endl;
			return 0;
		}
		y *= am;
		y %= N;
	}
}
