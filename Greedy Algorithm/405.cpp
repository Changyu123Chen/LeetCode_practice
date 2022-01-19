class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);
        int len = flowerbed.size();
        int k{0};
        
        for(int i{1}; i< len-1; ++i){
            if(flowerbed[i-1] == 0 && flowerbed[i+1] == 0 && flowerbed[i] == 0){
                flowerbed[i] = 1;
                k++;
            }
        }
        return k>=n;
    }
};
