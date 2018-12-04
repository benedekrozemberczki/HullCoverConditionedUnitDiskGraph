from hull_cover_graph import HullCoverConditionedUnitDiskGraphGenerator
from parser import parameter_parser

def main(args):

    machine = HullCoverConditionedUnitDiskGraphGenerator(args)
    machine.create_graph()
    machine.plot_graph()
    machine.save_graph()

if __name__ == "__main__":
    args = parameter_parser()
    main(args)
