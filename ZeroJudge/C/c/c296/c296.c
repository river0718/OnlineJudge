#include <stdio.h>
#include <stdlib.h>

int ans(int n, int m, int i, int boom_times) {
	if (i == boom_times) {
		return 0;
	}
	else {
		return (ans(n - 1, m, i + 1, boom_times) + m) % n;
	}
}

int main() {
	int number = 0, boom_round = 0, boom_times = 0;

	while (scanf("%d %d %d", &number, &boom_round, &boom_times) != EOF) {
		printf("%d\n", ans(number, boom_round, 0, boom_times) + 1);
	}

	return 0;
}