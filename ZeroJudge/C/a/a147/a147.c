#include <stdio.h>

int main() {
	int number, i;

	while (1) {
		scanf("%d", &number);

		if (number == 0) {
			break;
		}

		for (i = 0; i < number; i++) {
			if (i % 7 == 0) {
				continue;
			}

			if (i + 1 != number) {
				printf("%d ", i);
			}
			else {
				printf("%d\n", i);
			}
		}
	}

	return 0;
}
