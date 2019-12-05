"""Running the generator."""

from param_parser import parameter_parser
from hull_cover_graph import HullCoverConditionedUnitDiskGraphGenerator

def main(args):
    """
    Plotting and saving the graph created.
    """
    machine = HullCoverConditionedUnitDiskGraphGenerator(args)
    machine.create_graph()
    machine.plot_graph()
    machine.save_graph()

if __name__ == "__main__":
    args = parameter_parser()
    main(args)
