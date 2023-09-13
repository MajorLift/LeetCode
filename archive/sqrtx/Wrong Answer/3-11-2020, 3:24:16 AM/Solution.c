// https://leetcode.com/problems/sqrtx



int mySqrt(int x){
    if(x == 0) return 0;
    if(x < 0) return -1;
    unsigned int left = 1;
    unsigned int right = left + x / 2;
    unsigned int mid;
    while(right - left >= 0){
        mid = left + (right - left) / 2;
        if(mid * mid == x) return mid;
        if(mid * mid > x){
            if((mid - 1) * (mid - 1) <= x) return --mid;
            right = mid - 1;
        }
        if(mid * mid < x){
            if((mid + 1) * (mid + 1) > x) return mid;
            left = mid + 1;
        }
    }
    return mid;
}

