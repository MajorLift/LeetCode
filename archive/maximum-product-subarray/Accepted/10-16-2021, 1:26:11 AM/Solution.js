// https://leetcode.com/problems/maximum-product-subarray

var maxProduct = function(nums) {
    let currMax = nums[0];
    let currMin = nums[0];
    let max = nums[0];
    for (let i = 1; i < nums.length; i += 1) {
        let tempMax = currMax;
        let tempMin = currMin;
        currMin = Math.min(nums[i], nums[i] * tempMin, nums[i] * tempMax); //3
        currMax = Math.max(nums[i], nums[i] * tempMax, nums[i] * tempMin);
        max = Math.max(max, currMax);
        console.log(max, currMax, currMin)
    }
    return max;
};