//Problem Description
//Given an array of integers A, every element appears twice except for one. Find that single one.
//NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
//Problem Constraints
//  1 <= |A| <= 2000000
//0 <= A[i] <= INTMAX
//
//Input Format
//  First and only argument of input contains an integer array A.
//
//  Output Format
//  Return a single integer denoting the single element.
//Example Input
//  Input 1:
//
//Input 2:
//
//
//Example Output
//  Output 1:
//
//  3
//Output 2:
//
//  1

object Main {
  def main(args: Array[String]): Unit = {
    def singleNumber(A: Array[Int]): Int = {
      var result = 0
      for (i <- 0 to A.length - 1 by 1) {
        result ^= A(i)
      }
      result
    }

    var A1 = Array(1, 2, 2, 3, 1)
    var A2 = Array(1, 2, 2)
    println(singleNumber(A1))
    println(singleNumber(A2))

  }
}

//class Solution {
//    def singleNumber(A: Array[Int]): Int  = {
//        var res = 0
//        A.foreach(ai => res = res ^ ai)
//        res
//    }
//}
//int Solution::singleNumber(const vector<int> &A) {
//
//       int n = A.size();
//       int result = 0;
//       for (int i = 0; i < n; i++) {
//	       result ^= A[i];
//       }
//       return result;
//
//}
///**
// * @input A : Integer array
// *
// * @Output Integer
// */
//func singleNumber(numbers []int) (int) {
//	number := 0
//	for i := 0; i < len(numbers); i++ {
//		number ^= numbers[i]
//	}
//
//	return number
//}
//class Solution:
//    # @param A : tuple of integers
//    # @return an integer
//    def singleNumber(self, A):
//        from scipy import stats
//    print(stats.bernoulli.rvs(size=10,p=0.3))