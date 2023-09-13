// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

int strLen(char *s){
    int i = -1;
    while(s[++i] != '\0');
    return i;
}

int strStr(char * haystack, char * needle){
    if(needle[0] == '\0') return 0;
    int i = -1;
    int needleLen = strLen(needle);
    int hayLen = strLen(haystack);
    while(++i <= hayLen - needleLen){
        int j = -1;
        int k = i - 1;
        while(++j < needleLen && ++k < hayLen){
            if(haystack[k] != needle[j]) break;
        }
        if(j == needleLen) break;
    }
    if(i > hayLen - needleLen) return -1;
    return i;
}