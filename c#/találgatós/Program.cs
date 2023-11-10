using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace games
{
    class Program
    {
        static void Main(string[] args)
        {
            char userInput;
            Random rnd = new Random();
            do
            {
                Console.Write("Akarsz járszani még egyet ? y/n");
                userInput = Console.ReadKey().KeyChar;
                Console.WriteLine(); 

                if (userInput == 'n')
                {
                    Console.WriteLine("Akkor majd legközelebb :-)");
                    Console.ReadKey();
                    break;

                }
                else if (userInput == 'y')
                {
                    int szam = rnd.Next(0, 100);
                    int találat = 0;
                    int darab = 0;
                    Console.WriteLine("Találd ki a számot");
                    találat = int.Parse(Console.ReadLine());
                    do
                    {
                        if (szam > találat)
                        {
                            Console.WriteLine("A szám nagyobb mint a tipped");
                            találat = int.Parse(Console.ReadLine());
                            darab++;
                        }
                        else if (szam < találat)
                        {
                            Console.WriteLine("A szám kissebb mint a tipped");
                            találat = int.Parse(Console.ReadLine());
                            darab++;
                        }
                    } while (szam != találat);
                    Console.WriteLine($"Gratulálok eltaláltad!A szám: {szam} ");
                    Console.WriteLine($"Ennyi találatból találtad el : {darab}");
                }
                else
                {
                    Console.WriteLine("nem jól adtad meg próbáld meg újra");
                }

            } while (true);

        }
    }
}
