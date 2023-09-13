// https://leetcode.com/problems/container-with-most-water

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let maxArea = 0;
    for (let i = 0; i < height.length; i += 1) {
        for (let j = 0; j < height.length; j += 1) {
            if (height[j] <= height[i] && height[j] * Math.abs(j - i) > maxArea) {
                maxArea = height[j] * Math.abs(j - i);
            }
        }
        
    }
    return maxArea;
};