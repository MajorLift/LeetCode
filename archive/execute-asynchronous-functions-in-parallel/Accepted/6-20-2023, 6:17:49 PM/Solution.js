// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel

/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise(async (resolve, reject) => {
        let completed = 0
        const output = new Array(functions.length).fill(null)
        functions.forEach(async (func, i) => {
            try {
                output[i] = await func()
                completed += 1
                if (completed === functions.length) resolve(output)
            } catch(err) {
                reject(err)
            }
        })
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */