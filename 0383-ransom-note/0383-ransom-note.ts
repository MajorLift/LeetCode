function canConstruct(ransomNote: string, magazine: string): boolean {
    const [ransom_cnt, magazine_cnt] = Array.from([ransomNote, magazine], (e) => (
        e.split('').reduce((acc, curr) => {
            acc[curr] ??= 0
            acc[curr] += 1
            return acc
        }, {})
    ))
    return Object
        .keys(ransom_cnt)
        .every((key) => ransom_cnt[key] <= (magazine_cnt[key] ?? 0))
};
