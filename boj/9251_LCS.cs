using System;
using System.Linq;

namespace Algorithm
{
    class Program
    { 
        static void Main(string[] args)
        {
            string first = "0" + Console.ReadLine();
            string second = "0" + Console.ReadLine();

            int[,] DpTable = new int[first.Length, second.Length];
            
            for(int row = 0; row < first.Length; row++)
            {
                for(int col = 0; col < second.Length; col++)
                {
                    if (row == 0 || col == 0)
                        DpTable[row, col] = 0;
                    else if (first[row] == second[col])
                        DpTable[row, col] = DpTable[row - 1, col - 1] + 1;
                    else if (first[row] != second[col])
                        DpTable[row, col] = Math.Max(DpTable[row - 1, col], DpTable[row, col - 1]);
                }
            }

            Console.WriteLine(DpTable[first.Length - 1, second.Length - 1]);
        }
    }
}
