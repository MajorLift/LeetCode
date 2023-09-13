// https://leetcode.com/problems/throttle

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let interval = argsQueued = null

    return function(...args) {
        if (interval) {
            argsQueued = args
            return
        }
        
        fn(...args)
        interval = setInterval(() => {
            if (argsQueued === null) {
                clearInterval(interval)
                interval = null
            } else {
                fn(...argsQueued)
                argsQueued = null
            }
        }, t)
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */