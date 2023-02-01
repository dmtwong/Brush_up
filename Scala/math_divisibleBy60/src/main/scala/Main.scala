//
// exist fail test case, revisit later
//

// Problem Description
//Given a large number represent in the form of an integer array A, where each element is a digit.
//You have to find whether there exists any permutation of the array A such that the number becomes divisible by 60.
//Return 1 if it exists, 0 otherwise.
//Problem Constraints
//1 <= |A| <= 105
//0 <= Ai <= 9
//Input Format
//The first argument is an integer array A.
//Output Format
//Return a single integer '1' if there exists a permutation, '0' otherwise.
//Example Input
//Input 1:
//A = [0, 6]
//Input 2:
//A = [2, 3]
//Example Output
//Output 1:
//1
//Output 2:
//0
//Example Explanation
//Explanation 1:
//We can rearrange the digits to form 60, which is divisible by 60.
//Explanation 2:
//
//There are only two possible permutations: [23, 32].
//Both of them are not divisible by 60.

object Main {
  def main(args: Array[String]): Unit = {
    def divisibleBy60(A: Array[Int]): Int = {
//      val str_A = A.toString

      val last_A = A.length - 1
      if (last_A == 0 && A(0) == 0){
        return 1
      }
      var str_A = "a"
      for (i <- 0 to last_A){
        str_A = str_A + A(0).toString
      }
      str_A = str_A.substring(1)
      var hasZero = false
      var hasZeroS = false
      var ixZero = 0
      var isEven  = false
      var int_ai = 0

      val secondLastA = str_A(last_A - 1)

      var result = 0
      for (i <- 0 to last_A by 1){
        int_ai = str_A(i).toInt
        if (hasZero == true){
          hasZeroS = true
        }
        if (int_ai == 0){
          hasZero = true
          ixZero = i
        }
        if (isEven == false && int_ai % 2 ==0 && i != ixZero){
          isEven = true
        }
        result += int_ai
      }
      if (hasZero || result % 3 != 0){
        return 0
      }
      if (isEven == false) {
        return 0
      }
      if (int_ai == 0 && secondLastA % 2 == 0){
        return 1
      }
      if (hasZeroS == true && int_ai == 0 && secondLastA % 2 != 0) {
        return 1
      }
      return 1
    }
    val A1 = Array(0, 6)
    val A2 = Array(2, 3)
    val A3 = Array(0)
    val A4 = Array(2, 0, 5, 1, 1)

    val resulta = divisibleBy60(A1)
    val resultb = divisibleBy60(A2)
    val resultc = divisibleBy60(A3)
    val resultd = divisibleBy60(A4) // fail case, 15120 is a counter example
    println(resulta, resultb, resultc, resultd)
    println("Hello world!")
  }
}

