class Solution {
	public String reverseStr(String s, int k) {
        char[] chars = s.toCharArray();
        for (int i=0; i < s.length(); i += k*2) {
            int x = i;
            int y = Math.min(i+k, s.length()) - 1;
            while (x <= y) {
                chars[x] = s.charAt(y);
                chars[y] = s.charAt(x);
                x ++;
                y --;
            }
        }

        return new String(chars);
	}
}