#include <stdio.h>

int main() {
	int m = 0, d = 0, s = 0;

	while (scanf("%d %d", &m, &d) != EOF) {
		s = (m * 2 + d) % 3;

		if (s == 0) {
			printf("´¶³q\n");
		}
		else if (s == 1) {
			printf("¦N\n");
		}
		else {
			printf("¤j¦N\n");
		}
	}

	return 0;
}