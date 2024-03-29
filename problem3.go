package main

import (
	"fmt"
	"math"
)

func max(x, y int) int {
	if x < y {
		return y
	} else {
		return x
	}
}

func is_prime(y int) bool {
	max := int(math.Sqrt(float64(y))) + 1
	for i := 2; i < max; i++ {
		if y%i == 0 {
			return false
		}
	}
	return true
}

func list_factors(x int) []int {
     var factors []int
     for i := 2; i < ((x/2)+1); i++ {
     	 if x%i == 0 {
	    return append(append(factors, i), list_factors(x/i)...)
	 }
     }
     return append(factors, x)
}

func max_prime_factor(x int) int {
     factors := list_factors(x)
     return factors[len(factors)-1]
}

func max_factor(x int) int {
	for i := 2; i < ((x/2)+1); i++ {
		if (is_prime(i)) && (x%i == 0) {
			return max(max_factor(x / i), i)
		}
	}
	return x
}

func main() {
	fmt.Printf("%v\n", max_factor(600851475143))
	return
}

// the input is 600851475143
