// https://leetcode.com/problems/car-pooling

/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
var carPooling = function(trips, capacity) {
    const lastStop = Math.max(...trips.map((e) => e[2]));
    const demand = trips.reduce((acc, curr) => {
        const [numPassengers, from, to] = curr;
        for (let i = from; i < to; i += 1) {
            acc[i] += numPassengers;
        }
        return acc;
    }, new Array(lastStop).fill(0));
    console.log(demand);
    return demand.every((e) => e <= capacity);
};