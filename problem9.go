package main

import (
	"fmt"
)

func is_pythagorean(a, b, c int) bool {
	if (a*a)+(b*b) == (c * c) {
		return true
	}
	return false
}

func main() {
	for i := 0; i < 999; i++ {
		for j := 0; j < 999; j++ {
			for k := 0; k < 999; k++ {
				if i < j {
					if j < k {
						if is_pythagorean(i, j, k) {
							if i+j+k == 1000 {
								fmt.Printf("%v\n", (i * j * k))
							}
						}
					}
				}
			}
		}
	}
}

// first loop is i, second is j, third is k
