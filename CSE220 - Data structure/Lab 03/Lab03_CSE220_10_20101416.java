public class Tester {
    public static void main(String[] args) {

        System.out.println("-------------Task2-------------\n");

        System.out.println("---------Problem 01(a)---------");
        System.out.println("Execute a = new int[]{1, 2, 3, 4, 5}");
        int[] a = new int[]{1, 2, 3, 4, 5};
        System.out.println("Execute source = DoublyList(int[] a)");
        DoublyList source = new DoublyList(a);
        System.out.print("source.head.data = ");
        System.out.println(source.head.data);
        System.out.print("source.head.previous.data = ");
        System.out.println(source.head.previous.data);
        System.out.print("source.head.next.data = ");
        System.out.println(source.head.next.data);
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 02-----------");
        System.out.println("Execute a = new int[]{1, 2, 3, 4, 5}");
        a = new int[]{1, 2, 3, 4, 5};
        System.out.println("Execute source = DoublyList(int[] a)");
        source = new DoublyList(a);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute a = new int[]{1}");
        a = new int[]{1};
        System.out.println("Execute source = DoublyList(int[] a)");
        source = new DoublyList(a);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute source.remove(0)");
        source.remove(0);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 03-----------");
        System.out.println("Execute a = new int[]{1, 2, 3, 4, 5}");
        a = new int[]{1, 2, 3, 4, 5};
        System.out.println("Execute source = DoublyList(int[] a)");
        source = new DoublyList(a);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute source.insert(new Node(null, 7, null))");
        source.insert(new Node(null, 7, null));
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute source.insert(new Node(null, 3, null))");
        source.insert(new Node(null, 3, null));
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 04-----------");
        System.out.println("Execute a = new int[]{1, 2, 3, 4, 5}");
        a = new int[]{1, 2, 3, 4, 5};
        System.out.println("Execute source = DoublyList(int[] a)");
        source = new DoublyList(a);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute source.insert(7, 2)");
        source.insert(7, 2);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute source.insert(7, 2)");
        source.insert(7, 2);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 05-----------");
        System.out.println("Execute a = new int[]{1, 2, 3, 4, 5}");
        a = new int[]{1, 2, 3, 4, 5};
        System.out.println("Execute source = DoublyList(int[] a)");
        source = new DoublyList(a);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute source.remove(1) with exception block");
        try {
            source.remove(1);
        } catch (ArrayIndexOutOfBoundsException ae) {
            System.out.println("ArrayIndexOutOfBoundsException");
        }
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute source.insert(7) with exception block");
        try {
            source.remove(7);
        } catch (ArrayIndexOutOfBoundsException ae) {
            System.out.println("ArrayIndexOutOfBoundsException");
        }
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 06-----------");
        System.out.println("Execute a = new int[]{1, 2, 3, 4, 5}");
        a = new int[]{1, 2, 3, 4, 5};
        System.out.println("Execute source = DoublyList(int[] a)");
        source = new DoublyList(a);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute int returnedRemovedKey = source.removeKey(4)");
        int returnedRemovedKey = source.removeKey(4);
        System.out.print("returnedRemovedKey = ");
        System.out.println(returnedRemovedKey);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute int returnedRemovedKey = source.removeKey(9)");
        returnedRemovedKey = source.removeKey(9);
        System.out.print("returnedRemovedKey = ");
        System.out.println(returnedRemovedKey);
        System.out.println("Execute source.showList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

    }
}

class Node {
    int data;
    Node next;
    Node previous;
    public Node (Node previous, int data, Node next) {
        this.previous = previous;
        this.data = data;
        this.next = next;
    }
}

class DoublyList {
    Node head;

    public DoublyList (int [] a) {
        head = new Node(null, -1, null);
        Node n = head;

        outerLoop:
        for (int i = 0; i < a.length; ++i) {
            for (int j = 0; j < i; ++j) {
                if (a[i] == a[j]) {
                    continue outerLoop;
                }
            }
            n.next = new Node(n, a[i], null);
            n = n.next;
        }
        n.next = head;
        head.previous = n;
    }

    public void showList () {
        if (head == null || head.next == head) {
            System.out.println("Empty list");
        } else {
            System.out.print('[');
            for (Node n = head.next; n != head; n = n.next) {
                System.out.print(n.data);
                if (n.next != head) {
                    System.out.print(" -> ");
                }
            }
            System.out.println(']');
        }
    }

    public void insert (Node newElement) {
        Node n;
        for (n = head.next; n != head; n = n.next) {
            if (n.data == newElement.data) {
                return;
            }
        }
        Node tail = head.previous;
        tail.next = new Node(tail, newElement.data, head);
        head.previous = tail.next;
    }

    public void insert (int newElement, int index) {
        int currIndex = 0;
        for (Node n = head; n.next != head; n = n.next, ++currIndex) {
            if (currIndex == index) {
                if (n.next.data != newElement) {
                    n.next = new Node(n, newElement, n.next);
                    n.next.next.previous = n.next;
                }
                return;
            }
        }
        throw new ArrayIndexOutOfBoundsException();
    }

    public void remove (int index) {
        int currIndex = 0;
        for (Node n = head; n.next != head; n = n.next, ++currIndex) {
            if (currIndex == index) {
                Node delNode = n.next;
                n.next = n.next.next;
                n.next.previous = n;
                delNode.next = null;
                delNode.previous = null;
                return;
            }
        }
        throw new ArrayIndexOutOfBoundsException();
    }

    public int removeKey (int deleteKey) {
        for (Node n = head; n.next != head; n = n.next) {
            if (n.next.data == deleteKey) {
                Node delNode = n.next;
                n.next = n.next.next;
                n.next.previous = n;
                delNode.next = null;
                delNode.previous = null;
                return delNode.data;
            }
        }
        return -1;
    }
}