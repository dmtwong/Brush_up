//Problem Description
//Given an array A of N non-negative numbers and you are also given non-negative number B.
//You need to find the number of subarrays in A having sum less than B. We may assume that there is no overflow.
//Problem Constraints
//1 <= N <= 104
//1 <= A[i] <= 100
//1 <= B <= 108
//Input Format
//First argument is an integer array A.
//Second argument is an integer B.
//Output Format
//Return an integer denoting the number of subarrays in A having sum less than B.
//Example Input
//Input 1:

//Example Output
//Output 1: 4
//Output 2: 4
//Example Explanation
//Explanation 1:
//
// The subarrays with sum less than B are {2}, {5}, {6} and {2, 5},
//Explanation 2:
//
// The subarrays with sum less than B are {1}, {2}, {3} and {2, 3}

object Main {
  def main(args: Array[String]): Unit = {
    def solve(A: Array[Int], B: Int): Int = {
//      scala.util.Sorting.quickSort(A)
      var result = 0
//      var head_ix = 0
//      var tail_ix = 0
      val n_A = A.length
      var curSum = -99
      var j = 0
      for (i <- 0 to n_A-1 by 1){
        curSum = 0
        j = i
        while (j <= A.length - 1){
          if (curSum + A(j) < B){
            curSum += A(j)
            result += 1
            j += 1
          } else{
            j = n_A
          }
        }
      }
      result
    }
    var A1 = Array(2, 5, 6)
    val B1 = 10
    var A2 = Array(1, 11, 2, 3, 15)
    val B2 = 10
    println(solve(A1, B1))
    println(solve(A2, B2))
  }
}

//class Solution {
//    def solve(A: Array[Int], B: Int): Int  = {
//
//        val arr = A
//        val maxSum = B
//
//        var start = 0
//        var end = 0
//
//        var numSubArrays = 0
//        var currSum = arr(0)
//
//        while(start < arr.size && end < arr.size) {
//
//            if(currSum < maxSum) {
//                end = end + 1
//                if(end >= start) numSubArrays = numSubArrays + end - start
//                if (end < arr.size) currSum = currSum + arr(end)
//            } else {
//                currSum = currSum - arr(start)
//                start = start + 1
//            }
//        }
//
//        numSubArrays
//    }
//}

// int Solution::solve(vector<int> &A, int B) {
//    int n = A.size(), l = 0, r = 0, res = 0, sum = A[0];
//    while(l < n && r < n)
//    {
//        if(sum < B)
//        {
//            r++;
//            if(r >= l)
//                res += (r - l);
//            if(r < n)
//                sum += A[r];
//        }
//        else
//        {
//            sum -= A[l];
//            l++;
//        }
//    }
//    return res;
//}

///**
// * @input A : Integer array
// * @input B : Integer
// *
// * @Output Integer
// */
// import "fmt"
// const debug = false
//func solve(A []int , B int )  (int) {
//    currentSum, left, right, counts := 0, 0, 0, 0
//    for left <= right && right < len(A) {
//        if currentSum + A[right] < B {
//            counts+= (right-left)+1
//            currentSum += A[right]
//            right++
//        } else {
//            if debug {fmt.Println(left, right, currentSum, counts)}
//            if left == right {
//                left++
//                right++
//                currentSum = 0
//                continue
//            }
//
//            currentSum -= A[left]
//            left++
//        }
//    }
//
//    return counts
//}