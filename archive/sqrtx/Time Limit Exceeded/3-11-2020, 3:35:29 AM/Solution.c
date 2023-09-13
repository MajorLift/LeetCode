// https://leetcode.com/problems/sqrtx



int mySqrt(int x){
    if(x == 0) return 0;
    int left = 1;
    int right = 46339;
    int mid;
    while(right - left >= 0){
        mid = left + (right - left) / 2;
        if(mid * mid == x) return mid;
        if(mid * mid > x){
            if((mid - 1) * (mid - 1) <= x) return --mid;
            right = mid;
        }
        if(mid * mid < x){
            if((mid + 1) * (mid + 1) > x) return mid;
            left = mid;
        }
    }
    return mid;
}

