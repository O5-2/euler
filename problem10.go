package main

import (
	"fmt"
	"math"
)

func is_prime(y int) bool {
	max := int(math.Sqrt(float64(y))) + 1
	for i := 2; i < max; i++ {
		if y%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	sum := 0
	for i := 2; i < 2000000; i++ {
		if is_prime(i) {
			sum += i
		}
	}
	fmt.Printf("%v\n", sum)
}
