class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if(intervals.empty()){
            return 0;
        }
        int len = intervals.size();
        sort(intervals.begin(), intervals.end(), [](vector<int>&a, vector<int>&b) {
            return a[1] < b[1]; // sort by the second element in each vector
            // do not forget & & 
        });
        int prev = intervals[0][1];
        int sum = 0;
        for(int i{1}; i< len; ++i){

            if (prev > intervals[i][0]){
                sum++;
            }else{
                prev = intervals[i][1];
            }
        }
        return sum;
    }
};
