// Self notes: passed but extra space is used as first approach have O(N^2) time complexity; need to think think whether it can be done better


//Given a singly linked list, modify the value of first half nodes such that :
//1st node’s new value = the last node’s value - first node’s current value
//2nd node’s new value = the second last node’s value - 2nd node’s current value,
//and so on …
//NOTE :
//If the length L of linked list is odd, then the first half implies at first floor(L/2) nodes. So, if L = 5, the first half refers to first 2 nodes.
//If the length L of linked list is even, then the first half implies at first L/2 nodes. So, if L = 4, the first half refers to first 2 nodes.
//Example :
//Given linked list 1 -> 2 -> 3 -> 4 -> 5,
//You should return 4 -> 2 -> 3 -> 4 -> 5
//as
//for first node, 5 - 1 = 4
//for second node, 4 - 2 = 2
//Try to solve the problem using constant extra space.

object Main {
  def main(args: Array[String]): Unit = {
    class ListNode(val xc: Int) {
      var value: Int = xc
      var next: ListNode = null
    }
      def subtract(A: ListNode): ListNode = {
        var count_len = 0
        var dummy_count = A

        val value_list: Array[Int] = Array()
        var value_list2 = value_list

        while (dummy_count != null){
          value_list2 = value_list2 ++ Array(dummy_count.value)
          count_len += 1
          dummy_count = dummy_count.next
        }
        if (count_len == 1){
          return A
        }
        val ix = count_len / 2 - 1
        var temp = A
        var result_head = new ListNode(-99)
        result_head.next = temp
        var i = 0
        var j = count_len - 1
//        println(value_list)
//        println(value_list(0))


        for (i <- 0 to ix by 1) {
//          println(i)

//          mirror_val = temp_mirror.value
          temp.value = value_list2(j) - value_list2(i)
          j -= 1
          temp = temp.next
          i
        }
//        for (i <- 0 to ix by 1){
////          println(i)
//          var mirror_val = A.value
//          var ix_mirror = i
//          var temp_mirror = temp
//          while (i + ix_mirror < count_len - 1){
//            temp_mirror = temp_mirror.next
//            ix_mirror += 1
//          }
//          mirror_val = temp_mirror.value
//          temp.value = mirror_val - temp.value
//          temp = temp.next
//          i
//        }
        result_head.next
      }
//
    val A1 = new ListNode(1)
    val A2 = new ListNode(2)
    val A3 = new ListNode(3)
    val A4 = new ListNode(4)
    val A5 = new ListNode(5)
    A1.next = A2
    A2.next = A3
    A3.next = A4
    A4.next = A5
    var temp2 = subtract(A1)
    while (temp2 != null) {
      println(temp2.value)
      temp2 = temp2.next
    }
  }
}