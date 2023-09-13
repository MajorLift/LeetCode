// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

int strLen(char *s){
    int i = -1;
    while(s[++i] != '\0');
    return i;
}

int strStr(char * haystack, char * needle){
    int i = -1;
    while(haystack[++i] != '\0'){
        int j = -1;
        while(needle[++j] != '\0'){
            if(haystack[i] != needle[j]) break;
        }
        if(j == strLen(needle)) break;
    }
    if(i == strLen(haystack)) return 0;
    return i;
}

