//Merge two sorted linked lists and return it as a new list.
//
//The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
//
//For example, given following linked lists :
//
//  5 -> 8 -> 20
//  4 -> 11 -> 15
//The merged list should be :
//
//4 -> 5 -> 8 -> 11 -> 15 -> 20
object Main {
  def main(args: Array[String]): Unit = {
    class ListNode(val xc: Int) {
      var value: Int = xc
      var next: ListNode = null
    }
    def mergeTwoLists(A: ListNode, B: ListNode): ListNode = {
      //      val head_A = new ListNode(-99)
      //      val head_B = new ListNode(-99)
      val head_result = new ListNode(-99)
      //      head_A.next = A
      //      head_B.next = B
      var current = A
      var current_b = B
      var current_result = new ListNode(-99)
      head_result.next = current_result
      while ((current != null) && (current_b != null)) {
        var val_a = current.value
        var val_b = current_b.value
        if (val_a <= val_b) {
          current_result.next = current
          current_result = current
          current = current.next
        } else {
          current_result.next = current_b
          current_result = current_b
          current_b = current_b.next
        }
      }
      while (current != null) {
        var val_a = current.value
        current_result.next = current
        current_result = current
        current = current.next
      }
      while (current_b != null) {
        var val_b = current_b.value
        current_result.next = current_b
        current_result = current_b
        current_b = current_b.next
      }
      current_result.next = null
      head_result.next.next
    }
    val A1 = new ListNode(5)
    val A2 = new ListNode(8)
    val A3 = new ListNode(20)
    val B1 = new ListNode(4)
    val B2 = new ListNode(11)
    val B3 = new ListNode(15)
    A1.next = A2
    A2.next = A3
    B1.next = B2
    B2.next = B3
    //  5 -> 8 -> 20
    //  4 -> 11 -> 15
//    println(mergeTwoLists(A1, B1))
//    println(mergeTwoLists(A1, B1).value)
    var temp = mergeTwoLists(A1, B1)
    while (temp != null){
      println(temp.value)
      temp = temp.next
    }
  }
}
// Editorial
// // Definition for singly-linked list.
////    function Node(data){
////         this.data = data
////         this.next = null
////}
//
//module.exports = {
//    //param a : head node of linked list
//    //param b : head node of linked list
//    //return the head node in the linked list
//	mergeTwoLists : function(a, b){
//	    var result = new Node(1);
//        var head = result;
//        while (a != null && b != null) {
//            if (a.data >= b.data) {
//                var nextB = b.next;
//                result.next = b;
//                b.next = null;
//                b = nextB;
//            } else {
//                var nextA = a.next;
//                result.next = a;
//                a.next = null;
//                a = nextA;
//
//            }
//            result = result.next;
//        }
//        if (a != null) result.next = a;
//        if (b != null) result.next = b;
//        return head.next;
//	}
//};
// /**
// * Definition for singly-linked list.
// * struct ListNode {
// *     int val;
// *     ListNode *next;
// *     ListNode(int x) : val(x), next(NULL) {}
// * };
// */
//ListNode* Solution::mergeTwoLists(ListNode* A, ListNode* B) {
//    ListNode *ret, *temp, *rettemp;
//    if (!A) {
//        return B;
//    }
//    if (!B) {
//        return A;
//    }
//    if (A->val <= B->val) {
//        ret = new ListNode(A->val);
//        A = A->next;
//    } else {
//        ret = new ListNode(B->val);
//        B = B->next;
//    }
//
//    temp = ret;
//    while (A&&B) {
//        if (A->val <= B->val) {
//            temp->next = new ListNode(A->val);
//            A = A->next;
//        } else {
//            temp->next = new ListNode(B->val);
//            B = B->next;
//        }
//        temp = temp->next;
//    }
//    while (A) {
//        temp->next = new ListNode(A->val);
//        A = A->next;
//        temp = temp->next;
//    }
//    while (B) {
//        temp->next = new ListNode(B->val);
//        B = B->next;
//        temp = temp->next;
//    }
//
//    return ret;
//}
// GO
///**
// * Definition for singly-linked list.
// * type listNode struct {
// *     value int
// *     next *listNode
// * }
// *
// * func listNode_new(val int) *listNode{
// *     var node *listNode = new(listNode)
// *     node.value = val
// *     node.next = nil
// *     return node
// * }
// */
///**
// * @input A : Head pointer of linked list
// * @input B : Head pointer of linked list
// *
// * @Output head pointer of list.
// */
//func mergeTwoLists(A *listNode , B *listNode )  (*listNode) {
//    ha, hb := A, B
//    var h, curr *listNode
//    for ha!=nil && hb!=nil {
//        if ha.value<hb.value {
//            if h==nil {
//                h=A
//                curr=A
//            } else {
//                curr.next=ha
//                curr=curr.next
//            }
//            ha=ha.next
//        } else {
//            if h==nil {
//                h=B
//                curr=B
//            } else {
//                curr.next=hb
//                curr=curr.next
//            }
//            hb=hb.next
//        }
//    }
//    if ha!=nil {
//        if h==nil {
//            h=ha
//        } else {
//            curr.next=ha
//        }
//    }
//    if hb!=nil {
//        if h==nil {
//            h=hb
//        } else {
//            curr.next=hb
//        }
//    }
//    return h
//}
// # Definition for singly-linked list.
//# class ListNode:
//#    def __init__(self, x):
//#        self.val = x
//#        self.next = None
//
//class Solution:
//    # @param A : head node of linked list
//    # @param B : head node of linked list
//    # @return the head node in the linked list
//    def mergeTwoLists(self, a, b):
//        if a.val > b.val:
//            a, b = b, a
//
//        h = a
//
//        while a.next and b:
//            if a.next.val < b.val:
//                a = a.next
//            else:
//                a.next, b.next, a, b = b, a.next, b, b.next
//
//        if b:
//            a.next = b
//
//        return h
//
//