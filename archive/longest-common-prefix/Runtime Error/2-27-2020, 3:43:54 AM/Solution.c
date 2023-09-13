// https://leetcode.com/problems/longest-common-prefix

char* substr(char* s, int a, int b){
    char* ret = (char*) malloc(sizeof(char) * (b - a));
    int i = 0;
    while(i < b - a) ret[i++] = s[a + i++];
    return ret;
}

char * longestCommonPrefix(char ** strs, int strsSize){
    int j = 0;   
    while(strs[0][j] != '\0'){
        int i = 0;
        while(i < strsSize){
            if(strs[i][j] == '\0') break;
            if(strs[i][j] != strs[++i][j]) break;
        }
        if(i == strsSize) j++;
        else break;
    }
    if(j == 0) return '\0';
    return substr(strs, 0, j);
}

