using System;

namespace Algorithm
{
    class Program
    {
        static int[] value;

        static void Main()
        {
            /*----------------------입력----------------------*/
            int size = int.Parse(Console.ReadLine());

            value = new int[size];
            for(int i = 0; i < size; i++)
            {
                value[i] = int.Parse(Console.ReadLine());        
            }
            /*------------------------------------------------*/

            int[,] DpTable = new int[size, size];

            for(int row = 0; row < size - 1; row++)
            {
                for(int col = row + 1; col < row + 3 && col < size; col++)
                {
                    if (row == 0)
                        DpTable[row, col] = value[row] + value[col];
                    else if (row == 1)
                    {
                        if (col == row + 1)
                            DpTable[row, col] = value[row] + value[col];
                        else if (col == row + 2)
                            DpTable[row, col] = Math.Max(value[row], DpTable[row-1, col - 2]) + value[col];
                    }
                    else
                    {
                        if (col == row + 1)
                            DpTable[row, col] = DpTable[row - 2, col - 1] + value[col];
                        else if (col == row + 2)
                            DpTable[row, col] = Math.Max(DpTable[row - 2, col - 2], DpTable[row - 1, col - 2]) + value[col];
                    }
                }
            }

            Console.WriteLine(Math.Max(DpTable[size - 3, size - 1], DpTable[size - 2, size - 1]));
        }
    }
}
