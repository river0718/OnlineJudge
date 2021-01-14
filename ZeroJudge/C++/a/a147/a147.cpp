#include <iostream>

using namespace std;

int main() {
	int number, i;

	while (true) {
		cin >> number;

		if (number == 0) {
			break;
		}

		for (i = 1; i < number; i++) {
			if (i % 7 == 0) {
				continue;
			}

			if (i + 1 != number) {
				cout << i << " ";
			}
			else {
				cout << i << endl;
			}
		}
	}

	return 0;
}
