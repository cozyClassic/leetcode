class Solution {
	public boolean isSubstringPresent(String s) {
		HashMap<Character, Set<Character>> map = new HashMap();
		char[] chars = s.toCharArray();

		for (int i=0; i<s.length()-2; i++){
			Set<Character> set;
			if (map.containsKey(chars[i])) {
				set = map.get(chars[i]);
			} else {
				set = new HashSet<Character>();
				map.put(chars[i], set);
			}
			set.add(chars[i+1]);
		}

		for (int i=s.length()-1; i > 1; i--) {
			if (map.containsKey(chars[i])) {
				Set<Character> set = map.get(chars[i]);
				if (set.contains(chars[i-1])) return true;
			}
		}
		return false;
	}
}