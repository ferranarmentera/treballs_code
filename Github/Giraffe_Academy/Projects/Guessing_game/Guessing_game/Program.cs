using System;

namespace Guessing_game
{
    class Program
    {
        static void Main(string[] args)
        {
            string secretWord = "giraffe";
            string guess = "";
            int guessCount = 0;
            bool outOfGuesses = false;
            int guessLimit = 3;

            while(guess!=secretWord && !outOfGuesses)// el guess no es igual a secretword (and = &&) el usuari no  esta (negació logica = ! fora del outofguesses
            {
                if(guessCount < guessLimit)
                {
                    Console.Write("Enter guess:   ");
                    guess = Console.ReadLine();
                    guessCount++;   // comptador de proves
                }
                else
                {
                    outOfGuesses = true;   
                }
                
            }
            if (outOfGuesses)
            {
                Console.Write("you lose!");

            }
            else
            {
                Console.Write("you win!!!");
            }


            Console.ReadLine();
        }
    }
}
