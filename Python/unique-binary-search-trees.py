# -*- coding: utf-8 -*-
# 二叉搜索树（Binary Search Tree），它或者是一棵空树，或者是具有下列性质的二叉树：
# 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
# 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
# 它的左、右子树也分别为二叉搜索树
# 中序遍历二叉搜索树可得到一个关键字的有序序列
# Time:  O(n^2)
# Space: O(n)
# 思路：树的数目 = sum(根节点为i的树的数目)
# 所有的树的数目都等于其左子树的种类数*其右子树的种类数
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        nums = [1, 1]
        for i in range(2, n+1):
            nums.append(0)
            for j in range(i):
                nums[i] += nums[j]*nums[i-1-j]
        return nums[-1]