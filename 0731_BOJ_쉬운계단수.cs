using System;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {
            /*--------------입력--------------*/
            int input = int.Parse(Console.ReadLine());
            /*--------------------------------*/

            long[,] DpTable = new long[input + 1, 10];

            /*--------------초기화------------*/
            DpTable[1, 0] = 0;
            DpTable[1, 1] = 1;
            DpTable[1, 2] = 1;
            DpTable[1, 3] = 1;
            DpTable[1, 4] = 1;
            DpTable[1, 5] = 1;
            DpTable[1, 6] = 1;
            DpTable[1, 7] = 1;
            DpTable[1, 8] = 1;
            DpTable[1, 9] = 1;
            /*--------------------------------*/

            for(int row = 2; row <= input; row++)
            {
                for(int col = 0; col < 10; col++)
                {
                    if (col == 0)
                        DpTable[row, col] = (DpTable[row - 1, col + 1]) % 1000000000;
                    else if (col == 9)
                        DpTable[row, col] = DpTable[row - 1, col - 1] % 1000000000;
                    else
                        DpTable[row, col] = (DpTable[row - 1, col - 1] + DpTable[row - 1, col + 1]) % 1000000000;
                }
            }

            long total = 0;
            for(int col = 0; col < 10; col++)
            {
                total += DpTable[input, col];
            }

            Console.WriteLine(total % 1000000000);
        }
    }
}
