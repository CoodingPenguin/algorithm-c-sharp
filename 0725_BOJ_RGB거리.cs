using System;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {
            int[,] cost;   // 입력
            int house;     // 입력

            /*----------------입력---------------*/
            house = int.Parse(Console.ReadLine());

            cost = new int[house, 3];   // 집, 색깔

            string[] parsing = Console.ReadLine().Split(' ');
            cost[0, 0] = int.Parse(parsing[0]);
            cost[0, 1] = int.Parse(parsing[1]);
            cost[0, 2] = int.Parse(parsing[2]);

            /*-----------------------------------*/
            
            for(int i = 1; i < house; i++)
            {
                string[] subparsing = Console.ReadLine().Split(' ');

                cost[i, 0] = int.Parse(subparsing[0]) + Math.Min(cost[i - 1, 1], cost[i - 1, 2]);   // 이번에 빨간 색
                cost[i, 1] = int.Parse(subparsing[1]) + Math.Min(cost[i - 1, 0], cost[i - 1, 2]);   // 이번에 초록 색
                cost[i, 2] = int.Parse(subparsing[2]) + Math.Min(cost[i - 1, 0], cost[i - 1, 1]);   // 이번에 파란 색
            }

            Console.WriteLine(Math.Min(cost[house - 1, 0], Math.Min(cost[house - 1, 1], cost[house - 1, 2])));
        }
    }
}
