package main

import (
	"fmt"
)

func gcd(x int, y int) int {
     if (x == 0) || (y == 0) {
     	return x+y
     }
     if x >= y {
	return gcd(y, x%y)
     }
     if y > x {
	return gcd(x, y%x)
     }
     return -1
}

func lcm(x int, y int) int {
     return x*y/gcd(x, y)
}

func main() {
     var least int
     least = 1
     for i := 2; i <= 20; i++ {
     	 least = lcm(least, i)
     }
     fmt.Printf("%v", least)
     return
}