class Solution {
    public String reverseWords(String s) {
        String[] strs = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i=strs.length-1; i > -1; i --) {
            if (strs[i].isBlank()) { continue; }
            sb.append(strs[i]);
            sb.append(" ");
        }
        sb.deleteCharAt(sb.length()-1);
        return sb.toString();
    }
}