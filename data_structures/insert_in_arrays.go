package test

/*
 * When inserting an element in an array, we have to know the index where the element is to be inserted
 * if the elem is at the end, it can be entered in that pos by assigning it to that index
 * if the elm is to added between two places that are together, then it is hard because w ehave to move
 * the existsing elements aside to create space this is an issue because arr store things in contingous mem
 */

func insertAt(s []int, pos, num int) []int {
	s = append(s, 0)
	copy(s[pos+1:], s[pos:])
	s[pos] = num
	return s
}
