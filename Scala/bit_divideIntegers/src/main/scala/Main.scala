// Problem Description
//
//Divide two integers A and B, without using multiplication, division, and mod operator.
//Return the floor of the result of the division.
//Also, consider if there can be overflow cases. For overflow cases, return INT_MAX.
//Note: INT_MAX = 2^31 - 1
//
//Problem Constraints
//INT_MIN <= A, B <= INT_MAX
//B != 0
//
//
//Input Format
//The first argument is an integer A.
//The second argument is an integer B.
//
//
//Output Format
//Return an integer equal to A / B.
//
//Example Input
//A = 5
//B = 2
//
//Example Output
//2
//
//
//Example Explanation
//A = 5, B = 2, therefore A / B = 5 / 2 = 2.5
//Taking the floor value of 2.5 is 2
object Main {
  def main(args: Array[String]): Unit = {
    def divide(A: Int, B: Int): Int = {
      import scala.math.pow
      import java.lang.Math.addExact
      val INT_MAX = (pow(2,31) - 1).toInt
      var isPositive = 1
      if ((A < 0) ^ (B < 0)) // only negative if xor is true
        isPositive = -1

//      var isOverflow = false
      var abs_A = BigInt(A).abs
      var dynamic_A = abs_A

      var abs_B = BigInt(B).abs
//      println(A, B, abs_A, abs_B)
//      if (abs_A > INT_MAX){
//        abs_A = INT_MAX
//      }
      var result = BigInt(0)
      if (dynamic_A < abs_B){
        return 0
      }
      while (dynamic_A >= abs_B && (abs_B > 1) ){
        dynamic_A -= abs_B
        result += 1
      }
//      println(dynamic_A, A, B, abs_A, abs_B, result, dynamic_A == abs_A)

      if ((result == 0)) {
//        println("!!")
        if (isPositive == -1) {
          result = -abs_A
//          println("yes", result)
        } else {
          result = abs_A
        }

        if (result > BigInt(INT_MAX)) { // should be false unless overflow
//          println("here", result)
          return INT_MAX
        } else {
//          println("there", result)
          return result.toInt
        }

      }
      // result = isPositive * result
      if (isPositive == -1){
        result = -result
      }
      result.toInt
    }
    val A1 = 5
    val B1 = 2
    val A2 = -1
    val B2 = 1
    val A3 = -2147483648
    val B3 = -1
    println(divide(A1, B1))
    println(divide(A2, B2))
    println(divide(A3, B3))
    println(divide(A3, B2))
  }

}// Editorial
//class Solution {
//    def divide(A: Int, B: Int): Int = {
//        val positive = if ((A < 0 && B > 0) || (A > 0 && B < 0)) false else true
//         val d  = if (A == Int.MinValue) {
//          if (B == - 1) Int.MaxValue
//          else if (B < 0 ) dividePositive(Math.abs(A - B), Math.abs(B)) + 1
//          else if (B == 1) Int.MinValue
//          else dividePositive(Math.abs(A + B), Math.abs(B))
//        } else dividePositive(Math.abs(A), Math.abs(B))
//        if (positive) d else 0 - d
//    }
//
//    def dividePositive(A: Int, B: Int): Int = {
//        if (A == B) 1
//        else if (A < B) 0
//        else if (B == 1) A
//        else {
//
//          var l = 0
//          var b = B
//          while (b != 0) {
//            l += 1
//            b >>= 1
//          }
//
//          var g = B
//          var pow = 0
//          while (g << 1 < A && pow < 31 - l) {
//            g <<= 1
//            pow += 1
//          }
//
//          var a = A
//          var s = 0
//          while (pow > -1) {
//            val c = B << pow
//            if (c <= a) {
//              a -= c
//              s += 1 << pow
//            }
//            pow -= 1
//          }
//          s
//        }
//
//  }
//
//}

//int Solution::divide(int dividend, int divisor) {
//    long long n = dividend, m = divisor;
//    // determine sign of the quotient
//    int sign = n < 0 ^ m < 0 ? -1 : 1;
//
//    // remove sign of operands
//    n = abs(n), m = abs(m);
//
//    // q stores the quotient in computation
//    long long q = 0;
//
//    // test down from the highest bit
//    // accumulate the tentative value for valid bits
//    for (long long t = 0, i = 31; i >= 0; i--)
//        if (t + (m << i) <= n)
//            t += m << i, q |= 1LL << i;
//
//    // assign back the sign
//    if (sign < 0) q = -q;
//
//    // check for overflow and return
//        return q >= INT_MAX || q < INT_MIN ? INT_MAX : q;
//}
//
///**
// * @input A : Integer
// * @input B : Integer
// *
// * @Output Integer
// */
//
// import (
// "math")
//
//func divide(x, y int) int {
//	if y == 0 {
//		return math.MaxInt32
//	}
//	signed := false
//	if x < 0 && y > 0 {
//		x = -x
//		signed = true
//	}
//	if x > 0 && y < 0 {
//		y = -y
//		signed = true
//	}
//	if x < 0 && y < 0 {
//		x = -x
//		y = -y
//	}
//
//	answer := 0
//	calc := 1
//	for x > 0 {
//		for y > x {
//			y = y >> 1
//			calc = calc >> 1
//		}
//		x -= y
//		answer += calc
//		y = y << 1
//		calc = calc << 1
//	}
//	if answer > math.MaxInt32 && !signed {
//		answer = math.MaxInt32
//	}
//	if signed {
//		return -answer
//	}
//	return answer
//}
//class Solution:
//    # @param A : integer
//    # @param B : integer
//    # @return an integer
//    def divide(self, dividend, divisor):
//        INT_MAX = 2**31 - 1
//        INT_MIN = -2**31
//        res = 0
//        p = abs(dividend)
//        q = abs(divisor)
//        if divisor == 0 or (divisor == 1 and dividend >= INT_MAX) :
//            return INT_MAX
//        if dividend <= INT_MIN and divisor == -1 :
//            return INT_MAX
//        if abs(divisor) == 1 :
//            return dividend * divisor
//        while p >= q :
//            c = 0
//            while p > (q << c) :
//                c += 1
//            res += 1 << (c -1)
//            p -= q << (c - 1)
//
//        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) :
//            return res
//        else :
//            return -res