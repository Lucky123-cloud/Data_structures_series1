package main

import "fmt"

// func main() {
// 	num := [...]int{1, 2, 3, 4, 5}

// 	sum := 0

// 	for i := 0; i < len(num); i++ {
// 		sum = sum + num[i]
// 	}
// 	fmt.Println(sum)
// }

// func main() {
// 	num := [...]int{1, 2, 3, 4, 5}

// 	sum := 0

// 	for _, val := range num {
// 		sum = sum + val
// 	}

// 	fmt.Println(sum)
// }

func main() {
	num := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	sum := 0

	for index, val := range num {
		sum = sum + val
		fmt.Print("[", index, ",", val, "] ")
	}

	kvs := map[int]string{1: "apple", 2: "banana"}
	for k, v := range kvs {
		fmt.Println(k, " -> ", v)
	}
	str := "Hello, World!"
	for index, c := range str {
		fmt.Print("[", index, ",", string(c), "] ")
	}
}
