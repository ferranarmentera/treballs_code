using System;

namespace exponentia_method_forloop
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(GetPow(4, 3)); //cridem al mètode getpow i li assignem els valor 4 i 3
            Console.ReadLine();
        }
        static int GetPow(int baseNum,int powNum) //declarem el mètode amb les variables
        {
            int result = 1; //declarem la variable result =1
            for(int i = 0; i < powNum; i++)  // fem el for loop 
            {
                result = result * baseNum; // fem el càcul
            }
            return result; 
        }
    }
}
