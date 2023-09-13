// https://leetcode.com/problems/add-two-promises

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    return new Promise((resolve, reject) => {
        let remaining = 2
        let ans = 0
        ;[promise1, promise2].forEach((promise) => {
            promise.then((res) => {
                ans += res
                remaining -= 1
                if (remaining === 0) resolve(ans)
            }).catch((err) => reject(err))
        })
    })
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */