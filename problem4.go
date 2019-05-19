package main

import (
	"fmt"
	"strconv"
	"strings"
)

func is_palindrome(data int) bool {
	stringData := strconv.Itoa(data)
	listData := strings.Split(stringData, "")
	for i := 0; i < 3; i++ {
		if listData[i] != listData[len(listData)-i-1] {
		   	return false
		}
	}
	return true
}

func main() {
     for diag := 0; diag < 999; diag++ {
     	 for k := 0; k < diag + 1; k++ {
	     	x := 999-diag+k;
		y := 999-k;
			if is_palindrome(x * y) {
				fmt.Printf("%v\n", x*y)
				return
				break
				//break
			}

	 }
     }
}