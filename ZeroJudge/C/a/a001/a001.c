#include <stdio.h>

int main() {
	char name[1000];
	while (scanf("%s", &name) != EOF) {
		printf("hello, %s\n", name);
	}
	return 0;
}