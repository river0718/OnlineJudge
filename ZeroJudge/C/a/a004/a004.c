#include <stdio.h>

int main() {
	int year = 0;

	while (scanf("%d", &year) != EOF) {
		if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
			printf("�|�~\n");
		}
		else {
			printf("���~\n");
		}
	}

	return 0;
}
