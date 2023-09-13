// https://leetcode.com/problems/cheapest-flights-within-k-stops

/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, k) {
    const adj = flights.reduce((acc, [u, v, w]) => {
        acc[u][v] = w
        return acc
    }, Array.from({ length: n }, () => new Array(n).fill(0)))

    const dist = Array.from({ length: n }, () => [+Infinity, +Infinity])
    dist[src] = [0, 0]

    const pq = new PriorityQueue((a, b) => (a.cost - b.cost ? a.cost - b.cost : a.stops - b.stops))
    pq.enqueue({ cost: 0, stops: 0, node: src })
    while (!pq.isEmpty()) {
        const { cost, stops, u } = pq.dequeue()
        if (u === dst) break
        for (const [v, w] of adj[u].entries) {
            if (w === 0) return

            const [min_cost_v, min_stops_v] = dist[v]
            const [cost_v, stops_v] = [cost + w, stops + 1]

            if (cost_v < min_cost_v 
                || (cost_v === min_cost_v && stops_v < min_stops_v)) {
                dist[v] = [cost_v, stops_v]
            }
            if (stops_v < k 
                && (cost_v < min_cost_v || stops_v < min_stops_v)) {
                pq.enqueue({ cost: cost_v, stops: stops_v, node: v })
            }
        }
    }

    const min_cost_to_dst = dist[dst][0]
    return min_cost_to_dst < +Infinity ? min_cost_to_dst : -1
}