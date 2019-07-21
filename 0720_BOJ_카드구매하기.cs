using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practice
{
    class Program
    {
        static int MAXCARD; // 최대 살 수 있는 카드
        static int MAXKIND; // 최대 고를 수 있는 카드 종류

        static void Main()
        {
            /*--------------------입력--------------------*/
            MAXCARD = int.Parse(Console.ReadLine());
            //Console.WriteLine("디버깅 : " + MAXCARD);

            string[] parsing = Console.ReadLine().Split(' ');
            MAXKIND = parsing.Length;

            int[] price = new int[MAXKIND];
            for (int i = 0; i < MAXKIND; i++)
            {
                price[i] = int.Parse(parsing[i]);
                //Console.WriteLine("디버깅[" + i + "] : " + price[i]);
            }
            /*--------------------------------------------*/

            int[,] DpTable = new int[MAXKIND + 1, MAXCARD + 1];

            for(int kindCnt = 0; kindCnt <= MAXKIND; kindCnt++)
            {
                for(int cardCnt = 0; cardCnt <= MAXCARD; cardCnt++)
                {
                    if (kindCnt == 0 || cardCnt == 0)
                        DpTable[kindCnt, cardCnt] = 0;
                    else if (cardCnt >= kindCnt)
                        // 넣을 수 있다면
                        // "그 전 종류에서 가능했던 조합"과 "그 전 종류에서 넣으려는 카드를 제외하고 가능했던 조합 + 넣으려는 카드" 중 가장 큰 것
                        DpTable[kindCnt, cardCnt] = Math.Max(DpTable[kindCnt - 1, cardCnt], (DpTable[kindCnt, cardCnt - kindCnt] + price[kindCnt - 1]));
                    else
                        // 넣을 수 없다면
                        // 그 전 조합을 넣는다
                        DpTable[kindCnt, cardCnt] = DpTable[kindCnt - 1, cardCnt];

                    //Console.WriteLine("DpTable[" + kindCnt+ ", " + cardCnt + "] : " +  DpTable[kindCnt, cardCnt]);
                }
                //Console.WriteLine("////////");
            }

            /*
            for(int i = 0; i <= MAXKIND; i++)
            {
                for(int j = 0; j <= MAXCARD; j++)
                {
                    Console.Write(DpTable[i, j]);
                }
                Console.WriteLine();
            }
            */

            Console.WriteLine(DpTable[MAXKIND, MAXCARD]);
        }

    }
}
 