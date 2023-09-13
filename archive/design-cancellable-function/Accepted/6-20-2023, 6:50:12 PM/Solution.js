// https://leetcode.com/problems/design-cancellable-function

/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
    let cancelFn
    const cancelPromise = new Promise((_, reject) => cancelFn = () => reject("Cancelled"))
    cancelPromise.catch(() => {})
    return [
        cancelFn,
        (async () => {
            let next = generator.next()
            while (!next.done) {
                try {
                    next = generator.next(await Promise.race([next.value, cancelPromise]))
                } catch(err) {
                    next = generator.throw(err)
                }
            }
            return next.value
        })()
    ]
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */