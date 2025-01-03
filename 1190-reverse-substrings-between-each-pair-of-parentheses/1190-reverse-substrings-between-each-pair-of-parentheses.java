class Solution {
	public String reverseParentheses(String s) {
		List<Integer> opens = new ArrayList<>();

		char[] chars = s.toCharArray();
		int i = 0;
		int count = 0;
		while (i < chars.length) {
			if (chars[i] == '(') {
				opens.add(i);
				chars[i] = 0;
				count ++;
				continue;
			}
			if (chars[i] == ')') {
				// reverse open + 1 to i - 1
				int l = opens.remove(opens.size()-1) + 1;
				int r = i -1;
				while (l < r) {
					char temp = chars[l];
					chars[l] = chars[r];
					chars[r] = temp;
					l ++; r --;
				}
				chars[i] = 0;
			}
			i ++;
		}
		
		char[] result = new char[chars.length - 2 * count];
		
		int x = 0;
		for (char c: chars) {
			if (c == 0) continue;
			result[x] = c;
			x++;
		}

		return new String(result);
	}
}