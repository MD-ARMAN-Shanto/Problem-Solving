func maxArea(height []int) int {
	n := len(height)

	var l, result int
	r := n - 1

	for l < r {
		currArea := min(height[l], height[r]) * (r - l)
		result = max(result, currArea)
        
		if height[l] < height[r] {
			l++
		} else {
			r--
		}
	}
	return result
}

func min(a,b int) int {
    if a<b{
        return a
    }
    return b
}

func max(a, b int) int {
    if a>b {
        return a
    }
    return b
}