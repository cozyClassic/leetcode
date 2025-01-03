class Solution {
	public String reverseStr(String s, int k) {
        char[] chars = new char[s.length()];
        for (int i=0; i < s.length(); i += k*2) {
            int x = i;
            int y = Math.min(i+k, s.length()) - 1;
            while (x <= y) {
                chars[x] = s.charAt(y);
                chars[y] = s.charAt(x);
                x ++;
                y --;
            }
            int z = i + k;
            while (z < i + 2 * k && z < s.length()) {
                chars[z] = s.charAt(z);
                z ++;
            }
        }
        return new String(chars);
	}
}