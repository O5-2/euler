package main

import (
	"fmt"
)

func square_of_sum(x int) int {
     return (x*x*(x+1)*(x+1))/4
}

func sum_of_squares(x int) int {
     return (x*(x+1)*((2*x)+1))/6
}

func main() {
     	sumsquare := sum_of_squares(100)
	squaresum := square_of_sum(100)
	fmt.Printf("sum of squares is %v\n", sumsquare)
	fmt.Printf("square of sum is %v\n", squaresum)
	fmt.Printf("difference is %v\n", squaresum-sumsquare)
}
