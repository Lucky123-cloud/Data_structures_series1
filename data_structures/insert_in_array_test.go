package test

import (
	"reflect"
	"testing"
)

func TestInsertInArray(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		pos      int
		num      int
		expected []int
	}{
		{
			name:     "adding an element to the last position",
			input:    []int{1, 2, 3, 4, 5},
			pos:      5,
			num:      99,
			expected: []int{1, 2, 3, 4, 5, 99},
		},
		{
			name:     "adding an elem to the first place",
			input:    []int{1, 2, 3, 4, 5},
			pos:      0,
			num:      99,
			expected: []int{99, 1, 2, 3, 4, 5},
		},
		{
			name:     "adding elem in between other elems",
			input:    []int{1, 2, 3, 4, 5},
			pos:      2,
			num:      99,
			expected: []int{1, 2, 99, 3, 4, 5},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := insertAt(tt.input, tt.pos, tt.num)
			if !reflect.DeepEqual(tt.expected, result) {
				t.Errorf("Error occurred, expected %v, got %v", tt.expected, result)
			}
		})
	}
}
