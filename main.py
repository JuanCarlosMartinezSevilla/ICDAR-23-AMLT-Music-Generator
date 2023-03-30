import argparse, random
from data import Data
from generator import Generator

class Main:
    def main(args):
        #random.seed(10)
        Data.set_globals(args)
        
        score = {}
        score["measure"] = Data.measure
        score["number_measures"] = args.measures

        Generator.generator(args, score)


    def argument_parser():
        parser = argparse.ArgumentParser(description=__doc__, add_help=True,
                                            formatter_class=argparse.RawDescriptionHelpFormatter)

        parser.add_argument("-m", "--measures", required=True, type=int,
                                help="Number of generated measures per melody")
        parser.add_argument("-v", "--voices", required=False, type=int, default=1,  choices=range(1,3),
                                help="Number of voices per staff")
        parser.add_argument("-l", "--lyrics", required=False, type=int, default=0, 
                                help="Number of lyric lines")
        parser.add_argument("-c", "--camera", action='store_true',
                                help="Applies camera filter to resultant images")
        parser.add_argument("-bg", "--background", action='store_true',
                                help="Changes resultant images' background colors")


        return parser

if __name__ == '__main__':
    
    parser = Main.argument_parser()
    args = parser.parse_args()

    print(args)
    Main.main(args)