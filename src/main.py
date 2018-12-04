from concave_hull_graph import ConncaveHullUnitDiskGraphGenerator
from parser import parameter_parser

def main(args):

    machine = ConncaveHullUnitDiskGraphGenerator(args)
    machine.create_graph()
    machine.plot_graph()
    machine.save_graph()

if __name__ == "__main__":
    args = parameter_parser()
    main(args)
