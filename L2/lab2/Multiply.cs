using System;

namespace lab2
{
    public class Multiply
    {
        public int Multiplicand { get; set; }
        public int Multiplier { get; set; }
        public Multiply(int x, int y)
        {
            Multiplicand = x;
            Multiplier = y;
        }
        public void Do()
        {
            Int64 A = (Int64)Multiplicand << 17,
                S = (Int64)(-Multiplicand) << 17,
                P = (Multiplier << 1) & 0b0000_0000_0000_0000_1111_1111_1111_1111_0; //fill first 16 bits by zeros
            string A_bits = IntToBinaryString(A),
                S_bits = IntToBinaryString(S);
            Console.WriteLine("Booth's algorithm:");
            for (int i = 1; i < 17; ++i)
            {
                Console.WriteLine("  Step " + i + ":");
                switch (P & 0b11)
                {
                    case 0b01:
                        Console.WriteLine("  \tAdd A:\t{0}\n\tTo P:\t{1}", A_bits, IntToBinaryString(P));
                        P += A;
                        break;
                    case 0b10:
                        Console.WriteLine("  \tAdd S:\t{0}\n\tTo P:\t{1}", S_bits, IntToBinaryString(P));
                        P += S;
                        break;
                }
                Console.WriteLine("  \tShift right:\t" + IntToBinaryString(P));
                P >>= 1;
                Console.WriteLine("  \t\t        " + IntToBinaryString(P));
            }
            P >>= 1; //discard the last bit
            Console.WriteLine("  Answer is:\n\tIn decemal: {0}\n\tIn binary: {1}", P, IntToBinaryString(P, true));
        }

        private string IntToBinaryString(Int64 number, bool is_end_result = false)
        {
            const int mask = 1;
            var binary = string.Empty;
            for (int i = (is_end_result ? 1 : 0); i < 33; ++i)
            {
                binary = (i % 4 == 0 ? " " : "") + (number & mask) + binary;
                number >>= 1;
            }

            return binary;
        }


    }
}
