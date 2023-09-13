// https://leetcode.com/problems/sqrtx



int mySqrt(int x){
    int left = 1;
    int right = left + x / 2;
    int mid;
    while(right - left >= 0){
        mid = left + (right - left) / 2;
        if(mid * mid == x) return mid;
        if(mid * mid > x) right = mid - 1;
        if(mid * mid < x) left = mid + 1;
    }
    return mid;
}

