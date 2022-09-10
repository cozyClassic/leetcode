var inorderTraversal = function(root) {
    const result = []
    function dfs(node) {
        if (node === null) {
            return
        }
        dfs(node.left);
        result.push(node.val);
        dfs(node.right);
    }
    
    dfs(root);
    
    return result
};