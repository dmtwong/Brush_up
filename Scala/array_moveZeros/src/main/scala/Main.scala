object Main {


  def main(args: Array[String]): Unit = {
    def solve(A: Array[Int]): Array[Int] = {
      import scala.util.control.Breaks._
      // var cur = 0
      for (i <- 0 to A.length - 1 by 1) {
        //        println(A(i))
        if (i != A.length - 1) {
          if (A(i) == 0) {
            //          println(A(i), A(i+1))
            var j = 1
            if (A(i + j) != 0) {
              A(i) = A(i + j)
              A(i + j) = 0
            }
            else {
              var toLoop = true
              while (j < A.length - 1 - i & toLoop) {
                j += 1
                if (A(i + j) != 0) {
                  A(i) = A(i + j)
                  A(i + j) = 0
                  toLoop = false
                  j = 1
                }

              }
            }

          }
        }
      }
      A
    }
    var a1 = Array(1, 6, 1, 0, 9, 6, 2, 5, 6, 2, 10, 2, 0, 6)
    solve(a1)
    for (i <- 0 to a1.length - 1 by 1) {
      println(a1(i))
    }
  }

  // Suggested Solution
//  class Solution {
//    def solve(A: Array[Int]): Array[Int]  = {
//
//      var b = A
//      var nonZeroCount = 0
//
//      for (i <- 0 to b.size - 1){
//
//        if(b(i) != 0){
//          var temp = b(i)
//          b(i) = b(nonZeroCount)
//          b(nonZeroCount) = temp
//          nonZeroCount += 1
//        }
//      }
//
//      b
//    }
//  }
  // fastest
//  class Solution {
//    def solve(A: Array[Int]): Array[Int]  = {
//
//      val buffer = Array.fill(A.length)(0)
//      var idx = 0
//      A.foreach { v =>
//        if(v!=0){
//          buffer(idx) = v
//          idx = idx+1
//        }
//      }
//
//      buffer
//    }
//  }




}


//class Solution:
//# @param A : list of integers
//  # @return a list of integers
//def solve(self, A):
//  n=len(A)
//  i=0
//  while(n>0):
//    if(A[i]==0):
//      A.append(0)
//      del A[i]
//    else:
//      i += 1
//      n -= 1
//  return A

// GO:
///**
// * @input A : Integer array
// *
// * @Output Integer array.
// */
//func solve(A []int )  ([]int) {
//  zeroPointer, nonZeroPointer := 0, 0
//  for nonZeroPointer < len(A) {
//    A[zeroPointer], A[nonZeroPointer] = A[nonZeroPointer], A[zeroPointer]
//    for zeroPointer < len(A) && A[zeroPointer] != 0 {
//      zeroPointer++
//        nonZeroPointer = zeroPointer+1
//    }
//    for nonZeroPointer < len(A) && A[nonZeroPointer] == 0 {
//      nonZeroPointer++
//    }
//  }
//  return A
//}
