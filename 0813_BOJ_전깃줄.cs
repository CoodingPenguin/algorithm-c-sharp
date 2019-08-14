using System;
using System.Linq;

namespace Algorithm
{
    class Program
    {
        static int count;
        static int[,] elec;

        static void Main(string[] args)
        {
            /*---------------- 입력 ----------------*/
            count = int.Parse(Console.ReadLine());

            elec = new int[count + 1, count + 1];
            for(int i = 1; i <= count; i++)
            {
                string[] parsing = Console.ReadLine().Split();
                elec[i, 0] = int.Parse(parsing[0]);
                elec[i, 1] = int.Parse(parsing[1]);
            }
            /*---------------------------------------*/

            SortElec();

            int[] DpTable = new int[count + 1];
            DpTable[0] = 0;
            for(int i = 1; i <= count; i++)
            {
                DpTable[i] = 1;
            }

            for(int i = 1; i <= count; i++)
            {
                for(int j = 0; j < i; j++)
                {
                    if (elec[j, 1] < elec[i, 1] && DpTable[i] < DpTable[j] + 1)
                        DpTable[i] = DpTable[j] + 1;
                }
            }

            int max = DpTable.Max();

            Console.WriteLine(count - max);
        }

        static void SortElec()
        {
            for(int i = 1; i < count; i++)
            {
                int min = i;
                for(int j = i+1; j <= count; j++)
                {
                    if (elec[j, 0] < elec[min, 0])
                        min = j;
                }

                if (i != min)
                    Swap(i, min);
            }
        }

        static void Swap(int x, int y)
        {
            int temp1 = elec[x, 0];
            int temp2 = elec[x, 1];

            elec[x, 0] = elec[y, 0];
            elec[x, 1] = elec[y, 1];

            elec[y, 0] = temp1;
            elec[y, 1] = temp2;
        }
    }
}
