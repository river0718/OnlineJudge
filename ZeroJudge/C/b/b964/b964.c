#include <stdio.h>
#include <stdlib.h>

void Sort(int* n, int times);
int all_pass(int* n, int times);
int max_fail(int* n,int times);
int all_fail(int* n, int times);
int min_pass(int* n, int times);

int main() {
	int times = 0;
	int* score;

	while (scanf("%d", &times) != EOF) {
		score = malloc(times * sizeof(int));
		
		// input number
		for (int i = 0; i < times; i++) {
			scanf("%d", &score[i]);
		}

		Sort(score,times);

		// output number
		for (int i = 0; i < times - 1; i++) {
			printf("%d ", score[i]);
		}
		printf("%d\n", score[times - 1]);

		if (all_pass(score, times)) {
			printf("best case\n");
		}
		else {
			printf("%d\n", max_fail(score, times));
		}

		if (all_fail(score, times)) {
			printf("worst case\n");
		}
		else {
			printf("%d\n", min_pass(score, times));
		}

		free(score);
	}
	
	return 0;
}

void Sort(int* n, int times) {
	int temp = 0;

	for (int i = times - 1; i > 0; i--) {
		for (int j = 0; j <= i - 1; j++) {
			
			if (*(n + j) > * (n + j + 1)) {
				temp = *(n + j);
				* (n + j) = *(n + j + 1);
				*(n + j + 1) = temp;
			}
		}
	}
}

int all_pass(int* n, int times) {
	for (int i = 0; i < times; i++) {
		if (*(n + i) < 60) {
			return 0;
		}
	}
	return 1;
}

int max_fail(int* n, int times) {
	int max = 0;
	for (int i = 0; i < times; i++) {
		if (*(n + i) < 60 && *(n + i) > max) {
			max = *(n + i);
		}
		if (*(n + i) >= 60) {
			break;
		}
	}
	
	return max;
}

int all_fail(int* n, int times) {
	for (int i = 0; i < times; i++) {
		if (*(n + i) >= 60) {
			return 0;
		}
	}
	return 1;
}

int min_pass(int* n, int times) {
	int min = 100;
	for (int i = times - 1; i >= 0; i--) {
		if (*(n + i) >= 60 && *(n + i) < min) {
			min = *(n + i);
		}
		if (*(n + i) < 60) {
			break;
		}
	}
	return min;
}
