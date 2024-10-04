class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        Set<Character> charSet = new HashSet<>();

        int left = 0;

        for (int right =0; right < s.length(); right++) {
            if (charSet.contains(s.charAt(right))) {
                while (charSet.contains(s.charAt(right))) {
                    charSet.remove(s.charAt(left));
                    left ++;
                }
                charSet.add(s.charAt(right));
            } else {
                charSet.add(s.charAt(right));
                maxLength = Math.max(maxLength, right - left + 1);
            }
        }

        return maxLength;
    }
}