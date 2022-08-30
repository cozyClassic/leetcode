/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    const n = matrix.length;
    const m = matrix[0].length;
    const origin = []
    matrix.map((mat) => origin.push([...mat]))

    for (let i=0; i<n; i++){
        for (let j=0; j<m; j++){
            matrix[j][n-i-1] = origin[i][j]
        }
    }
    
    
    return
};