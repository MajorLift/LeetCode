// https://leetcode.com/problems/maximize-distance-to-closest-person

/**
 * @param {number[]} seats
 * @return {number}
 */
var maxDistToClosest = function(seats) {
    const distances = new Array(seats.length).fill(0);
    const ones = seats.reduce((acc, curr, i) => {
        if (curr === 1) acc.push(i);
        return acc;
    }, []);
    ones.forEach((e, i) => {
        let [j, k] = [1, 1];
        while (e - j >= 0 && (distances[e - j] === 0 || distances[e - j] > j)) {
            distances[e - j] = j;
            j++;
        }
        while (e + k < seats.length && e + k < ones[i + 1] && (distances[e + k] === 0 || distances[e + k] > k)) {
            distances[e + k] = k;
            k++;
        }
    });
    // console.log(distances);
    return Math.max(...distances);
};