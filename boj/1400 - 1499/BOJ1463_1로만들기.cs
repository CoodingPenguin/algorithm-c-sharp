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

            int[] DpTable = new int[input + 1];

            DpTable[0] = 0;
            DpTable[1] = 0;

            for(int i = 2; i <= input; i++)
            {
                if(i%2 == 0 && i%3 == 0)
                {
                    DpTable[i] = Math.Min(DpTable[i - 1], Math.Min(DpTable[i / 3], DpTable[i / 2])) + 1;
                }
                else if(i%2 == 0 && i%3 != 0)
                {
                    DpTable[i] = Math.Min(DpTable[i - 1], DpTable[i / 2]) + 1;
                }
                else if(i%2 != 0 && i%3 == 0)
                {
                    DpTable[i] = Math.Min(DpTable[i - 1], DpTable[i / 3]) + 1;
                }
                else
                {
                    DpTable[i] = DpTable[i - 1] + 1;
                }
            }

            Console.WriteLine(DpTable[input]);
        }
    }
}
