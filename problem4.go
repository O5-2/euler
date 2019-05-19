package main

import (
	"fmt"
)

func is_palindrome_new(data int) bool {
     var digits []int
     for data > 0 {
     	 last := data % 10
     	 digits = append(digits, last)
	 data /= 10
     }
     i := 0
     j := len(digits) - 1
     for i <= j {
     	 if digits[i] != digits[j] {
	    return false
	 }
	 i++
	 j--
     }
     return true
}

func main() {
     for diag := 0; diag < 999; diag++ {
     	 for k := 0; k < diag + 1; k++ {
	     	x := 999-diag+k;
		y := 999-k;
		if is_palindrome_new(x * y) {
			fmt.Printf("%v\n", x*y)
			return
		}
	 }
     }
}