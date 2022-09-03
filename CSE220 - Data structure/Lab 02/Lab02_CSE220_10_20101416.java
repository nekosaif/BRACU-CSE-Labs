public class Tester {
    public static void main(String[] args) {

        System.out.println("-------------Task2-------------\n");

        System.out.println("---------Problem 01(a)---------");
        MyList source = new MyList();
        System.out.println("Execute source = MyList()");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

        System.out.println("---------Problem 01(b)---------");
        int[] a = new int[]{1, 2, 3, 4, 5};
        System.out.println("Execute a = new int[]{1, 2, 3, 4, 5}");
        source = new MyList(a);
        System.out.println("source = Execute MyList(int[] a)");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

        System.out.println("---------Problem 01(c)---------");
        source = new MyList(new int[]{1, 2, 3, 4, 5});
        System.out.println("Execute source = MyList(int[]{1, 2, 3, 4, 5})");
        System.out.print("source = ");
        source.showList();
        MyList newSource = new MyList(source);
        System.out.println("Execute newSource = MyList(MyList source)");
        System.out.print("newSource = ");
        newSource.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 02-----------");
        source = new MyList(new int[]{1, 2, 3, 4, 5});
        System.out.println("Execute source = MyList(int[]{1, 2, 3, 4, 5})");
        System.out.println("Execute source.showList()");
        System.out.print("Output = ");
        source.showList();
        newSource = new MyList();
        System.out.println("Execute newSource = MyList()");
        System.out.println("Execute newSource.showList()");
        System.out.print("Output = ");
        newSource.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 03-----------");
        source = new MyList(new int[]{1, 2, 3, 4, 5});
        System.out.println("Execute source = MyList(int[]{1, 2, 3, 4, 5})");
        System.out.print("source = ");
        source.showList();
        newSource = new MyList();
        System.out.println("Execute newSource = MyList()");
        System.out.print("newSource = ");
        newSource.showList();
        System.out.println("Execute source.isEmpty()");
        System.out.println("Output = " + source.isEmpty());
        System.out.println("Execute newSource.isEmpty()");
        System.out.println("Output = " + newSource.isEmpty());
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 04-----------");
        source = new MyList(new int[]{1, 2, 3, 4, 5});
        System.out.println("Execute source = MyList(int[]{1, 2, 3, 4, 5})");
        System.out.print("source = ");
        source.showList();
        newSource = new MyList();
        source.clear();
        System.out.println("Execute source.clear()");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 05-----------");
        source = new MyList();
        System.out.println("Execute source = MyList()");
        System.out.print("source = ");
        source.showList();
        newSource = new MyList(new int[]{1, 2, 3, 4, 5});
        System.out.println("Execute newSource = MyList(int[]{1, 2, 3, 4, 5})");
        System.out.print("newSource = ");
        newSource.showList();
        Node n = new Node(4, null);
        System.out.println("Execute n = new Node(10, null)");
        source.insert(n);
        System.out.println("Execute source.insert(n)");
        System.out.print("source = ");
        source.showList();
        newSource.insert(n);
        System.out.println("Execute newSource.insert(n)");
        System.out.print("newSource = ");
        newSource.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 06-----------");
        source = new MyList(new int[]{1, 2, 3, 4, 5});
        System.out.println("Execute source = MyList(int[]{1, 2, 3, 4, 5})");
        System.out.print("source = ");
        source.showList();
        source.insert(100, 3);
        System.out.println("Execute source.insert(100, 3)");
        System.out.print("source = ");
        source.showList();
        source.insert(4, 4);
        System.out.println("Execute source.insert(4, 4)");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 07-----------");
        source = new MyList(new int[]{1, 2, 3, 4, 5});
        System.out.println("Execute source = MyList(int[]{1, 2, 3, 4, 5})");
        System.out.print("source = ");
        source.showList();
        int removedData = source.remove(4);
        System.out.println("Execute removedData = source.remove(4)");
        System.out.println("removedData = " + removedData);
        System.out.print("source = ");
        source.showList();
        removedData = source.remove(10);
        System.out.println("Execute removedData = source.remove(10)");
        System.out.println("removedData = " + removedData);
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n\n\n");



        System.out.println("-------------Task3-------------\n");

        System.out.println("-----------Problem 01----------");
        source = new MyList(new int[]{1, 2, 5, 3, 8});
        System.out.println("Execute source = MyList(int[]{1, 2, 5, 3, 8})");
        System.out.print("source = ");
        source.showList();
        MyList evenList = source.evenNumberList();
        System.out.println("Execute evenList = source.evenNumberList()");
        System.out.print("evenList = ");
        evenList.showList();
        newSource = new MyList(new int[]{101, 120, 25, 91, 87, 1});
        System.out.println("Execute newSource = MyList(int[]{101, 120, 25, 91, 87, 1})");
        System.out.print("newSource = ");
        newSource.showList();
        MyList newEvenList = newSource.evenNumberList();
        System.out.println("Execute newEvenList = source.evenNumberList()");
        System.out.print("newEvenList = ");
        newEvenList.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 02----------");
        source = new MyList(new int[]{1, 2, 5, 3, 8});
        System.out.println("Execute source = MyList(int[]{1, 2, 5, 3, 8})");
        System.out.print("source = ");
        source.showList();
        System.out.println("Execute source.contains(7)");
        System.out.println("Output = " + source.contains(7));
        newSource = new MyList(new int[]{101, 120, 25, 91, 87, 1});
        System.out.println("Execute newSource = MyList(int[]{101, 120, 25, 91, 87, 1})");
        System.out.print("newSource = ");
        newSource.showList();
        System.out.println("Execute newSource.contains(87)");
        System.out.println("Output = " + newSource.contains(87));
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 03----------");
        source = new MyList(new int[]{1, 2, 5, 3, 8});
        System.out.println("Execute source = MyList(int[]{1, 2, 5, 3, 8})");
        System.out.print("source = ");
        source.showList();
        source.reverse();
        System.out.println("Execute source.reverse()");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 04----------");
        source = new MyList(new int[]{1, 2, 5, 3, 8});
        System.out.println("Execute source = MyList(int[]{1, 2, 5, 3, 8})");
        System.out.print("source = ");
        source.showList();
        source.sort();
        System.out.println("Execute source.sort()");
        System.out.print("source = ");
        source.showList();
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 05----------");
        source = new MyList(new int[]{1, 2, 5, 3, 8});
        System.out.println("Execute source = MyList(int[]{1, 2, 5, 3, 8})");
        System.out.print("source = ");
        source.showList();
        int sum = source.getSum();
        System.out.println("Execute sum = source.getSum()");
        System.out.println("sum = " + sum);
        System.out.println("-------------------------------\n");

        System.out.println("-----------Problem 06----------");
        source = new MyList(new int[]{3, 2, 5, 1, 8});
        System.out.println("Execute source = MyList(int[]{3, 2, 5, 1, 8})");
        System.out.print("source = ");
        source.showList();
        source.rotate("left", 2);
        System.out.println("Execute source.rotate(\"left\", 2)");
        System.out.print("source = ");
        source.showList();
        newSource = new MyList(new int[]{3, 2, 5, 1, 8});
        System.out.println("Execute newSource = MyList(int[]{3, 2, 5, 1, 8})");
        System.out.print("newSource = ");
        newSource.showList();
        newSource.rotate("right", 2);
        System.out.println("Execute newSource.rotate(\"right\", 2)");
        System.out.print("newSource = ");
        newSource.showList();
        System.out.println("-------------------------------\n");

    }
}

class Node {
    int data;
    Node next;

    Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }
}

class MyList {
    Node head;

    MyList() {

    }

    MyList(int[] a) {
        head = new Node(a[0], null);
        Node n = head;
        for (int i = 1; i < a.length; ++i) {
            n.next = new Node(a[i], null);
            n = n.next;
        }
    }

    MyList(MyList a) {
        this.head = new Node(a.head.data, null);
        Node an = a.head;
        Node n = this.head;
        while (an.next != null) {
            n.next = new Node(an.next.data, null);
            an = an.next;
            n = n.next;
        }
    }

    public void showList () {
        if (head != null) {
            System.out.print('[');
            Node n = head;
            while (n != null) {
                if (n.next != null) {
                    System.out.print(n.data + " -> ");
                } else {
                    System.out.print(n.data);
                }
                n = n.next;
            }
            System.out.println(']');
        } else {
            System.out.println("Empty list");
        }
    }

    public boolean isEmpty () {
        return head == null;
    }

    public void clear () {
        head = null;
    }

    public void insert (Node newElement) {
        if (head == null) {
            head = newElement;
        }
        Node n = head;
        while (n.next != null) {
            if (n.data == newElement.data) {
                return;
            }
            n = n.next;
        }
        if (n.data == newElement.data) {
            return;
        }
        n.next = new Node(newElement.data, null);
    }

    public void insert (int newElement, int index) {
        if (head.data == newElement) {
            return;
        }
        if (index == 0) {
            Node newHead = new Node(newElement, head);
            head = newHead;
            return;
        }
        Node n = head;
        int i = 1;
        while (n.next != null) {
            if (n.next.data == newElement) {
                return;
            }
            if (i == index) {
                Node insertedNode = new Node(newElement, n.next);
                n.next = insertedNode;
                return;
            }
            n = n.next;
            ++i;
        }
        throw new IndexOutOfBoundsException();
    }

    public int remove (int deleteKey) {
        Node n = head;
        if (head.data == deleteKey) {
            head = head.next;
            return n.data;
        }
        while (n.next != null) {
            if (n.next.data == deleteKey) {
                Node retNode = n.next;
                n.next = n.next.next;
                return retNode.data;
            }
            n = n.next;
        }
        return -1;
    }

    public MyList evenNumberList () {
        MyList retList = new MyList();
        Node n = head;
        Node retTail = null;
        while (n != null) {
            if ((n.data ^ 1) == n.data + 1) {
                if (retTail == null) {
                    retList.head = new Node(n.data, null);
                    retTail = retList.head;
                } else {
                    retTail.next = new Node(n.data, null);
                    retTail = retTail.next;
                }
            }
            n = n.next;
        }
        return retList;
    }

    public boolean contains (int target) {
        Node n = head;
        while (n != null) {
            if (n.data == target) {
                return true;
            }
            n = n.next;
        }
        return false;
    }

    public void reverse () {
        if (head == null || head.next == null) {
            return;
        }
        Node newHead = null;
        Node n = head;
        while (n != null) {
            Node nextNode = n.next;
            n.next = newHead;
            newHead = n;
            n = nextNode;
        }
        head = newHead;
    }

    public void sort () {
        Node n1 = head;
        while (n1 != null) {
            Node n2 = n1;
            Node n3 = n1.next;
            while (n3 != null) {
                if (n2.data > n3.data) {
                    n2 = n3;
                }
                n3 = n3.next;
            }
            int t = n1.data;
            n1.data = n2.data;
            n2.data = t;
            n1 = n1.next;
        }
    }

    public int getSum () {
        int sum = 0;
        Node n = head;
        while (n != null) {
            sum += n.data;
            n = n.next;
        }
        return sum;
    }

    public void rotate (String direction, int k) {
        if (direction != "left" && direction != "right") {
            throw new IllegalArgumentException();
        }
        if (k != 0 && head != null && head.next != null) {
            if (direction == "left") {
                if (head.next.next != null) {
                    Node tail = head;
                    while (tail.next != null) {
                        tail = tail.next;
                    }
                    for (int i = 0; i < k; i++) {
                        tail.next = head;
                        head = head.next;
                        tail.next.next = null;
                        tail = tail.next;
                    }
                } else {
                    //swap head and tail for two elements
                    if ((k & 1) != 0) {
                        head.next.next = head;
                        head = head.next;
                        head.next.next = null;
                    }
                }
            } else if (direction == "right") {
                if (head.next.next != null) {
                    Node tail = head;
                    while (tail.next != null) {
                        tail = tail.next;
                    }
                    for (int i = 0; i < k; i++) {
                        tail.next = head;
                        head = tail;
                        while (tail.next != head) {
                            tail = tail.next;
                        }
                        tail.next = null;
                    }
                } else {
                    //swap head and tail for two elements
                    if ((k & 1) != 0) {
                        head.next.next = head;
                        head = head.next;
                        head.next.next = null;
                    }
                }
            }
        }
    }
}