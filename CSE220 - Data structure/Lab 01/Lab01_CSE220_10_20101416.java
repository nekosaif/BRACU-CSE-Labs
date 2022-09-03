public class Lab01_CSE220_10_20101416
{
	public static void main(String[] args)
	{
		System.out.println("---------Linear Arrays---------");

		System.out.println("-------------Task1-------------");
		int[] source = new int[]{10,20,30,40,50,60};
		System.out.print("source = ");
		printArr(source);
		shiftLeft(source,3);
		System.out.println("Execute shiftLeft(source,3)");
		System.out.print("source = ");
		printArr(source);
		System.out.println("-------------------------------\n");

		System.out.println("-------------Task2-------------");
		source = new int[]{10,20,30,40,50,60};
		System.out.print("source = ");
		printArr(source);
		rotateLeft(source,3);
		System.out.println("Execute rotateLeft(source,3)");
		System.out.print("source = ");
		printArr(source);
		System.out.println("-------------------------------\n");

		System.out.println("-------------Task3-------------");
		source = new int[]{10,20,30,40,50,0,0};
		System.out.print("source = ");
		printArr(source);
		remove(source,5,2);
		System.out.println("Execute remove(source,5,2)");
		System.out.print("source = ");
		printArr(source);
		System.out.println("-------------------------------\n");

		System.out.println("-------------Task4-------------");
		source = new int[]{10,2,30,2,50,2,2,0,0};
		System.out.print("source = ");
		printArr(source);
		removeAll(source,7,2);
		System.out.println("Execute removeAll(source,7,2)");
		System.out.print("source = ");
		printArr(source);
		System.out.println("-------------------------------\n");

		System.out.println("-------------Task5-------------");
		source = new int[]{1, 1, 1, 2, 1};
		System.out.print("source = ");
		printArr(source);
		System.out.println("Execute isSplitableArray(source)");
		System.out.print("Output = ");
		System.out.println(isSplitableArray(source));
		source = new int[]{2, 1, 1, 2, 1};
		System.out.print("source = ");
		printArr(source);
		System.out.println("Execute isSplitableArray(source)");
		System.out.print("Output = ");
		System.out.println(isSplitableArray(source));
		source = new int[]{10, 3, 1, 2, 10};
		System.out.print("source = ");
		printArr(source);
		System.out.println("Execute isSplitableArray(source)");
		System.out.print("Output = ");
		System.out.println(isSplitableArray(source));
		System.out.println("-------------------------------\n");

		System.out.println("-------------Task6-------------");
		System.out.println("Execute arraySeries(n) where n = 2");
		int n = 2;
		System.out.print("n = ");
		System.out.print(n);
		System.out.print(": ");
		source = arraySeries(n);
		System.out.println("Execute arraySeries(n) where n = 3");
		n = 3;
		System.out.print("n = ");
		System.out.print(n);
		System.out.print(": ");
		source = arraySeries(n);
		System.out.println("Execute arraySeries(n) where n = 4");
		n = 4;
		System.out.print("n = ");
		System.out.print(n);
		System.out.print(": ");
		source = arraySeries(n);
		System.out.println("-------------------------------\n");

		System.out.println("-------------Task7-------------");
		source = new int[]{1, 2, 2, 3, 4, 4, 4};
		System.out.print("source = ");
		printArr(source);
		n = maxBunchCount(source);
		System.out.println("Execute maxBunchCount(source)");
		System.out.print("Output = ");
		System.out.println(n);
		source = new int[]{1,1,2, 2, 1, 1,1,1};
		System.out.print("source = ");
		printArr(source);
		n = maxBunchCount(source);
		System.out.println("Execute maxBunchCount(source)");
		System.out.print("Output = ");
		System.out.println(n);
		System.out.println("-------------------------------\n");

		System.out.println("-------------Task8-------------");
		source = new int[]{4,5,6,6,4,3,6,4};
		System.out.print("source = ");
		printArr(source);
		boolean output = isLeastTwoRepeteSame(source);
		System.out.println("Execute isLeastTwoRepeteSame(source)");
		System.out.print("Output = ");
		System.out.println(output);
		source = new int[]{3,4,6,3,4,7,4,6,8,6,6};
		System.out.print("source = ");
		printArr(source);
		output = isLeastTwoRepeteSame(source);
		System.out.println("Execute isLeastTwoRepeteSame(source)");
		System.out.print("Output = ");
		System.out.println(output);
		System.out.println("-------------------------------\n");

		System.out.println("\n--------Circular Arrays--------");
		System.out.println("-------------Task1-------------");
		source = new int[]{20,10,0,0,0,10,20,30};
		System.out.print("source = ");
		printArr(source);
		output = isPalindrome(source, 5, 5);
		System.out.println("Execute isPalindrome(source, 5, 5)");
		System.out.print("Output = ");
		System.out.println(output);
		source = new int[]{10,20,0,0,0,10,20,30};
		System.out.print("source = ");
		printArr(source);
		output = isPalindrome(source, 5, 5);
		System.out.println("Execute isPalindrome(source, 5, 5)");
		System.out.print("Output = ");
		System.out.println(output);
		System.out.println("-------------------------------\n");

		System.out.println("-------------Task2-------------");
		int[] cirArr1 = new int[]{40,50,0,0,0,10,20,30};
		int[] cirArr2 = new int[]{10,20,5,0,0,0,0,0,5,40,15,25};
		System.out.print("cirArr1 = ");
		printArr(cirArr1);
		System.out.print("cirArr2 = ");
		printArr(cirArr2);
		int[] intersectionArray = arrIntersection(cirArr1, 5, 5, cirArr2, 8, 7);
		System.out.println("Execute arrIntersection(cirArr1, 5, 5, cirArr2, 8, 7)");
		System.out.print("Intersection Array = ");
		printArr(intersectionArray);
		System.out.println("-------------------------------\n");

	}

	//Task 01 - Shift Left k Cells
	public static void shiftLeft(int[] source, int k)
	{
		for(int i = 0, j = k; i < source.length; ++i, ++j)
		{
			if(j < source.length)
			{
				source[i] = source[j];
			}
			else
			{
				source[i] = 0;
			}
		}
	}

	//Task 02 - Rotate Left k cells
	public static void rotateLeft(int[] source, int k)
	{
		for(int i = 0, j = k; j < source.length; ++i, ++j)
		{
			if(j < source.length)
			{
				int temp = source[i];
				source[i] = source[j];
				source[j] = temp;
			}
		}
	}

	//Task 03 - Remove an element from an array
	public static void remove(int[] source, int size, int idx)
	{
		for(int i = idx; i < size; ++i)
		{
			int temp = source[i];
			source[i] = source[i+1];
			source[i+1] = temp;
		}
		source[size] = 0;
	}

	//Task 04 - Remove all occurrences of a particular element from an array
	public static void removeAll(int[] source, int size, int element)
	{
		int num_ele = 0;
		for(int i = 0; i < size; ++i)
		{
			if(source[i] == element)
			{
				num_ele++;
				source[i] = 0;
			}
			else
			{
				int temp = source[i-num_ele];
				source[i-num_ele] = source[i];
				source[i] = temp;
			}
		}
	}

	//Task 05 - Splitting an Array
	public static boolean isSplitableArray(int[] source)
	{
		int srcLen = source.length;

		if(srcLen > 1)
		{
			for(int i = 1; i < srcLen; ++i)
			{
				source[i] += source[i-1];
			}
		}

		for(int i = 0; i <= srcLen/2; ++i)
		{
			if(source[srcLen-1] - source[i] == source[i])
			{
				return true;
			}
		}

		return false;
	}

	//Task 06 - Array series
	public static int[] arraySeries(int n)
	{
		int[] arr = new int[n * n];

		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < n; ++j)
			{
				int curr_idx = i * n + j;
				if(n - j - 1 > i)
				{
					arr[curr_idx] = 0;
				}
				else
				{
					arr[curr_idx] = n - j;
				}
			}
		}

		System.out.print('{');
		for(int i = 0; i < arr.length; i++)
		{
			System.out.print(arr[i]);
			if(i < arr.length-1)
			{
				System.out.print(", ");
			}
		}
		System.out.println('}');

		return arr;
	}

	//Task 07 - Max Bunch Count
	public static int maxBunchCount(int[] source)
	{
		int currBunch = source[0];
		int currBunchCnt = 1;
		int maxBunchCnt = 1;

		if(source.length > 1)
		{
			for(int i = 1; i < source.length; ++i)
			{
				if(source[i] == currBunch)
				{
					++currBunchCnt;
				}
				else
				{
					if(maxBunchCnt < currBunchCnt)
					{
						maxBunchCnt = currBunchCnt;
					}
					currBunch = source[i];
					currBunchCnt = 1;
				}
			}
			if(maxBunchCnt < currBunchCnt)
			{
				maxBunchCnt = currBunchCnt;
			}
		}

		return maxBunchCnt;
	}
	
	//Task 08 - Repetition
	public static boolean isLeastTwoRepeteSame(int[] source)
	{
		//bubblesort source
		for (int i = 0; i < source.length-1; i++)
	    {
	        for (int j = 0; j < source.length-i-1; j++) 
	        {
	            if (source[j] > source[j+1])
	            { 
	                source[j] = source[j] ^ source[j+1];
	                source[j+1] = source[j] ^ source[j+1]; 
	                source[j] = source[j] ^ source[j+1]; 
	            } 
	        }
	    }

	    //count source elements and puts inside source else INT_MAX is put
	    int currEle = source[0];
	    source[0] = 2147483647;
	    int currEleClt = 1;
	    for(int i = 1; i < source.length; ++i)
	    {
	    	if(source[i] == currEle)
	    	{
	    		++currEleClt;
	    		source[i] = 2147483647;
	    	}
	    	else
	    	{
	    		source[i-1] = currEleClt;
	    		currEle = source[i];
	    		currEleClt = 1;
	    	}
	    }

	    //bubblesort source
	    for (int i = 0; i < source.length-1; i++)
	    {
	        for (int j = 0; j < source.length-i-1; j++) 
	        {
	            if (source[j] > source[j+1])
	            { 
	                source[j] = source[j] ^ source[j+1];
	                source[j+1] = source[j] ^ source[j+1]; 
	                source[j] = source[j] ^ source[j+1]; 
	            } 
	        }
	    }

		return source[0] == source[1];
	}

	//Task 01 - Palindrome
	public static boolean isPalindrome(int[] source, int start, int size)
	{
		int midIdx = start + size/2;
		for(int i = start, j = start + size - 1; i < midIdx; ++i, --j)
		{
			if(source[i % source.length] != source[j % source.length])
			{
				return false;
			}
		}
		return true;
	}

	//Task 02 - Intersection
	public static int[] arrIntersection(int[] source1, int start1, int size1,
										int[] source2, int start2, int size2)
	{
		int[] retArr = new int[size1 < size2 ? size1 : size2];
		int retArrSize = 0;

		for(int i = start1; i < start1 + size1; ++i)
		{
			for(int j = start2; j < start2 + size2; ++j)
			{
				if(source1[i % source1.length] == source2[j % source2.length])
				{
					//checks whether the retArr contains source1[i]
					boolean addFlag = true;
					for(int k = 0; k < retArrSize; ++k)
					{
						if(source1[i % source1.length] == retArr[k])
						{
							addFlag = false;
						}
					}

					if(addFlag)
					{
						retArr[retArrSize] = source1[i % source1.length];
						++retArrSize;
					}
				}
			}
		}

		int[] retArr2 = new int[retArrSize];

		for(int i = 0; i < retArrSize; ++i)
		{
			retArr2[i] = retArr[i];
		}

		return retArr2;
	}

	//Helper method for testing every cases
	public static void printArr(int[] source)
	{
		System.out.print('[');	
		for(int i = 0; i < source.length; i++)
		{
			System.out.print(source[i]);
			if(i < source.length - 1)
			{
				System.out.print(", ");
			}
		}
		System.out.println(']');
	}
}