using System;

// 결론 : Table이 다가 아니라 점화식이 다다
// 식을 세워야 뭐든 한다!
namespace Algorithm
{
    class Program
    {
        static void Main()
        {
            int size = int.Parse(Console.ReadLine());
            int[,] DpTable = new int[size, size];

            /*--------------------입력--------------------*/
            for(int i = 0; i < size; i++)
            {
                if (i == 0)
                    DpTable[0, 0] = int.Parse(Console.ReadLine());
                else
                {
                    string[] parsing = Console.ReadLine().Split(' ');
                    for(int j = 0; j < parsing.Length; j++)
                    {
                        DpTable[i, j] = int.Parse(parsing[j]);
                    }
                }
            }
            /*--------------------------------------------*/

            int max = 0;
            for (int row = 1; row < size; row++)
            {
                for (int col = 0; col < row + 1; col++)
                {
                    // 중간에 있는 경우
                    if (col != 0 && col < row)
                    {
                        DpTable[row, col] += Math.Max(DpTable[row - 1, col - 1], DpTable[row - 1, col]);
                    }
                    // 왼쪽 끝에 있는 경우
                    else if(col == 0)
                    {
                        DpTable[row, col] += DpTable[row - 1, col];
                    }
                    // 오른쪽 끝에 있는 경우
                    else if(row == col)
                    {
                        DpTable[row, col] += DpTable[row - 1, col - 1];
                    }

                    if (DpTable[row, col] > max)
                        max = DpTable[row, col];
                }
            }

            Console.WriteLine(max);
        }
    }
}
