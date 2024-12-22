class Solution {
	public int lengthOfLongestSubstring(String s) {
		List<Character> list = new ArrayList<>();
        int result = 0;
		for (char c: s.toCharArray()) {
			if (list.contains(c)) {
				list = list.subList(list.indexOf(c)+1, list.size());
			}
            list.add(c);
            result = Math.max(result, list.size());
        }
		return result;
    }
}