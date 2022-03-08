func findMin(nums []int) int {
    min_res := 9999999
    for i:=0;i<len(nums);i++{
        if nums[i] < min_res{
            min_res = nums[i]
            }
        }
    return min_res
}