package main

import "fmt"

func main() {
	fruits := map[string]int{"Lemon": 9, "Banana": 4, "Chapati": 3}

	for k, v := range fruits {
		fmt.Println(k, "->", v)
	}
}
