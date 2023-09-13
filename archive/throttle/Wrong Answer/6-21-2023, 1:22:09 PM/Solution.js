// https://leetcode.com/problems/throttle

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let timeout = argsQueued = null

    const recurse = () => {
        if (argsQueued === null) {
            timeout = null
        } else {
            fn(...argsQueued)
            argsQueued = null
            timeout = setTimeout(recurse, t)
        }
    }

    return function(...args) {
        if (timeout === null) {
            fn(...args)
            timeout = setTimeout(recurse, t)
        } else {
            argsQueued = args
        }
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */