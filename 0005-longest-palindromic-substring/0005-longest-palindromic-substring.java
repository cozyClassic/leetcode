class Solution {
    public String longestPalindrome(String s) {
        int max_length = 1;
        String result = Character.toString(s.charAt(0));
    
        for (int i=1; i < s.length(); i++) {
				if (s.charAt(i-1) == s.charAt(i)) {
                    int[] LR = expandPalindrome(i-1, i, s);
                    if (LR[1] - LR[0]> max_length) {
                        max_length = LR[1] - LR[0];
                        result = s.substring(LR[0], LR[1]);
                    }
                }
			}
        
        for (int i=2; i <s.length(); i++) {
            if (s.charAt(i-2) == s.charAt(i)){
                int[] LR = expandPalindrome(i-2, i, s);
                if (LR[1] - LR[0]> max_length) {
                    max_length = LR[1] - LR[0];
                    result = s.substring(LR[0], LR[1]);
                }
            }
        }

        return result;
    }

    public int[] expandPalindrome(int l, int r, String s) {
        while (l -1 >= 0 && r+1 < s.length() && s.charAt(l-1) == s.charAt(r+1)) {
            l -= 1;
            r += 1;
        }

        return new int[] {l, r+1};
    }
}