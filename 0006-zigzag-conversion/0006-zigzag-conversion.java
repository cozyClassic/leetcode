class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) { return s; }

        int numColumns = s.length()/(numRows+(numRows-2)) * (numRows-1);
        int last = s.length()%(numRows+(numRows-2));
        if (last != 0) {
            if (last <= numRows) {
                numColumns +=1;
            } else {
                numColumns += last + 1 - numRows;
            }
        }
        char[][] chars = new char[numRows][numColumns];
        System.out.println(numRows + " " + numColumns);

        int rowCount = 0;
        int columnCount = 0;
        boolean goDown = true;

        for (char c: s.toCharArray()){
            System.out.println("C:" + c + " row:" + rowCount + " col:" + columnCount);
            if (goDown) {
                chars[rowCount][columnCount] = c;
                rowCount ++;

                if (rowCount == numRows){
                    if (numRows == 2) {
                        rowCount = 0;
                    } else {
                        goDown = false;
                        rowCount -= 2;
                    }
                    columnCount ++;
                }
            } else {
                chars[rowCount][columnCount] = c;
                columnCount ++;
                rowCount --;

                if (rowCount == 0) {
                    goDown = true;
                }
            }
        }

        StringBuilder result = new StringBuilder();
        for (char[] row : chars) {
            for (char c: row) {
                if (c != '\u0000') {
                    result.append(c);
                }
            }
        }

        return result.toString();
    }
}