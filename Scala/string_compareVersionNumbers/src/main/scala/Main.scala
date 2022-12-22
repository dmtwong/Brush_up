//Compare two version numbers version1 and version2.
//  If version1 > version2 return 1,
//If version1 < version2 return -1,
//otherwise return 0.
//You may assume that the version strings are non-empty and contain only digits and the . character.
//  The . character does not represent a decimal point and is used to separate number sequences. For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
//
//Note: Here is an example of version numbers ordering:
//0.1 < 1.1 < 1.2 < 1.13 < 1.13.4

//Input Format
//  The first argument is a string A representing version1.
//  The first argument is a string B representing version2.
//  Output Format
//  Return an integer.
//  Example Input
//  A = "1.13"
//B = "1.13.4"
//Example Output
//  -1
//Example Explanation
//  Version1 = "1.13"
//Version2 = "1.13.4"
//Version1 < version2, hence return -1
object Main {
  def main(args: Array[String]): Unit = {
//    println("Hello.world!")
//    var A = "1.2.7.3.4"
//    var C = "1.3.9.3"
//    var B = "1.3.9.3.5"
//    val split_A = A.split('.')
//    val split_B = B.split('.')
//    val split_C = C.split('.')
//    for (i <- 0 to split_A.length - 1 by 1){
//      println(split_A(i).toInt)
//    }
//    val zip = split_A.zipAll(split_B, "", "")
//    val zip2 = split_A.zipAll(split_C, "", "")
//    val min_length = split_A.length.min(split_C.length)
//    println(min_length)
//    for (i <- 0 to zip.length - 1 by 1) {
//      println(zip(i))
//      println(zip2(i))
//    }
class Solution {
  def compareVersion(A: String, B: String): Int = {
    val split_A = A.split('.')
    val split_B = B.split('.')
    val n_loop = split_A.length.min(split_B.length)
    for (i <- 0 to n_loop-1 by 1){
      //          val cur_A = split_A(i).toInt
      //          val cur_B = split_B(i).toInt
      //          val cur_A = split_A(i).toLong
      //          val cur_B = split_B(i).toLong
      val cur_A = BigInt(split_A(i))
      val cur_B = BigInt(split_B(i))
      if (cur_A > cur_B){
        return 1
      }
      if (cur_B > cur_A){
        return -1
      }
    }
    if (split_A.length > split_B.length){
      if (split_A(split_A.length-1).toInt == 0){
        return 0
      }
      return 1
    }
    if (split_B.length > split_A.length) {
      if (split_B(split_B.length-1).toInt == 0){
        return 0
      }
      return -1
    }
    return 0
  }
}

//    var A = "1.2.7.3.4"
//    var C = "1.3.9.3"
//    var B = "1.3.9.3.5"
//    println(compareVersion(C, B))
//    println(compareVersion(B, C))
//    println(compareVersion(B, B))
//    println(compareVersion(A, B))
//    println(compareVersion(B, A))
//    println(compareVersion(A, C))
//    println(compareVersion(C, A))
//    var A2 = "4444371174137455"
//    var B2 = "5.168"
//    println(compareVersion(A2, B2))
//    var A3 = "444444444444444444444444"
//    var B3 = "4444444444444444444444444"
//    println(compareVersion(A3, B3))
//    var A4 = "1.0"
//    var B4 = "1"
//    println(compareVersion(A4, B4))
  }
}

// Suggested Solution:
//class Solution {
//  def compareVersion(A: String, B: String): Int  = {
//    val aa = A.split('.')
//    val bb = B.split('.')
//    val zip = aa.zipAll(bb, "", "")
//    for (t2 <- zip) {
//      val s1 = t2._1.dropWhile(ch => ch == '0')
//      val s2 = t2._2.dropWhile(ch => ch == '0')
//      if (!(s1.isEmpty && s2.isEmpty)) {
//        if (s1.length > s2.length) return 1
//        else if (s1.length < s2.length) return -1
//        else {
//          val v1 = s1.toLong
//          val v2 = s2.toLong
//          if (v1 > v2) return 1
//          else if (v1 < v2) return -1
//        }
//      }
//    }
//    0
//  }
//}

//int Solution::compareVersion(string A, string B) {
//    // Do not write main() function.
//    // Do not read input, instead use the arguments to the function.
//    // Do not print the output, instead return values as specified
//    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
//    int j, i;
//    for( i=0, j=0 ; i<A.size() || j<B.size() ; i++, j++){
//        unsigned long long num1 = 0, num2 = 0;
//        while(i < A.size() && A[i] != '.'){
//            num1 *= 10;
//            num1 += A[i] - '0';
//            i++;
//        }
//        while(j < B.size() && B[j] != '.'){
//            num2 *= 10;
//            num2 += B[j] - '0';
//            j++;
//        }
//        if(num1 > num2) return 1;
//        if(num1 < num2) return -1;
//    }
//    return 0;
//}

///**
// * @input A : String
// * @input B : String
// *
// * @Output Integer
// */
//
// import (
// "strings"
// "strconv"
//// "fmt"
// )
//
//func compareStrings(one, two string) int {
//    one = strings.Trim(one, " ")
//    two = strings.Trim(two, " ")
//
//    one = strings.TrimLeft(one, "0")
//    two = strings.TrimLeft(two, "0")
//
//    if len(one) > len(two) {
//        return 1
//    } else if len(one) < len(two) {
//        return -1
//    } else {
//	    strLen := len(one)
//     	for  i := 0; i < strLen; i++ {
//    		if string(one[i]) > string(two[i]) {
//    			return 1
//    		} else if string(one[i]) < string(two[i]) {
//    			return -1
//    		} else {
//    			continue
//    		}
//	    }
//    }
//    return 0
//}
//
//
//func compareVersion(A string , B string )  (int) {
//    aVersion := strings.Split(A, ".")
//    bVersion := strings.Split(B, ".")
//
//    i := 0
//    j := 0
//
//    for ;i < len(aVersion) && j < len(bVersion); {
//        aVersion[i] = strings.Trim(aVersion[i], "\r")
//        bVersion[j] = strings.Trim(bVersion[j], "\r")
//        //strconv.ParseInt("-42", 10, 64)
//        //first, _ := strconv.ParseInt(aVersion[i], 10, 64)
//        //second, _ := strconv.ParseInt(bVersion[j], 10, 64)
//        //fmt.Println(first, second)
//        res := compareStrings(aVersion[i], bVersion[j])
//        if res == 1 {
//            return 1
//        } else if res == -1 {
//            return -1
//        }
//
//        i++
//        j++
//    }
//
//
//    for ; i < len(aVersion);i++ {
//        aVersion[i] = strings.Trim(aVersion[i], "\r")
//        first, _ := strconv.ParseInt(aVersion[i], 10, 64)
//        //fmt.Println("i", aVersion[i], first)
//        if first == 0 {
//            continue
//        } else {
//            return 1
//        }
//    }
//
//    for ; j < len(bVersion);j++ {
//        //fmt.Println("j", aVersion[j])
//        bVersion[j] = strings.Trim(bVersion[j], "\r")
//        second, _ := strconv.ParseInt(bVersion[j], 10, 64)
//        if second == 0 {
//            continue
//        } else {
//            return -1
//        }
//    }
//
//    if i == len(aVersion) - 1 && j == len(bVersion) - 1 {
//        return 0
//    }
//
//    return 0
//
//}
//public class Solution {
//	public int compareVersion(String A, String B) {
//
//	    int l1 = A.length();
//        int l2 = B.length();
//        int l = l2;
//        if (l2 > l1) {
//            l = l1;
//        }
//        for (int i = 0; i < l; i++) {
//            if (A.charAt(i) == '.' && B.charAt(i) == '.') {
//                continue;
//            }
//            if (A.charAt(i) == '.' && B.charAt(i) != '.') {
//                return -1;
//            }
//            if (A.charAt(i) != '.' && B.charAt(i) == '.') {
//                return 1;
//            }
//            if (A.charAt(i) > B.charAt(i)) {
//                return 1;
//            }
//            if (B.charAt(i) > A.charAt(i)) {
//                return -1;
//            }
//        }
//        if (l1 > l2) {
//            return 1;
//        }
//        if (l2 > l1) {
//            return -1;
//        }
//        return 0;
//	}
//}

