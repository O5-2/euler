package main

import (
	"fmt"
)

func square_of_sum(x int) int {
	sum := 0
	for i := 1; i < x+1; i++ {
		sum += i
	}
	return sum * sum
}

func sum_of_squares(x int) int {
	sum := 0
	for i := 1; i < x+1; i++ {
		sum += i * i
	}
	return sum
}
func main() {
	fmt.Printf("sum of squares is %v\n", sum_of_squares(100))
	fmt.Printf("square of sum is %v\n", square_of_sum(100))
	fmt.Printf("difference is %v\n", square_of_sum(100)-sum_of_squares(100))
}
