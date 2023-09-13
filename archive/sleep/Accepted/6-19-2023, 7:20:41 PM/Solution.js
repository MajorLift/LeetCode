// https://leetcode.com/problems/sleep

/**
 * @param {number} millis
 */
async function sleep(millis) {
    let timer
    return new Promise((resolve, reject) => {
        try {
            timer = setTimeout(() => {
                resolve()
            }, millis)
        } catch(err) {
            reject(err)
        } finally {
            () => clearTimeout(timer)
        }
    })
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */