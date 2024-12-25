#include <iostream>
#include <cmath>

int sumOfAllDivisors(int n) {
    int total_sum = 0;

    // Iterate over each number from 1 to n
    for (int i = 1; i <= n; i++) {
        int sum = 0;
        
        // Calculate sum of divisors for i
        for (int j = 1; j <= std::sqrt(i); j++) {
            if (i % j == 0) {
                if (j == i / j) {
                    // If divisors are the same, add it only once
                    sum += j;
                } else {
                    // Otherwise add both divisors
                    sum += j + (i / j);
                }
            }
        }
        
        // Add the sum of divisors of i to the total sum
        total_sum += sum;
    }

    return total_sum;
}

int main() {
    int n = 5;
    std::cout << "Sum of all divisors from 1 to " << n << " is: " << sumOfAllDivisors(n) << std::endl;
    
    n = 3;
    std::cout << "Sum of all divisors from 1 to " << n << " is: " << sumOfAllDivisors(n) << std::endl;
    
    n = 10;
    std::cout << "Sum of all divisors from 1 to " << n << " is: " << sumOfAllDivisors(n) << std::endl;

    return 0;
}
