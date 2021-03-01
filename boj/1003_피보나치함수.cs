using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practice
{
    class Program
    {
        static int[] tests;

        static void Main()
        {
            /*-------------------입력-------------------*/
            int numOfTest = int.Parse(Console.ReadLine());

            tests = new int[numOfTest];
            for(int i = 0; i < numOfTest; i++)
            {
                tests[i] = int.Parse(Console.ReadLine());
            }
            /*------------------------------------------*/

            int[,] count = new int[2, 41];
            count[0, 0] = 1;
            count[0, 1] = 0;
            count[1, 0] = 0;
            count[1, 1] = 1;

            for(int i = 2; i <= 40; i++)
            {
                count[0, i] = count[0, i - 1] + count[0, i - 2];
                count[1, i] = count[1, i - 1] + count[1, i - 2];
            }

            for(int i = 0; i < numOfTest; i++)
            {
                Console.WriteLine(count[0, tests[i]].ToString() + " " + count[1,tests[i]].ToString());
            }

        }
            
    }
}
 