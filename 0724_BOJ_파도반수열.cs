using System;

namespace Algorithm
{
    class Program
    {
        static void Main(string[] args)
        {
            int numOfTest = int.Parse(Console.ReadLine());
            int[] testCase = new int[numOfTest];
            for(int i = 0; i < numOfTest; i++)
            {
                testCase[i] = int.Parse(Console.ReadLine());
            }

            int maxValue = MaxValue(testCase);
            long[] arr = new long[maxValue + 1];
            arr[0] = 0;
            arr[1] = 1;
            arr[2] = 1;
            arr[3] = 1;
            arr[4] = 2;
            arr[5] = 2;

            for(int i = 6; i <= maxValue; i++)
            {
                arr[i] = arr[i - 5] + arr[i - 1];
            }

            for(int i = 0; i < numOfTest; i++)
            {
                Console.WriteLine(arr[testCase[i]]);
            }
        }

        static int MaxValue(int[] arr)
        {
            int max = 0;
            for(int i = 1; i < arr.Length; i++)
            {
                if (arr[i] > arr[max])
                    max = i;
            }

            return arr[max];
        }
    }
}
