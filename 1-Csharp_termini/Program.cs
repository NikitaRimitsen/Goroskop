using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;//using-import(python)

namespace _1_Csharp_termini//менят название нельзя
{
    class Program//трогать нельзя
    {
        static void Main(string[] args)//если её не будет , ничего не запустится ; void - вызывает функции, static void - def(python)
        {
            Console.BackgroundColor = ConsoleColor.Gray;//BackgroundColor-свойство,фон; свойство должно чему нибудь равно;
            Console.ForegroundColor = ConsoleColor.Red;//цвет текста
            Console.Clear();//Clear-очистка (и закрашивает весь фон)
            Console.WriteLine("Hello world!"); //Line - переносит мышку на новую строчку, после предложения
            Random rnd = new Random();//конструктор-это метод,функция; rnd-название переменной
            Console.WriteLine("jah-random, ei-ise sisestan number");
            string soov = Console.ReadLine();//soov-переменная, input(python), (то что будет веденно с клавитуры)
            int num = 0;//num-переменная
            if (soov=="jah")
            {
                num = rnd.Next(1, 7);//радомно выбирает цифры; //num = rnd.Next(1, 1);//num-название переменной; Next-свойство

            }
            else
            {
                try
                {
                    num = Convert.ToInt32(Console.ReadLine());//Convert.ToInt32- всё что будеть веденно с клавиатуры, будет превращена в цифры
                    Console.WriteLine("Päeva number: {0}", num.ToString());
                }
                catch (SystemException)
                {
                }

            }
            Console.WriteLine("Päeva number: {0}", num.ToString());//Console.WriteLine("Päeva number: {0}", num.ToString());//{0}-она будет подставлена сюда, то что после скобки; num.ToString()-она будет превращена из int в str 

            //int num = rnd.Next(1, 8);//num-название переменной; Next-свойство
           
            string nimetus = "";
            switch (num)
            {
                case 1: nimetus = "esmapäev"; break;// case - варианты значения; break-прервала, закончила, остонавливает
                case 2: nimetus = "teisipäev"; break;//nimetus - переменная
                case 3: nimetus = "kolmapäev"; break;
                case 4: nimetus = "neljapäev"; break;
                case 5: nimetus = "reede"; break;
                case 6: nimetus = "laupäev"; break;
                case 7: nimetus = "pühapäev"; break;
                default://else(python)
                    nimetus = "Viga!";//если нет цифр, которые не указаны-будет писаться 
                    break;
            }
            
            Console.WriteLine(nimetus);//Console.WriteLine-выводит информацию на экран; nimetus-переменная
            StreamWriter filesse = new StreamWriter(@"..\..\andmed.txt", true);//filesse-переменная;..\..\-выйдет из двух папок; true-будет добавлять (новые файлы);если по русски - то надо писать (encoding-8-utf)
            filesse.WriteLine("Number oli {0}, päev on {1}", num.ToString(), nimetus);//место {0} поставит в num, место {1} поставит в nimetus
            filesse.Close();//закрывает файл
            Console.WriteLine("Failis oli salvestatud: Number oli " + num.ToString() + " päev on " + nimetus);
            StreamReader filest = new StreamReader(@"..\..\andmed.txt");
            string a = filest.ReadToEnd();//ReadToEnd()-читает до конца, всё что видит
            Console.WriteLine("Failis oli seda: \n" + a);//  \n-новая строка

            Console.ReadLine();//Не закрывает программу
        }
    }
}
