class Solution {
    public String reverseOnlyLetters(String s) {
        int L = s.length();
        int l = 0;
        int r = L - 1;

        char[] chars = s.toCharArray();

        while (l < r) {
            while (!Character.isAlphabetic(chars[l]) && l < L-1) {
                l++;
            }
            while (!Character.isAlphabetic(chars[r]) && r > 0) {
                r--;
            }

            if (l > r) break;

            char temp = chars[l];
            chars[l] = chars[r];
            chars[r] = temp;

            l ++;
            r --;
        }

        return new String(chars);
    }
}