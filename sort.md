# 排序算法

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

**关于时间复杂度**：

1. 平方阶 ( O(n²) ) 排序：各类简单排序：直接插入、直接选择和冒泡排序；
2. 线性对数阶 ($O(n\log_2n)$) 排序：快速排序、堆排序和归并排序；
3. $O(n^{1+c})$ 排序，c 是介于 0 和 1 之间的常数：希尔排序；
4. 线性阶 ( O(n) ) 排序：基数排序，此外还有桶、箱排序。

**关于稳定性**： 排序后 2 个相等键值的顺序和排序之前它们的顺序相同

- 稳定的排序算法：冒泡排序、插入排序、归并排序和基数排序。
- 不稳定的排序算法：选择排序、快速排序、希尔排序、堆排序。

## 冒泡排序

冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

> 冒泡排序还有一种优化算法，就是立一个 flag，当在一趟序列遍历中元素没有发生交换，则证明该序列已经有序。但这种改进对于提升性能来说并没有什么太大作用。


### 1. 算法步骤

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。


### 2. 动图演示

![动图演示](https://raw.githubusercontent.com/hustcc/JS-Sorting-Algorithm/master/res/bubbleSort.gif)


### 3. 什么时候最快

当输入的数据已经是正序时（都已经是正序了，我还要你冒泡排序有何用啊）。


### 4. 什么时候最慢

当输入的数据是反序时（写一个 for 循环反序输出数据不就行了，干嘛要用你冒泡排序呢，我是闲的吗）。


### 5. Python 代码实现

```python
# 升序
def bubbleSort(arr):
    # flag = False
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # flag = True
        # if not flag:
            # break
    return arr
```

### 6. C++ 代码实现

```c++
// swap
void swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}
// array
void BubbleSort(int *p, int length) {
    for (int i = 0; i < length-1; i++) {
        for (int j = 0; j < length-1-i; j++) {
            if (p[j] > p[j+1]) {
                swap(p[j], p[j+1]);
            }
        }
    }
}
// vector
void BubbleSort(vector<int>& nums){
    int n = nums.size();
    for (int i = 0; i < n-1; i++){
        for (int j = 0; j < n-1-i; j++){
            if (nums[j] > nums[j+1]){
                swap(nums[j], nums[j+1]);
            }
        }
    }
}
```

## 选择排序

选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。


### 1. 算法步骤

1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置；
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾；
3. 重复第二步，直到所有元素均排序完毕。


### 2. 动图演示

![动图演示](https://raw.githubusercontent.com/hustcc/JS-Sorting-Algorithm/master/res/selectionSort.gif)


### 3. Python 代码实现

```python
def selectSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
```

### 4. C++ 代码实现

```c++
// array
void SelectSort(int *p, int length) {
    for (int i = 0; i < length-1; i++) {
        int min = i;      //记录最小值的下标，初始化为i
        for (int j = i+1; j < length; j++) {
            if (p[j] < p[min])
                min = j;  //通过不断地比较，得到最小值的下标
        }
        swap(p[i], p[min]);
    }
}
// vector
void SelectSort(vector<int> &nums){
    int n = nums.size();
    for (int i = 0; i < n-1; i++) {
        int min = i;
        for (int j = i+1; j < n; j++) {
            if (nums[j] < nums[min])
                min = j;
        }
        swap(nums[i], nums[min]);
    }
}
```

## 插入排序

插入排序是一种简单直观的排序算法，只要打过扑克牌的人都应该能够秒懂，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。


### 1. 算法步骤

1. 将待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）


### 2. 动图演示

![动图演示](https://raw.githubusercontent.com/hustcc/JS-Sorting-Algorithm/master/res/insertionSort.gif)


### 3. Python 代码实现

```python
def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```

### 4. C++ 代码实现

```c++
// array
void InsertSort(int *p, int length) {
    for (int i = 1; i < length; i++) {
        int key = p[i];
        for (int j = i-1; j >= 0 && p[j] > key; j--) {
            p[j+1] = p[j];
        }
        p[j+1] = key;
    }
}
// vector
void InsertSort(vector<int>& nums){
    int n = nums.size();
    //少于两个元素的数组不用排序
    if (n < 2) return;
    //排序从第二个元素进行考察
    for (int i = 1; i < n; i++) {
        int key = nums[i];
        int j = i-1;
        while (j >= 0 && nums[j] > key) {
            nums[j+1] = nums[j];
            j--;
        }
        nums[j+1] = key;
    }
}
```

## 希尔排序

希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。

希尔排序是基于插入排序的以下两点性质而提出改进方法的：

 - 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率；
 - 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位；

希尔排序的基本思想是：先将整个待排序的记录序列按下标的一定增量分组，分别对每组进行直接插入排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个序列为一组（待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序）。


### 1. 算法步骤

1. 选择一个增量序列 $t_1，t_2，\cdots，t_k$，其中 $t_i > t_j$, 对于 $i < j$ ; $t_k = 1$；
2. 按增量序列个数 k，对序列进行 k 趟排序；
3. 每趟排序，根据对应的增量 $t_i$，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。


### 2. Python 代码实现

```python
def shellSort(arr):
    gap = 1
    while (gap < len(arr) / 3):
        gap = gap * 3 + 1
    while gap > 0:	# python 不支持 do...while..., 可用 while 和 break 结合代替
        for i in range(gap, len(arr)):
            key = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > key:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = key
        gap = gap // 3  # 必定会取到 1
    return arr
```

### 3. C++ 代码实现

```c++
// array
void ShellSort(int *p, int length) {
    int increment = length;
    do {
         increment = increment / 3 +1;
         for (int i = increment ; i < length; i++) {
              int key = p[i];
              for (int j = i - increment; j >= 0 && p[j] > key; j -= increment)
                  p[j + increment] = p[j];
              p[j + increment] = key;
          }
    } while (increment > 1);
}
// vector
void ShellSort(vector<int> & nums) {
    int n = nums.size();
    int  d = n / 3 + 1;
    while (1) {
    //对每组进行直接插入排序
        for (int i = d; i < n; ++i){
            int key = nums[i];
            for (int j = i - d; j >= 0 && nums[j] > key; j -= d){
                nums[j + d] = nums[j];
            }
            nums[j + d] = key;
        }
        if (d == 1) break;
        d = d / 3 + 1;
    }
}
```

## 归并排序

归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

作为一种典型的分而治之思想的算法应用，归并排序的实现有两种方法：
 - 自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
 - 自下而上的迭代；

和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是 O(nlogn) 的时间复杂度。代价是需要额外的内存空间。


### 1. 算法步骤

1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
4. 重复步骤 3 直到某一指针达到序列尾；
5. 将另一序列剩下的所有元素直接复制到合并序列尾。


### 2. 动图演示
![动图演示](https://raw.githubusercontent.com/hustcc/JS-Sorting-Algorithm/master/res/mergeSort.gif)


### 3. Python 代码实现

```python
def mergeSort(arr):
    if(len(arr) < 2):
        return arr
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0));
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));
    return result
```

### 4. C++ 代码实现

```c++
// array
void Merge(int* p, int left, int mid, int right){
    int k = right - left + 1;
    int* tmpArray = new int[k];
    int i = right, j = mid;
    while (i > mid && j >= left) {
        if (p[i] > p[j]){
            tmpArray[--k] = p[i--];
        }
        else{
            tmpArray[--k] = p[j--];
        }
    }
    while (i > mid){
        tmpArray[--k] = p[i--];
    }
    while (j >= left){
        tmpArray[--k] = p[j--];
    }

    k = right - left + 1;
    for (i = 0; i < k; i++) {
        p[left + i] = tmpArray[i];
    }
    delete [] tmpArray;
}
//折半法，即分治思想
void BiMerge(int* p, int left, int right){
    if (left < right){
        int mid = left + (right - left) / 2;
        BiMerge(p, left, mid);
        BiMerge(p, mid + 1, right);
        Merge(p, left, mid, right);
    }
}
void MergeSort(int* p, int length){
    BiMergeSort(p, 0, length - 1);
}
// vector
void Merge(vector<int>&nums, int left, int mid, int right){
    int k = right - left + 1;
    vector<int> tmpArray(k);
    int i = right, j = mid;
    while (i > mid && j >= left) {
        if (nums[i] > nums[j]){
            tmpArray[--k] = nums[i--];
        }
        else{
            tmpArray[--k] = nums[j--];
        }
    }
    while (i > mid){
        tmpArray[--k] = nums[i--];
    }
    while (j >= left){
        tmpArray[--k] = nums[j--];
    }

    k = right - left + 1;
    for (i = 0; i < k; i++) {
        nums[left + i] = tmpArray[i];
    }
}
//折半法，即分治思想
void BiMerge(vector<int>& nums, int left, int right){
    if (left < right){
        int mid = left + (right - left) / 2;
        BiMerge(nums, left, mid);
        BiMerge(nums, mid + 1, right);
        Merge(nums, left, mid, right);
    }
}
void MergeSort(vector<int>& nums){
    int n = nums.size();
    BiMergeSort(nums, 0, n - 1);
}
```

## 快速排序

在平均状况下，排序 n 个项目要 Ο(nlogn) 次比较。在最坏状况下则需要 Ο(n²) 次比较，但这种状况并不常见。事实上，快速排序通常明显比其他 Ο(nlogn) 算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地被实现出来。

快速排序使用分治法（Divide and conquer）策略来把一个串（list）分为两个子串（sub-lists）。

快速排序又是一种分而治之思想在排序算法上的典型应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。

快速排序的名字起的是简单粗暴，因为一听到这个名字你就知道它存在的意义，就是快，而且效率高！它是处理大数据最快的排序算法之一了。虽然 Worst Case 的时间复杂度达到了 O(n²)，但是在大多数情况下都比平均时间复杂度为 O(n logn) 的排序算法表现要更好。

> 《算法艺术与信息学竞赛》：快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 记号中隐含的常数因子很小，比复杂度稳定等于 O(nlogn) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。


### 1. 算法步骤

1. 从数列中挑出一个元素，称为 “基准”（pivot）;
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；

递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总会退出，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。


### 2. 动图演示

![动图演示](https://raw.githubusercontent.com/hustcc/JS-Sorting-Algorithm/master/res/quickSort.gif)


### 3. Python 代码实现

```python
def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = arr[right]	# 基准值设为最右(也可设为最左, 下标相应修改)
    # 设置两个指针 i, j
    i = left
    for j in range(left, right) # 遍历下标由 left 到 right-1 的数
        if arr[j] < arr[pivot]:	# 如果 arr[j] 小于 基准值, 则交换 i, j 位置
            arr[j], arr[i] = arr[i], arr[j]
            i += 1	# i 右移一个位置
    arr[pivot], arr[i] = arr[i], arr[pivot]
    return i
```

### 4. C++ 代码实现

```c++
// 严蔚敏《数据结构》标准分割函数
Paritition1(int A[], int low, int high) {
    int pivot = A[low];	// 最左边元素设为基准值
    while (low < high) {
        // 一开始认为左侧位置是空的, 从后往前找到小于基准值的数来填充它
        while (low < high && A[high] >= pivot) {
            --high;
        }
    	A[low] = A[high];
        // 从前往后找到大于基准值的数来填充右侧位置
        while (low < high && A[low] <= pivot) {
            ++low;
        }
        A[high] = A[low];
    }
    A[low] = pivot;	// 基准值放在中间位置
    return low;	// 返回基准值所在位置
}

void QuickSort(int A[], int low, int high) //快排母函数
{
    if (low < high) {
        int pivot = Paritition1(A, low, high);
        QuickSort(A, low, pivot - 1);
        QuickSort(A, pivot + 1, high);
    }
}
```

## 堆排序

堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆是一个近似完全二叉树的结构，并同时满足堆的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：

1. 大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
2. 小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；

堆排序的平均时间复杂度为 Ο(nlogn)。


### 1. 算法步骤

1. 创建一个堆 $H[0,1,...,n-1]$；
2. 把堆首（最大值）和堆尾互换；
3. 把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；
4. 重复步骤 2，直到堆的尺寸为 1。


### 2. 动图演示

![动图演示](https://raw.githubusercontent.com/hustcc/JS-Sorting-Algorithm/master/res/heapSort.gif)


### 3. Python 代码实现

```python
def buildMaxHeap(arr):
    for i in range(len(arr)//2-1, -1, -1):
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1	# 左子结点
    right = 2*i+2	# 右子结点
    largest = i
    # 取得父结点和两个子结点中的较大值
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arrLen -=1
        heapify(arr, 0)
    return arr
```

### 4. C++ 代码实现

```c++
//构造最大堆
void MaxHeapFixDown(int *p, int i, int length) {
    int j = 2 * i + 1;	// i 的左子结点
    int tmp = p[i];
    while (j < length) {
        if (j+1 < length && p[j] < p[j+1])	// 得到左右子结点中的较大值
            ++j;
        if (tmp > p[j])
            break;
        else {	// 若父结点小于该子结点, 则令父结点等于该子结点
            p[i] = p[j];
            i = j;
            j = 2 * i + 1;
        }
    }
    p[i] = tmp;	// 子结点填上原结点的值
}

//堆排序
void HeapSort(int *p, int length) {
    // 建初始堆
    for (int i = length / 2 - 1; i >= 0; i--) // 从最后一个结点的父结点开始遍历
        MaxHeapFixDown(p, i, length);
    // 堆排序
    for (int i = length - 1; i >= 1; i--) { // 从最后一个结点开始遍历
        swap(p[0], p[i]);	// 交换堆顶与当前堆的最后一个结点
        MaxHeapFixDown(p, 0, i); // 调整剩余元素成为一个新的堆(只需对堆顶进行操作)
    }
}
```

## 计数排序

计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

### 1. 动图演示

![动图演示](https://raw.githubusercontent.com/hustcc/JS-Sorting-Algorithm/master/res/countingSort.gif)


### 2. Python 代码实现

```python
def countingSort(arr, maxValue):
    bucketLen = maxValue + 1
    bucket = [0] * bucketLen
    sortedIndex = 0
    for i in range(len(arr)):
        bucket[arr[i]] += 1
    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return arr
```

### 3. C++ 代码实现

```c++
// array
void CountingSort(int* p, int length, int maxValue) {
    int* bucket = new int[maxValue+1] (); //每个元素初始化为0
    int sortedIndex = 0;
    for (int i = 0; i < length; i++)
        bucket[p[i]] ++;
    for (int i = 0; i < maxValue; i++)
        for (int j = 0; j < bucket[i]; j++)
            p[sortedIndex++] = i;
    delete [] bucket;
}
// vector
void CountingSort(vector<int>& nums, int maxValue) {
	//长度为 maxValue+1, 值初始化为 0 的 vector
    vector<int> bucket(maxValue+1, 0);
    int sortedIndex = 0;
    for (int i = 0; i < nums.size(); i++)
        bucket[nums[i]] ++;
    for (int i = 0; i <= maxValue; i++) {
        for (int j = 0; j < bucket[i]; j++)
            nums[sortedIndex++] = i;
    }
}
```

## 桶排序

桶排序的基本思想是将一个数据表分割成许多buckets，然后每个bucket各自排序，或用不同的排序算法，或者递归的使用bucket sort算法。桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：

1. 在额外空间充足的情况下，尽量增大桶的数量
2. 使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中

同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。

### 1. 算法步骤

1. 建立一堆 buckets；
2. 遍历原始数组，并将数据放入到各自的 buckets 当中；
3. 对非空的 buckets 进行排序；
4. 按照顺序遍历这些 buckets 并放回到原始数组中，即可构成排序后的数组。

### 2. 什么时候最快

当输入的数据可以均匀的分配到每一个桶中。

### 3. 什么时候最慢

当输入的数据被分配到了同一个桶中。


### 4. Python 代码实现

```python

```

### 5. C++ 代码实现

```c++

```