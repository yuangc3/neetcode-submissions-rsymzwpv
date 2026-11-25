class Solution {
    public int[] twoSum(int[] nums, int target) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        Map<Integer, Integer> temp = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            int n = nums[i];
            temp.put(n, i);
        }

        for(int i = 0; i < nums.length; i++) {
            int n = nums[i];
            int complement = target - n;
            if (temp.containsKey(complement) && i != temp.get(complement)){
                return new int[]{i, temp.get(complement)};
            }
        
        }
        return new int[]{};
    }
}
