using System;

namespace LuckyNumbers_LoopTrials
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] LuckyNumbers = { 4, 56, 8, 41, 55, 23, 12 };//creem un array [] amb el nom LuckyNUmbers que conte els numeros dintre de {}
            for(int i=0; i < LuckyNumbers.Length; i++) // el loop for és millor que els while perque queda molt més polit
                // els dos fan el mateix pero el for loop ocupa molt menys lloc 
            {
                Console.WriteLine(LuckyNumbers[i]);
            }
            Console.ReadLine();
        }
    }
}
