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

func main() {
	for i := 999; i > 99; i-- {
		for j := 999; j > 99; j-- {
			if is_palindrome(i * j) {
				fmt.Printf("%v ", i*j)
				break
				//break
			}
		}
	}
}
