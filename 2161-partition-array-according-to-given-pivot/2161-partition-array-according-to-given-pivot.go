func pivotArray(nums []int, pivot int) []int {
    var idx int
    res := make([]int, len(nums))
    for i := range nums {
        if nums[i]<pivot {
            res[idx]=nums[i]
            idx++
        } 
    }
    
    for i := range nums {
        if nums[i]==pivot {
            res[idx]=pivot
            idx++
        } 
    }
    
    for i := range nums {
        if nums[i]>pivot {
            res[idx]=nums[i]
            idx++
        } 
    }
    
    
    return res
}