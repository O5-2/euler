package main

import (
	"fmt"
)

const M = 2000000

func filter(sieve []bool, k int) {
	for i := k; i < len(sieve); i += k {
		sieve[i] = true
	}
}

func main() {
	sieve := make([]bool, M)
	sum := 0
	for i := 2; i < M; i++ {
		if !(sieve[i]) {
			filter(sieve, i)
			sum += i
		}
	}
	fmt.Printf("%v\n", sum)
}
