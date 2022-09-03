public class Lab06_20101416 {
    public static void main(String[] args) {

        System.out.println("--------------------------Task1--------------------------");
        System.out.println("Execute arr = new int[]{3, 4, 2, 7, 8, 0, 1, 9}");
        int[] arr = new int[]{3, 4, 2, 7, 8, 0, 1, 9};
        System.out.println("Execute printArr(arr)");
        printArr(arr);
        System.out.println("Execute selectionSortRecur(arr, 0)");
        selectionSortRecur(arr, 0);
        System.out.println("Execute printArr(arr)");
        printArr(arr);
        System.out.println("---------------------------------------------------------\n");

        System.out.println("--------------------------Task2--------------------------");
        System.out.println("Execute arr = new int[]{3, 4, 2, 7, 8, 0, 1, 9}");
        arr = new int[]{3, 4, 2, 7, 8, 0, 1, 9};
        System.out.println("Execute printArr(arr)");
        printArr(arr);
        System.out.println("Execute insertionSort(arr, 0, arr.length)");
        insertionSort(arr, 0, arr.length);
        System.out.println("Execute printArr(arr)");
        printArr(arr);
        System.out.println("---------------------------------------------------------\n");

        System.out.println("--------------------------Task3--------------------------");
        System.out.println("Execute list = new LinkedList(new int[]{3, 4, 2, 7, 8, 0, 1, 9})");
        LinkedList list = new LinkedList(new int[]{3, 4, 2, 7, 8, 0, 1, 9});
        System.out.println("Execute list.print()");
        list.print();
        System.out.println("Execute bubbleSortLinkedList(list)");
        bubbleSortLinkedList(list);
        System.out.println("Execute list.print()");
        list.print();
        System.out.println("---------------------------------------------------------\n");

        System.out.println("--------------------------Task4--------------------------");
        System.out.println("Execute list = new LinkedList(new int[]{3, 4, 2, 7, 8, 0, 1, 9})");
        list = new LinkedList(new int[]{3, 4, 2, 7, 8, 0, 1, 9});
        System.out.println("Execute list.print()");
        list.print();
        System.out.println("Execute selectionSortLinkedList(list)");
        selectionSortLinkedList(list);
        System.out.println("Execute list.print()");
        list.print();
        System.out.println("---------------------------------------------------------\n");

        System.out.println("--------------------------Task5--------------------------");
        System.out.println("Execute doublyList = new DoublyLinkedList(new int[]{3, 4, 2, 7, 8, 0, 1, 9})");
        DoublyLinkedList doublyList = new DoublyLinkedList(new int[]{3, 4, 2, 7, 8, 0, 1, 9});
        System.out.println("Execute doublyList.print()");
        doublyList.print();
        System.out.println("Execute insertionSortDoublyLinkedList(list)");
        insertionSortDoublyLinkedList(doublyList);
        System.out.println("Execute doublyList.print()");
        doublyList.print();
        System.out.println("---------------------------------------------------------\n");

        System.out.println("--------------------------Task6--------------------------");
        System.out.println("Execute arr = new int[]{3, 4, 2, 7, 8, 0, 1, 9}");
        arr = new int[]{14, 28, 34, 47, 52, 67, 72, 85};
        System.out.println("Execute printArr(arr)");
        printArr(arr);
        System.out.println("Execute a loop from 0 to 100 and find and print number of arr");
        for(int i = 0; i < 100; ++i) {
            if(binarySearch(arr, i, 0, arr.length)) {
                System.out.print(String.valueOf(i) + " ");
            }
        }
        System.out.println("\n---------------------------------------------------------\n");

        System.out.println("--------------------------Task7--------------------------");
        System.out.println("Execute a loop from 0 to 10 and print fibonacci number with fibonacciRecursiveMemorization()");
        for(int i = 0; i < 10; ++i) {
            System.out.print(String.valueOf(fibonacciRecursiveMemorization(i, null)) + " ");
        }
        System.out.println("\n---------------------------------------------------------\n");

    }

    public static void printArr(int[] arr) {
        for(int i = 0; i < arr.length; ++i) {
            System.out.print(arr[i]);
            if(i != arr.length-1) {
                System.out.print(", ");
            }
        }
        System.out.println();
    }

    public static void selectionSortRecur(int[] arr, int start) {
        int minIdx = start;
        for(int j = start+1; j < arr.length; ++j) {
            if(arr[minIdx] > arr[j]) {
                minIdx = j;
            }
        }
        if(minIdx != start) {
            arr[minIdx] = arr[minIdx] ^ arr[start];
            arr[start] = arr[minIdx] ^ arr[start];
            arr[minIdx] = arr[minIdx] ^ arr[start];
        }
        if(start < arr.length-1) {
            selectionSortRecur(arr, start+1);
        }
    }

    public static void insertionSort(int[] arr, int startIdx, int length) {
        int insertEle = arr[startIdx + 1];
        int insertIdx = startIdx + 1;
        while (insertIdx > 0 && arr[insertIdx - 1] > insertEle) {
            arr[insertIdx] = arr[insertIdx - 1];
            insertIdx--;
        }
        arr[insertIdx] = insertEle;
        if (startIdx <= length - 3) {
            insertionSort(arr, startIdx + 1, length);
        }
    }

    public static void bubbleSortLinkedList(LinkedList l) {
        int length = Integer.MAX_VALUE;
        int cntLength = 0;
        for(int i = 0; i < length; ++i) {
            LinkedList.Node n = l.head;
            while(n.next != null) {
                if(n.data > n.next.data) {
                    n.data = n.data ^ n.next.data;
                    n.next.data = n.data ^ n.next.data;
                    n.data = n.data ^ n.next.data;
                }
                n = n.next;
                if(length == Integer.MAX_VALUE) {
                    ++cntLength;
                }
            }
            if(length == Integer.MAX_VALUE) {
                length = cntLength;
            }
        }
    }

    public static void selectionSortLinkedList(LinkedList l) {
        int length = Integer.MAX_VALUE;
        int cntLength = 1;
        LinkedList.Node startNode = l.head;
        for(int i = 0; i < length - 1; ++i) {
            LinkedList.Node minNode = startNode;
            LinkedList.Node n = startNode;
            while(n != null) {
                if(minNode.data > n.data) {
                    minNode = n;
                }
                if(length == Integer.MAX_VALUE) {
                    ++cntLength;
                }
                n = n.next;
            }
            if(minNode != startNode) {
                startNode.data  = startNode.data ^ minNode.data;
                minNode.data  = startNode.data ^ minNode.data;
                startNode.data  = startNode.data ^ minNode.data;
            }
            if(length == Integer.MAX_VALUE) {
                length = cntLength;
            }
            startNode = startNode.next;
        }
    }

    public static void insertionSortDoublyLinkedList(DoublyLinkedList l) {
        if(l.head.next != null) {
            DoublyLinkedList.Node n = l.head.next;
            while (n != l.head) {
                if(n.prev.data > n.data) {
                    DoublyLinkedList.Node insertNode = n.prev;
                    n.prev.next = n.next;
                    n.next.prev = n.prev;
                    while(insertNode.prev.data > n.data) {
                        if(insertNode == l.head) {
                            l.head = n;
                            break;
                        }
                        insertNode = insertNode.prev;
                    }
                    insertNode.prev.next = n;
                    n.next = insertNode;
                    n.prev = insertNode.prev;
                    insertNode.prev = n;
                }
                n = n.next;
            }
        }
    }

    public static boolean binarySearch(int[] arr, int target, int start, int end) {
        int m = (start + end)/2;
        if(arr[m] == target) {
            return true;
        }
        if (start == m || end == m) {
            return false;
        }
        return binarySearch(arr, target, start, m) || binarySearch(arr, target, m+1, end);
    }

    public static long fibonacciRecursiveMemorization(int n, long[] cache) {
        if(cache == null) {
            cache = new long[n+1];
            for(int i = 0; i <= n; ++i) {
                cache[i] = -1;
            }
        }
        if(n == 0 || n == 1) {
            return n;
        } else {
            long fiboNPre = cache[n-1] != -1 ? cache[n-1] : fibonacciRecursiveMemorization(n-1, cache);
            long fiboNPrePre = cache[n-2] != -1 ? cache[n-2] : fibonacciRecursiveMemorization(n-2, cache);
            cache[n] = fiboNPre + fiboNPrePre;
            return cache[n];
        }
    }
}

class LinkedList {
    class Node {
        int data;
        Node next;
        public Node(int data, Node next) {
            this.data = data;
            this.next = next;
        }
    }

    Node head;

    public LinkedList() {
    }

    public LinkedList(int[] arr) {
        for(int i = 0; i < arr.length; ++i) {
            this.insert(arr[i]);
        }
    }

    public void insert(int data) {
        if(head == null) {
            head = new Node(data, null);
        } else {
            Node n = head;
            while(n.next != null) {
                n = n.next;
            }
            n.next = new Node(data, null);
        }
    }

    public void print() {
        System.out.print("[");
        Node n = head;
        while(n != null) {
            System.out.print(n.data);
            if (n.next != null) {
                System.out.print(" -> ");
            }
            n = n.next;
        }
        System.out.println("]");
    }
}

class DoublyLinkedList {
    class Node {
        Node prev;
        int data;
        Node next;
        public Node(Node prev, int data, Node next) {
            this.prev = prev;
            this.data = data;
            this.next = next;
        }
    }

    Node head;

    public DoublyLinkedList() {
    }

    public DoublyLinkedList(int[] arr) {
        for(int i = 0; i < arr.length; ++i) {
            this.insert(arr[i]);
        }
    }

    public void insert(int data) {
        if(head == null) {
            head = new Node(null, data, null);
            head.prev = head;
            head.next = head;
        } else {
            head.prev.next = new Node(head.prev, data, head);
            head.prev = head.prev.next;
        }
    }

    public void print() {
        System.out.print("[");
        DoublyLinkedList.Node n = head;
        System.out.print(n.data);
        if (n.next != head) {
            System.out.print(" -> ");
        }
        while(n.next != head) {
            n = n.next;
            System.out.print(n.data);
            if (n.next != head) {
                System.out.print(" -> ");
            }
        }
        System.out.println("]");
    }
}