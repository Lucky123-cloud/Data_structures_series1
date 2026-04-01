package main

import "fmt"

func IncreamentPassByValue(x int) {
	x++
}

func main() {
	i := 10
	fmt.Println("Value of i before increament is: ", i)
	IncreamentPassByValue(i)
	fmt.Println("Value of i after increament is: ", i)
}

//we see that pass by value just makes a copy of the variable (argument) being called
// and it does not affect anything when the function exits
// that means the value before and after remains the same
