class Solution {
    public long countPairs(int[] nums, int k) {
        Map<Integer, Integer> gcdMap = new HashMap<>();

        long count = 0;
        for (int n : nums) {
            int i = gcd(n, k);
            
            for (var e : gcdMap.entrySet()) {
                int j = e.getKey();
                int cnt = e.getValue();
                //convert to long to avoid i * j overflow error
                count += (long) i * j % k == 0 ? cnt : 0;
            }
            
            gcdMap.put(i, gcdMap.getOrDefault(i, 0) + 1);
        }
        return count;
    }
    
    private int gcd(int a, int b) {
        if (a < b) {
            return gcd(b, a);
        }
        if (a % b == 0) {
            return b;
        }
        return gcd(b, a % b);
    }
}
