package main

import (
	"fmt"
)

func main() {
	bool1 := false
	for i := 2520; i < 1000000000; i++ {
		for j := 2; j < 21; j++ {
			if i%j != 0 {
				bool1 = false
				break
			}
			if j == 20 {
				bool1 = true
			}
		}
		if bool1 == true {
			fmt.Printf("%v", i)
			break
		}
		bool1 = false
	}
}
