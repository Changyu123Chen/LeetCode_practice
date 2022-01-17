class Solution {
public:
    int maxArea(vector<int>& height) {
        int length=height.size();
        int i=0,j=length-1;
        int res=0;
        while(i<j){
            int w=(j-i)*min(height[i],height[j]);
            res=max(res,w);
            if(height[i]<height[j])
                ++i;
            else
                --j;
            //cout<<"i"<<i<<"j"<<j<<"     ";
        }
        return res;
    }
};


