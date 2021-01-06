#include <stdio.h>

int main() {
	int number1 = 0, number2 = 0;

	while (scanf("%d %d", &number1, &number2) != EOF) {
		printf("%d\n", number1 + number2);
	}

	return 0;
}