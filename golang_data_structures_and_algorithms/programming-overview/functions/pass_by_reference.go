package main

import "fmt"

func IncreamentPassByPointer(ptr *int) {
	(*ptr)++
}

func main() {
	i := 10
	fmt.Println("Value of i before increment is: ", i)
	IncreamentPassByPointer(&i)
	fmt.Println("Value of i after increment is: ", i)

}
