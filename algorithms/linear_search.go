package main

func linear_search(s []int, value int) (int) {
	if len(s) == 0 {
		return 0
	}

	for i := range s {
		if s[i] == value {
			return i
		}
		return nil
	}
}
