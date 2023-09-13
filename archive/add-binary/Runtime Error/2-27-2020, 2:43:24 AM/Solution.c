// https://leetcode.com/problems/add-binary

int charLen(char* s){
    int i = -1;
    while(s[++i] != '\0');
    return i;
}

void charReverse(char* s){
    char* head_ptr = s;
    char* tail_ptr = s;
    while(*tail_ptr++ != '\0');
    --tail_ptr;
    
    while(head_ptr != tail_ptr){
        char tmp = *tail_ptr;
        *tail_ptr = *head_ptr;
        *head_ptr = tmp;
        head_ptr++;
        tail_ptr--;
    }    
}

char * addBinary(char * a, char * b){
    int alen = charLen(a);
    int blen = charLen(b);
    int maxlen;
    if(alen >= blen) maxlen = alen;
    else maxlen = blen;
    char* ret = (char*) malloc(sizeof(char) * (maxlen + 1));
    int i = 0;
    int j = 0;
    while(++i <= alen && ++j <= blen){
        if(ret[i - 1] == '\0') ret[i - 1] = 0;
        int sum = a[alen - i] + b[blen - j] + ret[i - 1];
        if(sum == 3){
            ret[i - 1] = 1;
            ret[i] = 1;
        }else if(sum == 2){
            ret[i - 1] = 0;
            ret[i] = 1;
        }else if(sum == 1){
            ret[i - 1] = 1;
        }
    }
    charReverse(ret);
    return ret;
}

