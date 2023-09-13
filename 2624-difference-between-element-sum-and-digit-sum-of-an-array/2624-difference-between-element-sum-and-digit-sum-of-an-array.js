/**
 * @param {number[]} nums
 * @return {number}
 */
var differenceOfSum = function(nums) {
    const sum = (arr) => arr.reduce((acc, curr) => acc + curr)
    const [elemSum, digitSum] = [nums, nums.map(addDigits)].map(sum)
    return elemSum - digitSum
};

function addDigits(num) {
    let sum = 0
    while (num > 0) {
        sum += num % 10
        num = Math.floor(num / 10)
    }
    return sum
}