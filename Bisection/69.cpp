class Solution {
public:
    int mySqrt(int x) {
        
        if (x == 0){return x;}
        int l = 1, r = x;
        int mid{0};
        int sqrt{0};
        while(1< r){
            mid = 1 + (r-1)/2;
            sqrt = x/mid;
            
            if(sqrt == mid){
                return mid;
            }else if(mid > sqrt){
                r = mid - 1;
            }else{
                l = mid+1;
            }
        }
        return r;
    }
};
