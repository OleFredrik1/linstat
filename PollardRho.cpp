#include<iostream>
#include<algorithm>
#include<gmp.h>
#include<gmpxx.h>
#include<string>

using namespace std;

typedef mpz_class ull;

ull alpha, beta, N;

ull gcdExtended(ull a, ull b, ull* x, ull* y);

// Function to find modulo inverse of a
ull modInv(ull a, ull m)
{
	ull x, y;
	ull k = gcd(a, m);
	a /= k;
	m /= k;
	ull g = gcdExtended(a, m, &x, &y);
	// m is added to handle negative x
	return (x % m + m) % m;
}

// C function for extended Euclidean Algorithm
ull gcdExtended(ull a, ull b, ull* x, ull* y)
{
	// Base Case
	if (a == 0)
	{
		*x = 0, * y = 1;
		return b;
	}

	ull x1, y1; // To store results of recursive call
	ull g = gcdExtended(b % a, a, &x1, &y1);

	// Update x and y using results of recursive
	// call
	*x = y1 - (b / a) * x1;
	*y = x1;

	return g;
}
ull f(ull x) {
	if (x % 3 == 2) {
		return (beta * x) % N;
	}
	if (x % 3 == 0) {
		return (x * x) % N;
	}
	return (alpha * x) % N;
}

ull g(ull x, ull n) {
	if (x % 3 == 2) {
		return n;
	}
	if (x % 3 == 0) {
		return (2 * n) % (N - 1);
	}
	return (n + 1) % (N - 1);
}

ull h(ull x, ull n) {
	return g((-x % 3) + 3, n);
}

int main() {
	cin >> alpha >> beta >> N;
	ull as = 0;
	ull bs = 0;
	ull xs = 1;
	ull al = 0;
	ull bl = 0;
	ull xl = 1;
	while (true)
	{
		as = g(xs, as);
		bs = h(xs, bs);
		xs = f(xs);
		al = g(f(xl), g(xl, al));
		bl = h(f(xl), h(xl, bl));
		xl = f(f(xl));
		if (xs == xl) {
			ull r = (bs - bl + N-1) % (N-1);
			if (r == 0) {
				cout << "No solution found";
				return 1;
			}
			ull g = gcd(r, N-1);
			r /= g;
			ull a = (al-as) / g;
			ull n = (N-1) / g;
			ull x = ((modInv(r, n) + N-1) * (a + N-1)) % n;
			mpz_class y, d;
			mpz_powm(y.get_mpz_t(), alpha.get_mpz_t(), x.get_mpz_t(), N.get_mpz_t());
			mpz_powm(d.get_mpz_t(), alpha.get_mpz_t(), n.get_mpz_t(), N.get_mpz_t());
			for (int i=0; i<g; i++){
				if (y == beta){
					cout << x + i*n << endl;
					return 0;
				}
				y *= d;
				y %= N;
			}
			return 0;
		}
	}
}