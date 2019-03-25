using System;
using lab2;
namespace Lab2
{
    class Program
    {
     
        static void Main(string[] args)
        {
            Int16 x, y;
            Console.WriteLine("Enter 16 bits signed multiplicand:");
            x = Int16.Parse(Console.ReadLine());
            Console.WriteLine("Enter 16 bits signed multiplier:");
            y = Int16.Parse(Console.ReadLine());
            Multiply m = new Multiply(x, y);
            m.Do();


            Console.WriteLine("Enter 16 bits signed dividend:");
            x = Int16.Parse(Console.ReadLine());
            Console.WriteLine("Enter 16 bits signed divisor:");
            y = Int16.Parse(Console.ReadLine());
            Divide d = new Divide(x, y);
            d.Do();

            float a, b;
            Console.WriteLine("Enter first float signed value:");
            a = float.Parse(Console.ReadLine());
            Console.WriteLine("Enter second float signed value:");
            b = float.Parse(Console.ReadLine());
            FloatMultiply f = new FloatMultiply(a, b);
            f.Do();
            Console.ReadKey();
        }
        
        

      
       

      
       
       
    }
}