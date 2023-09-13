// https://leetcode.com/problems/reverse-string

void swap(char* s, int i, int j) {
    char temp;
    temp = s[i];
    s[i] = s[j];
    s[j] = temp;
}

void reverseString(char* s, int sSize){
    if(sSize > 1) {
        swap(s, 0, sSize-1);
        reverseString(s+1, sSize-2);
    }
    else return;
}

