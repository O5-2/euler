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

func max_factor(x int) int {
	maximum := (x / 2) + 1
	for i := 2; i < maximum; i++ {
		if is_prime(i) {
			if x%i == 0 {
				compare := max_factor(x / i)
				return max(compare, i)
			}
		}
	}
	return x
}

func main() {
	fmt.Printf("%v\n", max_factor(600851475143))
}

// the input is 600851475143
