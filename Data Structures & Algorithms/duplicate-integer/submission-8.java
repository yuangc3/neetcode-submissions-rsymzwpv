class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> temp = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int n = nums[i];
            if (temp.containsKey(n)){
                return true;
            }
            temp.put(n, 1);

        }
        return false;
    }
}