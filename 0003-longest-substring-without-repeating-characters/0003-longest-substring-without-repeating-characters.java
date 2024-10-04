class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        Set<Character> charSet = new HashSet<>();

        int left = 0;

        for (int right =0; right < s.length(); right++) {
            char r = s.charAt(right);
            if (charSet.contains(r)) {
                while (charSet.contains(r)) {
                    charSet.remove(s.charAt(left));
                    left ++;
                }
                charSet.add(r);
            } else {
                charSet.add(r);
                maxLength = Math.max(maxLength, right - left + 1);
            }
        }

        return maxLength;
    }
}