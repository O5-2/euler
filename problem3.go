package main

import (
	"fmt"
	"math"
)

func is_prime(y int) bool {
	max := (y / 2) + 1
	for i := 2; i < max; i++ {
		if y%i == 0 {
			return false
		}
	}
	return true
}

func prime_factors(x int) []int {
	maximum := (x / 2) + 1
	list := []int{}
	primes := []int{}
	for i := 2; i < maximum; i++ {
		if is_prime(i) {
			primes = append(primes, i)
		}
	}
	for i := 0; i < len(primes); i++ {
		if x%primes[i] == 0 {
			list = append(list, primes[i])
		}
	}
	return list
}

func main() {
	fmt.Printf("%v", prime_factors(600851475143))
}

// the input is 600851475143
