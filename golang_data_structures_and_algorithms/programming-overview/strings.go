//string is a sequence of unicode characters, they are immutable
//if we want to modify strings, we first convert it into slice of runes do the changes, then convert it back to string

//lets try this:

package main

import (
	"fmt"
)

func main() {
	//we declare the string here. We want to change the h to be H
	s := "hello, World"

	//we first change it to a slice of rune.
	r := []rune(s)

	//then we do the change we want
	r[0] = 'H'

	//we convert it back to string
	s2 := string(r)

	//then show it out
	fmt.Println(s2)

}
