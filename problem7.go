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
	primes := 2
	for i := 5; i < 1000000; i += 2 {
		if is_prime(i) {
			primes += 1
		}
		if primes == 10001 {
			fmt.Printf("%v\n", i)
			break
		}
	}
}
