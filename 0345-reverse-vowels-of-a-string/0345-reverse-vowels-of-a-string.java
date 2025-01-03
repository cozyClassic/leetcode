class Solution {
    char[] vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

    public boolean isVowel(char c) {
		for (char v: vowels) {
			if (c == v) { return true; }
		}
		return false;
	}

    public String reverseVowels(String s) {
        int l = 0;
        int r = s.length() - 1;

        char[] strs = s.toCharArray();

        while (l < r) {
            boolean findingL = true;
            while (findingL && l < s.length()) {
                if (isVowel(strs[l])) {
                    findingL = true;
                    break;
                }
                l++;
            }

            boolean findingR = true;
            while (findingR && r > -1) {
                if (isVowel(strs[r])) {
                    findingR = false;
                    break;
                }
                r--;
            }

            if (l >= r) {
                break;
            }

            strs[l] = strs[r];
            strs[r] = s.charAt(l);

            l ++;
            r --;
        }

        return new String(strs);
    }
}