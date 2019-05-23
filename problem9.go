package main

import (
	"fmt"
)

func is_pythagorean(a, b, c int) bool {
	return ((a*a)+(b*b) == (c * c))
}

func find_triple(number_sum int) [3]int {
     m := 0
     n := 0
     for (2*m*m) < number_sum {
     	 m++
	 if (number_sum - (2*m*m)) % (2*m) == 0 {
	    n = (number_sum - (2*m*m))/(2*m)
	    return [3]int{(m*m - n*n), 2*m*n, (m*m + n*n)}
	 }
     }
     return [3]int{-1, -1, -1}
}

func main() {
	for i := 999; i > 501; i-- {
		for j := 0; j < 1000-i; j++ {
		      	a := i-j
			b := j
			c := 1000-a-b
			if is_pythagorean(a, b, c) {
				fmt.Printf("%v\n", (a * b * c))
				return
			}
		}
	}
}