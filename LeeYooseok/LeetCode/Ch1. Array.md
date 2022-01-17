### Max Consecutive Ones

- Given a binary array nums, return the maximum number of consecutive 1's in the array.
- 이진수 배열 nums가 주어지면, 배열에서 연속 1의 최대 수를 반환합니다.

- Example
```python
Input : nums = [1,0,1,1,0,1]
Output : 2
```


**아이디어**
- 반복문 사용하여 1 개수 세기
    - 변수에 최대값 담아서 0 만났을때 비교


```python
def findMaxConsecutiveOnes(nums):
    ans = 0
    temp = 0
    for n in nums:
        if n == 1:
            temp += 1
            ans = max(ans, temp)
        else:
            temp = 0
        

    return ans

findMaxConsecutiveOnes([1,1,0,1,1,1])
```




    3



### Find Numbers with Even Number of Digits
- Given an array nums of integers, return how many of them contain an even number of digits.
- 주어진 정수 배열에 대해서, 길이가 짝수인 정수의 개수 반환

- Example
```python
Input : nums = [12,345,2,6,7896]
Output : 2
```


```python
def findNumbers(nums):
    ans = 0
    for n in nums:
        if len(str(n)) % 2 == 0:
            ans += 1
    
    return ans

findNumbers([12,345,2,6,7896])
```




    2



### Squares of a Sorted Array
- Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
- 주어진 오름차순 배열에 대해서, 각 수에 대한 제곱수 오름차순 배열을 반환해서

- Example
```python
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```


```python
def sortedSquares(nums):
    nums = list(map(abs, nums))
    nums.sort()
    nums = list(map(lambda x: x ** 2, nums))
    
    return nums

sortedSquares([-4,-1,0,3,10])
```




    [0, 1, 9, 16, 100]



### Duplicate Zeros

- Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
- 고정 길이 배열에 대해서, 0을 복제 시키고, 숫자를 오른쪽으로 이동시켜라
- Example
```python
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
```



```python
def duplicateZeros(arr):
    zeros = list()
    
    for i in arr:
        zeros.append(i)
        if i == 0:
            zeros.append(i)
    
    arr[:] = zeros[:len(arr)]
        
    return arr

duplicateZeros([1,0,2,3,0,4,5,0])
```




    [1, 0, 0, 2, 3, 0, 0, 4]



### Merge Sorted Array
- You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
- Merge nums1 and nums2 into a single array sorted in non-decreasing order.
- 오름차순으로 정렬된 두 배열을 합쳐서 오름차순으로 정렬하여라, m,n은 두 배열의 요소 개수 이다.
- Example

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

Output: [1,2,2,3,5,6]


```python
def merge(nums1, m, nums2, n):
    # nums1에서 비어있는 자리 수 빼기
    nums1[:] = nums1[:m]
    
    # merge sort 시행
    result = list()
    l=h=0
    while l < m and h < n:
        if nums1[l] < nums2[h]:
            result.append(nums1[l])
            l += 1
        else:
            result.append(nums2[h])
            h += 1
    result += nums1[l:]
    result += nums2[h:]
    
    nums1[:] = result
    return nums1

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
```




    [1, 2, 2, 3, 5, 6]




```python
merge([1],1,[],0)
```




    [1]



### Remove Element
- Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

- Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

- Return k after placing the final result in the first k slots of nums.

- Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

- 주어진 배열에 대해서, 숫자 val 를 제거하고 남은 숫자 개수를 반환

- Example
~~~python
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
    ~~~


```python
def removeElement(nums, val):
    while nums.count(val) != 0:
        nums.remove(val)
    return len(nums)
    
removeElement([3,2,2,3], 3)
```




    2




```python
removeElement([0,1,2,2,3,0,4,2], 2)
```




    5



### Remove Duplicates from Sorted Array
- Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

- Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

- Return k after placing the final result in the first k slots of nums.

- Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
- 주어진 오름차순 정수 배열에 대하여, 중복된 수를 제거하여라. 그 후, 배열 길이 반환
- Example
```python
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    ```


```python
def removeDuplicates(nums):
    nums[:] = list(set(nums))
    nums.sort()
    return len(nums)

removeDuplicates([0,0,1,1,1,2,2,3,3,4])
```




    5




```python
def removeDuplicates2(nums):
    result = list()
    
    for n in nums:
        if result.count(n) == 0:
            result.append(n)
        
    nums[:] = result
    return len(nums)

removeDuplicates2([0,0,1,1,1,2,2,3,3,4])
```




    5



### Check If N and Its Double Exist

- Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
- 주어진 정수 배열에 대해서, 다음과 같은 N, M이 있는지 확인 하여라 (N = 2 * M)

- Example
```python
Input: arr = [7,1,14,11]
Output: true
    ```


```python
def checkIfExist(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j] * 2 and i != j:
                return True
    
    return False

checkIfExist([7,1,14,11])
```




    True




```python
checkIfExist([-2, 0, 10, -19, 4, 6, -8])
```




    False




```python
checkIfExist([0,0])
```




    True



### Valid Mountain Array

- Given an array of integers arr, return true if and only if it is a valid mountain array.
- Recall that arr is a mountain array if and only if:
    - arr,length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that
        - arr[0] < arr[1] < ... < arr[i-1] < arr[i]
        - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

- 주어진 정수 배열에 대해서, mountain array인지 확인 하여라
- Example
```python
    Input : arr = [2,1]
    Output : false
```
        


```python
def validMountainArray(arr):
    max_num = max(arr)
    
    # 최대값이 2개 이상이 면 return False
    if arr.count(max_num) == 2:
        return False
    
    max_index = arr.index(max_num)
    
    if max_index == 0 or max_index == len(arr)-1:
        return False
    
    # 상승 확인
    for i in range(len(arr[:max_index])):
        if arr[i] >= arr[i+1]:
            return False
        
    # 하락 확인
    for i in range(len(arr[max_index:-1])):
        if arr[max_index+i] <= arr[max_index+i+1]:
            return False
        
    return True

validMountainArray([2,1])
```




    False



### Replace Elements with Greatest Element on Right Side

- Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

- After doing so, return the array.

- 주어진 배열에 대해서, 모든 요소를 해당 요소의 오른쪽 요소들 중 가장 큰 값으로 대체해라.
- 마지막 요소는 -1 로 대체해라.

```python
    Input : arr = [17,18,5,4,6,1]
    Output : [18,6,6,6,1,-1]
```


```python
def replaceElements(arr):
    for i in range(len(arr)-1):
        arr[i] = max(arr[i+1:])
        
    arr[-1] = -1
    
    return arr

replaceElements([17,18,5,4,6,1])
```




    [18, 6, 6, 6, 1, -1]



### Move Zeroes
- Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

- 주어진 정수 배열에 대해서, 배열의 모든 0을 마지막으로 옮겨라

- Example
```python
    Input : nums [0,1,0,3,12]
    Output : [1,3,12,0,0]
```


```python
def moveZeroes(nums):
    temp = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[temp] = nums[i]
            temp += 1
            
    for i in range(len(nums[temp:])):
        nums[temp+i] = 0 
        
    return nums
    
moveZeroes([0,1,0,3,12])
```




    [1, 3, 12, 0, 0]



### Sort Array By Parity

- Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

- Return any array that satisfies this condition.
- 주어진 정수 배열에 대해서, 모든 짝수 요소를 배열의 홀수 요소 앞으로 옮겨라
- Example
```python
    Input : nums = [3,1,2,4]
    Output : [2,4,3,1]
```


```python
def sortArrayByParity(nums):
    odds = list()
    evens = list()
    
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)
            
    evens.extend(odds)
    
    return evens

sortArrayByParity([3,1,2,4])
```




    [2, 4, 3, 1]



### Height Checker

- A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in **non-decreasing order** by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

- You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

- Return the number of indices where heights[i] != expected[i].

- 키 순으로 오름차순으로 정렬
- expected 리스트
    - expected[i] = i 번째 학생의 expected height 순서

- heights 리스트
    - heights[i] = i 번째 학생의 현재 키 순서
    
- 위 heights[i] != expected[i]인 숫자 개수 반환

- Example
```python
    Input : heights = [1,1,4,2,1,3]
    Output : 3
    Explanations:
        heights : [1,1,4,2,1,3]
        expected : [1,1,1,2,3,4]
        Indices 2, 4, and 5 do not match.
```


```python
def heightChecker(heights):
    expected = heights.copy()
    heights.sort()
    
    ans = 0
    
    for i in range(len(heights)):
        if expected[i] != heights[i]:
            ans += 1
            
    return ans

heightChecker([1,1,4,2,1,3])
```

    [1, 1, 4, 2, 1, 3]
    [1, 1, 1, 2, 3, 4]





    3



### Third Maximum Number

- Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
- 주어진 정수 배열에 대해서, 세번째로 큰 수를 반환해라.
- 만약 세번째 큰 수가 없을 시, 가장 큰 수를 반환해라.

- Example
```python
    Input: nums = [3,2,1]
    Output: 1
```


```python
def thirdMax(nums):
    nums.sort(reverse = True)
    
    max_num = nums[0]
    temp = 1
    
    for i in nums[1:]:
        if i < max_num:
            max_num = i
            temp += 1
            
        if temp == 3:
            return max_num
        
    return nums[0]
        
thirdMax([3,2,1])
```




    1



### Find All Numbers Disappeared in an Array

- Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

- 주어진 n개의 [1,n] 범위내의 정수 배열에 대해서, [1,n] 범위 에서 없는 수들의 배열을 반환 해라

- Example
```python
    Input : nums = [4,3,2,7,8,2,3,1]
    Output : [5,6]
```


```python
def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])
        
        print(nums)
            
    return [i + 1 for i, num in enumerate(nums) if num > 0]

findDisappearedNumbers([4,3,2,7,8,2,3,1])
```

    [4, 3, 2, -7, 8, 2, 3, 1]
    [4, 3, -2, -7, 8, 2, 3, 1]
    [4, -3, -2, -7, 8, 2, 3, 1]
    [4, -3, -2, -7, 8, 2, -3, 1]
    [4, -3, -2, -7, 8, 2, -3, -1]
    [4, -3, -2, -7, 8, 2, -3, -1]
    [4, -3, -2, -7, 8, 2, -3, -1]
    [-4, -3, -2, -7, 8, 2, -3, -1]





    [5, 6]


