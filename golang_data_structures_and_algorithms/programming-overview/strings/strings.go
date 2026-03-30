package strings

import "fmt"

func changeString() string {
	s := "hello, World"

	//let's change the h to be H
	r := []rune(s)

	//let's change it now
	r[0] = 'H'

	//convert it back to string
	s2 := string(r)

	return s2

}

func main() {
	fmt.Println(changeString())
}
