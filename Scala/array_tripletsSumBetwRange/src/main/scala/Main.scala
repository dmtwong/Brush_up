

object Main {
  def main(args: Array[String]): Unit = {
    def solve(A: Array[String]): Int = {
      val A2 = A.map(_.toFloat).sorted

      def sumTriplet(left: Int, right: Int): Int = {
        if (left >= right - 1) {
          0
        } else {
          var first = A2(left)
          var second = A2(left + 1)
          var third = A2(right)
          var movingSum = first + second + third
          if (movingSum >= 2) {
            sumTriplet(left, right - 1)
          } else if (movingSum <= 1) {
            sumTriplet(left + 1, right)
          }
          else 1
        }
      }

      sumTriplet(0, A2.length - 1)
    }
    // Suggested Solution
//class Solution {
//    def solve(as: Array[String]): Int  = {
//      var Acnt, Bcnt, Ccnt = 0
//      var Amin1, Amin2, Bmin1, Bmin2, Cmin1 = 3.0
//      var Amax1, Amax2, Amax3, Bmax1 = -1.0
//      def process(s: String): Unit = {
//        val d = s.toDouble
//        if (d > 0.0 && d < 2.0 / 3.0) {
//          Acnt += 1
//          if (d > Amax1) {
//            Amax3 = Amax2
//            Amax2 = Amax1
//            Amax1 = d
//          }
//          else if (d > Amax2) {
//            Amax3 = Amax2
//            Amax2 = d
//          }
//          else if (d > Amax3) {
//            Amax3 = d
//          }
//          if (d < Amin1) {
//            Amin2 = Amin1
//            Amin1 = d
//          }
//          else if (d < Amin2) {
//            Amin2 = d
//          }
//        }
//        else if (d >= 2.0 / 3.0 && d <= 1.0) {
//          Bcnt += 1
//          if (d > Bmax1) {
//            Bmax1 = d
//          }
//          if (d < Bmin1) {
//            Bmin2 = Bmin1
//            Bmin1 = d
//          }
//          else if (d < Bmin2) {
//            Bmin2 = d
//          }
//        }
//        else if (d > 1.0 && d < 2.0) {
//          Ccnt += 1
//          if (d < Cmin1) {
//            Cmin1 = d
//          }
//        }
//      }
//      var i = 0
//      while (i < as.length) {
//        process(as(i))
//        i += 1
//      }
//      val t1 = Acnt > 2 && Amax1 + Amax2 + Amax3 >= 1.0
//      val t2a = Acnt > 1 && Bcnt > 0 && Amax1 + Amax2 + Bmin1 < 2.0 && Amax1 + Amax2 + Bmin1 > 1.0
//      val t2b = Acnt > 1 && Bcnt > 0 && Amin1 + Amin2 + Bmax1 > 1.0 && Amin1 + Amin2 + Bmax1 <= 2.0
//      val t3 = Acnt > 1 && Ccnt > 0 && Amin1 + Amin2 + Cmin1 <= 2.0
//      val t4 = Acnt > 0 && Bcnt > 1 && Amin1 + Bmin1 + Bmin2 <= 2.0
//      val t5 = Acnt > 0 && Bcnt > 0 && Ccnt > 0 && Amin1 + Bmin1 + Cmin1 <= 2.0
//      if (t1 || t2a || t2b || t3 || t4 || t5) 1 else 0
//    }
//}

    var a1 = Array("0.6", "0.7", "0.8", "1.2", "0.4")
    for (i <- 0 to a1.length - 1 by 1) {
      println(solve(a1))
    }
  }
}