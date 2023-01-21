//Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
//
//Example:
//
//Given [100, 4, 200, 1, 3, 2],
//
//The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
//
//Your algorithm should run in O(n) complexity.

object Main {
  def main(args: Array[String]): Unit = {
    def longestConsecutive(A: Array[Int]): Int = {
      var set_1 = Set(1)
      set_1 -= 1
      val n_A = A.length
      var result = 0

      for (i <- 0 to n_A - 1 by 1){
        set_1 += A(i)
      }
      var j = 0
      for (i <- 0 to n_A - 1 by 1){
        if (!(set_1.contains(A(i) - 1))){
          j = A(i)
          while(set_1.contains(j)){
            j += 1
          }
          result = result.max(j - A(i))
        }
      }
      result
  }
    var A1 = Array(100, 4, 200, 1, 3, 2)
    var A2 = Array(100, 4, 200, 1, 3, 2, 0)
    var A3 = Array(100, 4, 200, 1, 0)
    var A4 = Array(100, 4, 200, 1)
    println(longestConsecutive(A1))
    println(longestConsecutive(A2))
    println(longestConsecutive(A3))
    println(longestConsecutive(A4))
  }
}
