package main

import (
	"fmt"
	"strconv"
	"strings"
)

func is_palindrome(data int) bool {
	bool1 := true
	stringData := strconv.Itoa(data)
	listData := strings.Split(stringData, "")
	for i := 0; i < 3; i++ {
		if listData[0] != listData[len(listData)-1] {
			bool1 = false
			break
		}
		if len(listData) == 1 {
			break
		}
		if len(listData) == 2 {
			break
		}
		listData = listData[1 : len(listData)-1]
	}
	return bool1
}

func sol1() {
	for i := 999; i > 99; i-- {
		for j := 999; j >= i; j-- {
			if is_palindrome(i * j) {
				fmt.Printf("%v\n", i*j)
				return
				break
				//break
			}
		}
	}
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