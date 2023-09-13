// https://leetcode.com/problems/container-with-most-water

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
//     let maxArea = 0;
//     for (let i = 0; i < height.length; i += 1) {
//         for (let j = 0; j < height.length; j += 1) {
//             if (height[j] <= height[i] && height[j] * Math.abs(j - i) > maxArea) {
//                 maxArea = height[j] * Math.abs(j - i);
//             }
//         }
        
//     }
//     return maxArea;
    let maxArea = 0;
    let [left, right] = [0, height.length - 1];
    while (left <= right && right >= 0 && left <= height.length - 1) {
        const area = (right - left) * Math.min(height[left], height[right]);
        if (area > maxArea) maxArea = area;
        if (height[left + 1] > height[left]) left++;
        else if (height[right - 1] > height[right]) right--;
        else {
            if ((height[left] - height[left + 1]) < (height[right] - height[right - 1])) left++;
            else right--;
        }
    }
    return maxArea;
};