# Algorithms-Note

- [Sort](https://github.com/simochen/algorithms-note#sort)
- [Bit Manipulation](https://github.com/simochen/algorithms-note#bit-manipulation)
- [Array](https://github.com/simochen/algorithms-note#array)
- [Linked List](https://github.com/simochen/algorithms-note#linked-list)
- [Hash Table](https://github.com/simochen/algorithms-note#hash-table)
- [Dynamic Programming](https://github.com/simochen/algorithms-note#dynamic-programming)



## Sort
| 排序算法 | 平均时间复杂度 |   最好    |   最坏    | 空间复杂度 | 排序方式  | 稳定性 |
| :------: | :------------: | :-------: | :-------: | :--------: | :-------: | :----: |
| 冒泡排序 |     O(n²)      |   O(n)    |   O(n²)   |    O(1)    | in-place  |  稳定  |
| 选择排序 |     O(n²)      |   O(n²)   |   O(n²)   |    O(1)    | in-place  | 不稳定 |
| 插入排序 |     O(n²)      |   O(n²)   |   O(n²)   |    O(1)    | in-place  |  稳定  |
| 希尔排序 |  $O(n^{1.3})$  |   O(n)    |   O(n²)   |    O(1)    | in-place  | 不稳定 |
| 归并排序 |    O(nlogn)    | O(nlogn)  | O(nlogn)  |    O(n)    | out-place |  稳定  |
| 快速排序 |    O(nlogn)    | O(nlogn)  |   O(n²)   |  O(logn)   | in-place  | 不稳定 |
|  堆排序  |    O(nlogn)    | O(nlogn)  | O(nlogn)  |    O(1)    | in-place  | 不稳定 |
| 计数排序 |     O(n+k)     |  O(n+k)   |  O(n+k)   |    O(k)    | out-place |  稳定  |
|  桶排序  |     O(n+k)     |  O(n+k)   |   O(n²)   |   O(n+k)   | out-place |  稳定  |
| 基数排序 |   O(d(n+r))    | O(d(n+r)) | O(d(n+r)) |  O(n+rd)   | out-place |  稳定  |

[Click here](https://github.com/simochen/algorithms-note/blob/master/sort.md) for details.



## Bit Manipulation

|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note|
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
|136 | [Single Number](https://leetcode.com/problems/single-number/) | [Python](./Python/single-number.py) | O(n)       | O(1)          | Easy         |||
|137 | [Single Number II](https://leetcode.com/problems/single-number-ii/) |  | O(n) | O(1)          | Medium         |||
|190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/)  | [Python](./Python/reverse-bits.py) | O(1)        | O(1)          | Easy           |||
|191  |[Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | [Python](./Python/number-of-1-bits.py) | O(1) | O(1)          | Easy           |||
|201 | [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) |  | O(1) | O(1) | Medium |||
|231 | [Power of Two](https://leetcode.com/problems/power-of-two/) | [Python](./Python/power-of-two.py) | O(1) | O(1) | Easy | LintCode ||
|260 | [Single Number III](https://leetcode.com/problems/single-number-iii/) |  | O(n) | O(1)          | Medium         |||
|268| [Missing Number](https://leetcode.com/problems/missing-number/) |   | O(n) |  O(1) | Medium         | LintCode ||
|318| [Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/) |   | O(n) ~ O(n^2) |  O(n) | Medium         || Bit Manipulation, Counting Sort, Pruning|
|342 | [Power of Four](https://leetcode.com/problems/power-of-four/) | [Python](./Python/power-of-four.py) | O(1) | O(1) | Easy | ||
|371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | [Python](./Python/sum-of-two-integers.py) | O(1) | O(1) | Easy | LintCode ||
|389 | [Find the Difference](https://leetcode.com/problems/find-the-difference/) | [Python](./Python/find-the-difference.py) | O(n) | O(1) | Easy | ||
|393 | [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/) |  | O(n) | O(1) | Medium | ||
|401 | [Binary Watch](https://leetcode.com/problems/binary-watch/) | [Python](./Python/binary-watch.py) | O(1) | O(1) | Easy | ||
|411 | [Minimum Unique Word Abbreviation](https://leetcode.com/problems/minimum-unique-word-abbreviation/) |  | O(2^n) | O(n) | Hard | 📖 ||
|421 | [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) |  | O(n) | O(1) | Medium |||
|461 | [Hamming Distance](https://leetcode.com/problems/hamming-distance/) | [Python](./Python/hamming-distance.py) | O(1) | O(1) | Easy |||
|462 | [Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) |  | O(n)  on average | O(1) | Medium |||
|477 | [Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/) |  | O(n) | O(1) | Medium |||
|645 | [Set Mismatch](https://leetcode.com/problems/set-mismatch/) | [Python](./Python/set-mismatch.py) | O(n) | O(1) | Easy |||
|693 | [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/) | [Python](./Python/binary-number-with-alternating-bits.py) | O(log(n)) | O(1) | Easy |||
|762 | [Prime Number of Set Bits in Binary Representation](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) | [Python](./Python/prime-number-of-set-bits-in-binary-representation.py) | O(1) | O(1) | Easy |||
|868 | [Binary Gap](https://leetcode.com/problems/binary-gap/) | [Python](./Python/binary-gap.py) | O(1) | O(1) | Easy |||
|898 | [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/) |  | O(n) | O(1) | Medium |||


## Array

|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note|
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
|015 | [3 Sum](https://leetcode.com/problems/3sum/)         | [C++](./C++/3sum.cpp) | O(n^2)        | O(1)          | Medium         || Two Pointers|
|016 | [3 Sum Closest](https://leetcode.com/problems/3sum-closest/) | [C++](./C++/3sum-closest.cpp) | O(n^2)       | O(1)          | Medium         || Two Pointers|
|018| [4 Sum](https://leetcode.com/problems/4sum/)         | [C++](./C++/4sum.cpp) | O(n^3)    | O(1)    | Medium         || Two Pointers|



## Linked List
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note|
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
|002| [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) |  | O(n)   | O(1)          | Medium         |||
|021| [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)| [Python](./Python/merge-two-sorted-lists.py) | O(n) | O(1) | Easy         |||
|023| [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) |  | O(nlogk)| O(1)| Hard          | | Heap, Divide and Conquer|
|024| [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)| [Python](./Python/swap-nodes-in-pairs.py)   | O(n)          | O(1)          | Easy         |||
|025| [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)|  | O(n)       | O(1)         | Hard         |||
|061| [Rotate List](https://leetcode.com/problems/rotate-list/)| [Python](./Python/rotate-list.py)   | O(n)          | O(1)          | Medium         |||
|082| [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)| [Python](./Python/remove-duplicates-from-sorted-list-ii.py) | O(n)       | O(1)         | Medium         |||
|083| [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)| [Python](./Python/remove-duplicates-from-sorted-list.py) | O(n)       | O(1)         | Easy           |||
|092| [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)| [Python](./Python/reverse-linked-list-ii.py) | O(n)       | O(1)         | Medium         |||
|138| [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) |  | O(n)   | O(1)          | Hard         |||
|160| [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)|  [Python](./Python/intersection-of-two-linked-lists.py) | O(m +n) | O(1)         | Easy           |||
|203| [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)| [Python](./Python/remove-linked-list-elements.py) | O(n)       | O(1)         | Easy         |||
|206| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)| [Python](./Python/reverse-linked-list.py) | O(n)       | O(1)         | Easy         |||
|234| [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)| [Python](./Python/palindrome-linked-list.py) | O(n)       | O(1)         | Easy         |||
|237| [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)| [Python](./Python/delete-node-in-a-linked-list.py) | O(1)       | O(1)         | Easy         | LintCode ||
|328| [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)|  | O(n)       | O(1)         | Medium         | ||
|369| [Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/)|  | O(n)       | O(1)         | Medium         | 📖 | Two Pointers |
|445| [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)|  | O(m +n)       | O(m + n)         | Medium         |||
|725 | [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/) |  | O(n + k) | O(1) | Medium |||
|817 | [Linked List Components](https://leetcode.com/problems/linked-list-components/) |  | O(m +n) | O(m) | Medium |||



## Hash Table
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note|
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
|001| [Two Sum](https://leetcode.com/problems/two-sum/)      | [C++](./C++/two-sum.cpp) | O(n)         | O(n)          | Easy         ||



## Dynamic Programming
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note|
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
|010| [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) |  | O(m * n) | O(n) | Hard |||
|053| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|[Python](./Python/maximum-subarray.py)| O(n)     | O(1)         | Easy         |||
|062| [Unique Paths](https://leetcode.com/problems/unique-paths/)    | [Python](./Python/unique-paths.py) | O(m * n)      | O(m)   | Medium         |||
|063| [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | [Python](./Python/unique-paths-ii.py) |  O(m * n) | O(m)  | Medium         |||
|064| [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)| [Python](./Python/minimum-path-sum.py) | O(m * n) | O(m)     | Medium         |||
|070| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)| [Python](./Python/climbing-stairs.py) | O(n)    | O(1)          | Easy           |||
|072| [Edit Distance](https://leetcode.com/problems/edit-distance/)|| O(m * n)      | O(m+n)      | Hard           |||
|087| [Scramble String](https://leetcode.com/problems/scramble-string/) |  | O(n^4) | O(n^3)        | Hard           |||
|091| [Decode Ways](https://leetcode.com/problems/decode-ways/)   | [Python](./Python/decode-ways.py) | O(n)          | O(1)          | Medium         |||
|096| [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | [Python](./Python/unique-binary-search-trees.py) | O(n)      | O(1)         | Medium         || Math|
|097| [Interleaving String](https://leetcode.com/problems/interleaving-string/)|| O(m * n) | O(m+n) | Hard         |||
|115| [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)|| O(n^2) | O(n) | Hard           |||
|120| [Triangle](https://leetcode.com/problems/triangle/)       |    | O(m * n)      | O(n)         | Medium         |||
|123| [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) |  | O(n) | O(1) | Hard |||
|132| [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) |  | O(n^2) | O(n^2) | Hard |||
|139| [Word Break](https://leetcode.com/problems/word-break/)     |  |  O(n * l^2)         | O(n)       | Medium         |||
|152| [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)|| O(n) | O(1) | Medium     |||
|174| [Dungeon Game](https://leetcode.com/problems/dungeon-game/)  |                                                              | O(m * n)     | O(m+n)      | Hard           |||
|188| [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)|  | O(k * n) | O(k) | Hard |||
|198| [House Robber](https://leetcode.com/problems/house-robber/)| [Python](./Python/house-robber.py) | O(n)          | O(1)          | Easy           |||
|213| [House Robber II](https://leetcode.com/problems/house-robber-ii/)| [Python](./Python/house-robber-ii.py) | O(n)          | O(1)          | Medium           |||
|221| [Maximal Square](https://leetcode.com/problems/maximal-square/)|  | O(n^2)         | O(n)          | Medium           | EPI ||
|256| [Paint House](https://leetcode.com/problems/paint-house/) |  | O(n)| O(1)| Medium |📖||
|265| [Paint House II](https://leetcode.com/problems/paint-house-ii/) |  | O(n * k)| O(k)| Hard |📖||
|276| [Paint Fence](https://leetcode.com/problems/paint-fence/) |  | O(n)| O(1)| Easy |📖||
|279| [Perfect Squares](https://leetcode.com/problems/perfect-squares/)|  | O(n * sqrt(n))         | O(n)          | Medium           ||  Hash |
|303| [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)| [Python](./Python/range-sum-query-immutable.py) | ctor: O(n), lookup: O(1)          | O(n)          | Easy           |||
|304| [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)| [Python](./Python/range-sum-query-2d-immutable.py) | ctor: O(m*n), lookup: O(1)          | O(m*n)          | Medium           |||
|309| [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |  | O(n) | O(1) | Medium |||
|312| [Burst Balloons](https://leetcode.com/problems/burst-balloons/) |  | O(n^3) | O(n^2) | Hard |||
|322| [Coin Change](https://leetcode.com/problems/coin-change/) |  | O(n * k) | O(k) | Medium |||
|351| [Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/) |  | O(9^2 * 2^9) | O(9 * 2^9) | Medium | 📖 | Backtracking |
|357| [Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits/) |  | O(n) | O(1) | Medium || Backtracking, Math |
|361| [Bomb Enemy](https://leetcode.com/problems/bomb-enemy/) |  | O(m * n) | O(m*n) | Medium | 📖 | |
|368| [Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/) |  | O(n^2) | O(n) | Medium | | |
|375| [Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/)|    | O(n^2)          | O(n^2)          | Medium         | ||
|377| [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)|    | O(nlogn + n * t)          | O(t)          | Medium         | ||
|403 | [Frog Jump](https://leetcode.com/problems/frog-jump/) |  | O(n) | O(n) ~ O(n^2) | Hard |||
|416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |  | O(n * s) | O(s) | Medium |||
|418 | [Sentence Screen Fitting](https://leetcode.com/problems/sentence-screen-fitting/) |  | O(r + n * c) | O(n) | Medium |📖||
|446 | [Arithmetic Slices II - Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/) |  | O(n^2) | O(n * d) | Hard |||
|465 | [Optimal Account Balancing](https://leetcode.com/problems/optimal-account-balancing/) |  | O(n * 2^n) | O(n * 2^n) | Hard |📖||
|466 | [Count The Repetitions](https://leetcode.com/problems/count-the-repetitions/) |  | O(s1 * min(s2, n1)) | O(s2) | Hard |||
|467 | [Unique Substrings in Wraparound String](https://leetcode.com/problems/unique-substrings-in-wraparound-string/) |  | O(n) | O(1) | Medium |||
|471 | [Encode String with Shortest Length](https://leetcode.com/problems/encode-string-with-shortest-length/) |  | O(n^3) on average | O(n^2) | Medium |📖||
|472 | [Concatenated Words](https://leetcode.com/problems/concatenated-words/) |  | O(n * l^2) | O(n * l) | Medium |||
|474 | [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) |  | O(s * m * n) | O(m*n) | Medium |||
|486 | [Predict the Winner](https://leetcode.com/problems/predict-the-winner/) |  | O(n^2) | O(n) | Medium | | |
|514 | [Freedom Trail](https://leetcode.com/problems/freedom-trail/) |  | O(k) ~ O(k * r^2) | O(r) | Hard |||
|516 | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) |  | O(n^2) | O(n) | Medium |||
|546 | [Remove Boxes](https://leetcode.com/problems/remove-boxes/) |  | O(n^3) ~ O(n^4) | O(n^3) | Hard |||
|552 | [Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/) |  | O(n) | O(1) | Hard |||
|562 | [Longest Line of Consecutive One in Matrix](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/) |  | O(m * n) | O(n) | Medium |📖||
|568 | [Maximum Vacation Days](https://leetcode.com/problems/maximum-vacation-days/) |  | O(n^2 * k) | O(k) | Hard |📖||
|576 | [Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/) |  | O(N * m * n) | O(m*n) | Medium |||
|583 | [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) |  | O(m * n) | O(n) | Medium |||
|600 | [Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/) |  | O(1) | O(1) | Hard |||
|629 | [K Inverse Pairs Array](https://leetcode.com/problems/k-inverse-pairs-array/) |  | O(n * k) | O(k) | Hard |||
|639 | [Decode Ways II](https://leetcode.com/problems/decode-ways-ii/) |  | O(n) | O(1) | Hard |||
|650 | [2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard/) |  | O(sqrt(n)) | O(1) | Medium |||
|656 | [Coin Path](https://leetcode.com/problems/coin-path/) |  | O(n * B) | O(n) | Hard |📖||
|664 | [Strange Printer](https://leetcode.com/problems/strange-printer/) |  | O(n^3) | O(n^2) | Hard |||
|673 | [Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) |  | O(n^2) | O(n) | Medium |||
|688 | [Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/) |  | O(k * n^2) | O(n^2) | Medium |||
|689 | [Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) |  | O(n) | O(n) | Hard |||
|691 | [Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word/) |  | O(T * S^T) | O(T * S^T) | Hard || Backtracking, Memoization|
|712 | [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) |  | O(m * n) | O(n) | Medium |||
|714 | [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) |  | O(n) | O(1) | Medium |||
|727 | [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/) |  | O(s * t) | O(s) | Hard |📖||
|730 | [Count Different Palindromic Subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences/) |  | O(n^2) | O(n) | Hard |||
|740 | [Delete and Earn](https://leetcode.com/problems/delete-and-earn/) |  | O(n) | O(1) | Medium |||
|741 | [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) |  | O(n^3) | O(n^2) | Hard |||
|746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | [Python](./Python/min-cost-climbing-stairs.py) | O(n) | O(1) | Easy |||
|750 | [Number Of Corner Rectangles](https://leetcode.com/problems/number-of-corner-rectangles/) |  | O(n * m^2) | O(n * m) | Medium |||
|764 | [Largest Plus Sign](https://leetcode.com/problems/largest-plus-sign/) |  | O(n^2) | O(n^2) | Medium |||
|788 | [Rotated Digits](https://leetcode.com/problems/rotated-digits/) | [Python](./Python/rotated-digits.py) | O(logn) | O(logn) | Easy || Memoization |
|790 | [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/) |  | O(logn) | O(logn) | Medium || Matrix Exponentiation |
|799 | [Champagne Tower](https://leetcode.com/problems/champagne-tower/) |  | O(n^2) | O(n) | Medium |||
|801 | [Minimum Swaps To Make Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/) |  | O(n) | O(1) | Medium |||
|805 | [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/) |  | O(n^4) | O(n^3) | Hard |||
|808 | [Soup Servings](https://leetcode.com/problems/soup-servings/) |  | O(1) | O(1) | Medium || Memoization |
|813 | [Largest Sum of Averages](https://leetcode.com/problems/largest-sum-of-averages/) |  | O(k * n^2) | O(n) | Medium || |
|818 | [Race Car](https://leetcode.com/problems/race-car/) |  | O(nlogn) | O(n) | Hard || |
|823 | [Binary Trees With Factors](https://leetcode.com/problems/binary-trees-with-factors/) |  | O(n^2) | O(n) | Medium || |
|837 | [New 21 Game](https://leetcode.com/problems/new-21-game/) |  | O(n) | O(n) | Medium || |
|838 | [Push Dominoes](https://leetcode.com/problems/push-dominoes/) |  | O(n) | O(n) | Medium || |
|847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) |  | O(n * 2^n) | O(n * 2^n) | Hard || BFS |
|877 | [Stone Game](https://leetcode.com/problems/stone-game/) |  | O(n^2) | O(n) | Medium | variant of [Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | |
|879 | [Profitable Schemes](https://leetcode.com/problems/profitable-schemes/) |  | O(n * p * g) | O(p * g) | || |