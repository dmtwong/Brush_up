object Main {
  def main(args: Array[String]): Unit = {
//    var ix_list:List[Int] = List()
//    List(1,2,3) ::: List(1)
////    List(ix_list) :+ 7
//    for (i <- 0 to 2 by 1) {
//      ix_list = ix_list :+ i
//      println(List(1,2,3) ::: List(1))
//      println(ix_list)

    }
    //  def count_ass(str_A):
    //    vowel_ix, len_str_A = find_vowel(str_A)
    //
    //    result = 0
    //    for i in range(len(vowel_ix)):
    //      result += (len_str_A - vowel_ix[i])
    //    return result
    def solve(A: String): Int = {
      def findVowel(str_A: String): List[Int] = {
        var ix_list:List[Int] = List()
        for (i <- 0 to str_A.length - 1 by 1){
          if ("AEIOUaeiou" contains str_A(i)){
            ix_list = ix_list :+ i
          }
        }
        return ix_list
      }
      def countVowel(A: String): Int = {
        var ix_list = findVowel(A)
        val n_str_A = A.length
        var result = 0
        for (i <- 0 to ix_list.length - 1 by 1){
          result += (n_str_A - ix_list(i))
        }
        return result
      }
      return countVowel(A) % 10003

    }

  val A = "ABEC"
  println(solve(A))

}
//class Solution {
//    def solve(A: String): Int  = {
//        if (A.length == 0) return 0
//
//        val set = Set('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
//        def isVowel(c: Char) = set.contains(c)
//
//        val result = (0 until A.length).foldLeft(0) { case (acc, idx) =>
//            if (isVowel(A(idx))) acc + (A.length - idx) else acc
//        }
//
//        result % 10003
//    }
//}
//class Solution {
//  def solve(A: String): Int  = {
//
//    var count = 0
//    for(i <- 0 until A.length) {
//      val c = A.charAt(i).toLower
//      if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
//        count += A.length - i
//      }
//    }
//    return count % 10003
//  }
//}
//int Solution::solve(string A) {
//    int length= A.size();
//    int sum=0;
//    for(int i=0;i<length;i++){
//        if(A[i]=='a'||A[i]=='e'||A[i]=='i'||A[i]=='o'||A[i]=='u'||A[i]=='A'||A[i]=='E'||A[i]=='I'||A[i]=='O'||A[i]=='U') sum+= length-i;
//    }
//    return (sum%10003);
//}
///**
// * @input A : String
// *
// * @Output Integer
// */
//
//func isVowel(c byte) bool {
//    if c >= 'A' && c <= 'Z' {
//        c += byte(32)
//    }
//    if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
//        return true
//    }
//    return false
//}
//
//func solve(A string )  (int) {
//    ans := 0
//    for i := 0; i < len(A); i++ {
//        if isVowel(A[i]) {
//            ans += (len(A) - i) % 10003
//        }
//    }
//    return ans%10003
//}