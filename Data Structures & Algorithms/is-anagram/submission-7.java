class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> cnt1 = new HashMap<>();
        Map<Character, Integer> cnt2 = new HashMap<>();

        for (char v : s.toCharArray()){
            cnt1.put(v, cnt1.getOrDefault(v, 0)+1);
        }
        for (char c : t.toCharArray()){
            cnt2.put(c, cnt2.getOrDefault(c, 0)+1);
        }

        if (cnt1.equals(cnt2)) {
            return true;
        }
        return false;
    }
}
