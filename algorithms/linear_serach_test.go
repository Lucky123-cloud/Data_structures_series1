package test



import (
	"testing"
)

func TestLinearSearch(t *testing.T) {
	tests := struct {
		name string
		input []int
		value int
		expected int
	}{
		{
			name: "getting index of value 5",
			input: []int{1, 2, 3, 4, 5},
			value: 5,
			expected: 4,
		},
		{
			name: "getting index of value 3",
			input: []int{1, 2, 3, 4, 5, , 6},
			value: 3,
			expected: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := linear_search(tt.input, tt.value)
			if result != tt.expected {
				t.Errorf("Error occured: expcted %v, got %v", tt.expected, result)
			}
		}
	}
}

