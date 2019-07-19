using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practice
{
    class Program
    {

        static int[] time;

        static void Main(string[] args)
        {
            int numOfPeople = 0;

            /*-------------------입력-------------------*/
            numOfPeople = int.Parse(Console.ReadLine());
            time = new int[numOfPeople];

            string input = Console.ReadLine();
            string[] parsing = input.Split(' ');

            for(int i = 0; i < time.Length; i++)
            {
                time[i] = int.Parse(parsing[i]);
            }
            /*-----------------------------------------*/

            int result = SumOfTime();
            Console.WriteLine(result);
        }

        static int SumOfTime()
        {
            Sort();
            
            for(int i = 0; i < time.Length; i++)
            {
                time[i] *= time.Length - i;
            }

            int total = 0;
            for(int i = 0; i<time.Length; i++)
            {
                total += time[i];
            }

            return total;
        }

        static void Sort()
        {
            for(int i = 0; i < time.Length -1; i++)
            {
                int temp = i;
                for(int j = i+1; j < time.Length; j++)
                {
                    if (time[temp] >= time[j])
                        temp = j;
                }

                Swap(i, temp);
            }
        }

        static void Swap(int x, int y)
        {
            int temp = time[x];
            time[x] = time[y];
            time[y] = temp;
        }
    }
}
 