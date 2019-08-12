using System;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {
            /*--------------입력--------------*/
            int count = int.Parse(Console.ReadLine());

            string[] parsing = Console.ReadLine().Split(' ');
            int[] num = new int[count + 1];
            num[0] = 0;
            for(int i = 1; i <= count; i++)
            {
                num[i] = int.Parse(parsing[i - 1]);
            }
            /*--------------------------------*/

            int[,] DpTable = new int[count + 1, count + 1];
            
            for(int row = 0; row < count; row++)
            {
                for(int col = row + 1; col <= count; col++)
                {
                    if (row == 0)
                        DpTable[row, col] = 1;
                    else if (num[row] >= num[col])
                        DpTable[row, col] = 0;
                    else if (num[row] < num[col])
                    {
                        int max = 0;
                        for(int i = 0; i < row; i++)
                        {
                            if (DpTable[i, row] > max)
                                max = DpTable[i, row];
                        }
                        DpTable[row, col] = max + 1;
                    }
                }
            }

            int maxCnt = 0;
            for(int row = 0; row < count; row++)
            {
                for(int col = row + 1; col <= count; col++)
                {
                    if (DpTable[row, col] > maxCnt)
                        maxCnt = DpTable[row, col];
                }
            }

            Console.WriteLine(maxCnt);

        }
    }
}
