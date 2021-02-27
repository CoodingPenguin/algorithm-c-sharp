using System;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {
            /*--------------입력--------------*/
            int count = int.Parse(Console.ReadLine());

            int[] amount = new int[count + 1];
            for(int i = 1; i <= count; i++)
            {
                amount[i] = int.Parse(Console.ReadLine());
            }
            /*--------------------------------*/

            int[] DpTable = new int[count + 1];

            DpTable[0] = 0;
            DpTable[1] = amount[1];

            if (count > 1)
                DpTable[2] = amount[1] + amount[2];
            if (count > 2)
            {
                for(int i = 3; i <= count; i++)
                {
                    // 3번 연속으로 먹지 않을 경우
                    DpTable[i] = Math.Max(
                        DpTable[i - 1],                              // 이번에 안 마심 (0)
                        Math.Max(DpTable[i-2] + amount[i],           // 직전에 안 마시고 이번에 마심 (1)
                        DpTable[i-3] + amount[i] + amount[i-1]));    // 직직전에 안 마시고 직전이랑 이번에 마심 (2)
                }
            }

            Console.WriteLine(DpTable[count]); 
        }
    }
}
