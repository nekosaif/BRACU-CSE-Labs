public class Lab07_20101416 {
    public static void main(String[] args) {

        System.out.println("----------------------Tester Arrays----------------------");
        System.out.println("Evaluate arrPos = new int[]{4, 2, 3, 4, 7, 4}");
        int[] arrPos = new int[]{4, 2, 3, 4, 7, 4};
        System.out.println("Evaluate arrNeg = new int[]{4, -2, 3, -4, 7, 4}");
        int[] arrNeg = new int[]{4, -2, 3, -4, 7, 4};
        System.out.println("---------------------------------------------------------\n");


        System.out.println("--------------------------Task1--------------------------");
        System.out.println("Constructor KeyIndex(int []a):");
        System.out.println("Evaluate kIdxObjPos = new KeyIndex(arrPos)");
        KeyIndex kIdxObjPos = new KeyIndex(arrPos);
        System.out.println("Evaluate kIdxObjPos.printKeyIndexArray()");
        kIdxObjPos.printKeyIndexArray();
        System.out.println("Evaluate kIdxObjNeg = new KeyIndex(arrNeg)");
        KeyIndex kIdxObjNeg = new KeyIndex(arrNeg);
        System.out.println("Evaluate kIdxObjNeg.printKeyIndexArray()");
        kIdxObjNeg.printKeyIndexArray();

        System.out.println("\nMethod search(int val):");
        System.out.println("Execute a loop from -10 to 10 and search in kIdxObjPos and prints if it exists");
        for(int i = -10; i < 10; ++i) {
            if(kIdxObjPos.search(i)) {
                System.out.print(i);
                System.out.print(" ");
            }
        }
        System.out.println();
        System.out.println("Execute a loop from -10 to 10 and search in kIdxObjNeg and prints if it exists");
        for(int i = -10; i < 10; ++i) {
            if(kIdxObjNeg.search(i)) {
                System.out.print(i);
                System.out.print(" ");
            }
        }

        System.out.println("\n\nMethod sort():");
        System.out.println("Execute printArr(kIdxObjPos.sort())");
        printArr(kIdxObjPos.sort());
        System.out.println("Execute printArr(kIdxObjNeg.sort())");
        printArr(kIdxObjNeg.sort());
        System.out.println("---------------------------------------------------------\n");


        System.out.println("----------------------Tester Arrays----------------------");
        System.out.println("Evaluate strArr = new String[]{\"ABC\", \"IJK\", \"LKN\", \"CAB\", \"PAL\", \"TOP\"}");
        String[] strArr = new String[]{"ABC", "IJK", "LKN", "CAB", "PAL", "TOP"};
        System.out.println("---------------------------------------------------------\n");

        System.out.println("--------------------------Task2--------------------------");
        System.out.println("Constructor Hashing(String[] arr):");
        System.out.println("Evaluate hashObj = new Hashing(strArr)");
        Hashing hashObj = new Hashing(strArr);
        System.out.println("Evaluate hashObj.printHashTable()");
        hashObj.printHashTable();

        System.out.println("\nMethod search(String str):");
        System.out.println("Execute iterate through strArr[] and search in hashObj and prints if it exists");
        for(int i = 0; i < strArr.length; ++i) {
            if(hashObj.search(strArr[i])) {
                System.out.print(strArr[i] + " ");
            }
        }
        System.out.println("\n---------------------------------------------------------\n");
    }

    public static void printArr(int[] arr) {
        for(int i = 0; i < arr.length; ++i) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }
        System.out.println();
    }
}

class KeyIndex {
    private int[] k;
    private int shift;

    public KeyIndex(int[] a) {
        if(a != null && a.length != 0) {
            int min = 1, max = -1;
            boolean isPositive = true;

            //min finder for non-negative array and max finder for any array
            for (int i = 0; i < a.length; ++i) {
                if (a[i] > max) {
                    max = a[i];
                }
                if (a[i] < 0) {
                    isPositive = false;
                    if (a[i] < min) {
                        min = a[i];
                    }
                }
            }

            //shift calculation for negative array
            if (!isPositive) {
                shift = min * (-1);
            }

            //data insertion in k[]
            k = new int[isPositive ? max + 1 : shift + max + 1];
            for (int i = 0; i < a.length; ++i) {
                k[a[i] + shift] += 1;
            }
        }
    }

    //for testing and debugging purpose
    public void printKeyIndexArray() {
        System.out.print("[");
        if(k != null) {
            for(int i = 0; i < k.length; ++i) {
                System.out.print(k[i]);
                if(i < k.length - 1) {
                    System.out.print(", ");
                }
            }
        }
        System.out.println("]");
    }

    public boolean search(int val) {
        if(k != null) {
            //search for non-negative array
            if(shift == 0) {
                if(val < 0 || val >= k.length) {
                    return false;
                } else {
                    return k[val] != 0;
                }
                //search for negative array
            } else {
                if(val+shift < 0 || val+shift >= k.length) {
                    return false;
                } else {
                    return k[val+shift] != 0;
                }
            }
        }
        return false;
    }

    public int[] sort() {
        //num of Ele counter
        int numEle = 0;
        for(int i = 0; i < k.length; ++i) {
            numEle += k[i];
        }
        int[] retArr = new int[numEle];

        //sorted printing
        for(int kIdx = 0, retArrIdx = 0; kIdx < k.length; ++kIdx) {
            for(int multiplierIdx = 0; multiplierIdx < k[kIdx]; ++multiplierIdx, ++retArrIdx) {
                retArr[retArrIdx] = shift == 0 ? kIdx : kIdx-shift;
            }
        }

        return retArr;
    }
}

class Hashing {
    String[] hashTable;

    public Hashing(String[] arr) {
        //initializing hashTable[] and setting null every element
        hashTable = new String[9];
        for(int i = 0; i < hashTable.length; ++i) {
            hashTable[i] = null;
        }

        //filling hashtable with arr[] elements
        for(int i = 0; i < arr.length; ++i) {
            int hashVal = hashFunction(arr[i]);
            //no collision in hashtable
            if(hashTable[hashVal] == null) {
                hashTable[hashVal] = arr[i];
            }
            //collision in hashtable and using liner probing
            else {
                int c = hashVal + 1;
                while(c%9 != hashVal-1) {
                    if(hashTable[c%9] == null) {
                        hashTable[c] = arr[i];
                        break;
                    }
                    ++c;
                }
            }
        }
    }

    public boolean search(String str) {
        //searching in hashVal and checking consecutive elements for linear probing
        int hashVal = hashFunction(str);
        int idx = hashVal;
        while((idx % 9) == hashVal-1 || hashTable[(idx % 9)] != null) {
            if(hashTable[(idx % 9)] == str) {
                return true;
            }
            ++idx;
        }
        return false;
    }

    //for testing and debugging purpose
    public void printHashTable() {
        System.out.println("Index\t=\tString");
        for(int i = 0; i < hashTable.length; ++i) {
            System.out.println(String.valueOf(i) + "\t\t=\t" + hashTable[i]);
        }
    }

    private int hashFunction(String str) {
        int retVal = 0;
        for(int i = 0; i < str.length(); ++i) {
            char chr = str.charAt(i);
            //if character is a alphabet
            if((97 <= (int)chr && (int)chr <= 122) || (65 <= (int)chr && (int)chr <= 90)) {
                //if character is a consonants
                if(chr != 'a' && chr != 'e' && chr != 'i' && chr != 'o' && chr != 'u' &&
                   chr != 'A' && chr != 'E' && chr != 'I' && chr != 'O' && chr != 'U') {
                    retVal += 24;
                }
            //if character is a digit
            } else if(48 <= (int)chr && (int)chr <= 57) {
                retVal += ((int)chr - 48);
            }
        }
        return retVal%9;
    }
}