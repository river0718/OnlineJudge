#include <stdio.h>

int circle_length(int n) {
	int length = 1;

	while (n != 1) {
		length = length + 1;

		if (n % 2 == 0) {
			n = n / 2;
		}
		else {
			n = 3 * n + 1;
		}
	}

	return length;
}

int max_circle_length(int x, int y) {
	int temp = 0, max = 0;

	for (int i = x; i <= y; i++) {
		temp = circle_length(i);

		if (temp >= max) {
			max = temp;
		}
	}

	return max;
}

int main() {
	int a, b, ans = 0, temp = 0;
	
	while (scanf("%d %d", &a, &b) != EOF) {
		if (a < b) {
			ans = max_circle_length(a, b);
		}
		else {
			ans = max_circle_length(b, a);
		}

		printf("%d %d %d\n", a, b, ans);
	}
	
	return 0;
}