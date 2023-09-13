// https://leetcode.com/problems/sqrtx



int mySqrt(int x){
    if(x == 0) return 0;
    if(x < 0) return -1;
    int left = 1;
    int right = left + x / 2;
    int mid;
    while(right - left > 0){
        mid = left + (right - left) / 2;
        if(mid * mid == x) return mid;
        if(mid * mid > x){
            right = mid - 1;
            if((mid - 1) * (mid - 1) <= x) return --mid;
        }
        if(mid * mid < x){
            left = mid + 1;
            if((mid + 1) * (mid + 1) > x) return mid;
        }
    }
    return mid;
}

