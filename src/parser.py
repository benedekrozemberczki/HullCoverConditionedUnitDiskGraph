import argparse

def parameter_parser():

    """
    A method to parse up command line parameters. By default it gives an embedding of the partial NCI1 graph dataset.
    The default hyperparameters give a good quality representation without grid search.
    Representations are sorted by ID.
    """

    parser = argparse.ArgumentParser(description = "Run Graph2Vec.")


    parser.add_argument('--input-path',
                        nargs = '?',
                        default = './input/trex.jpg',
	                help = 'Input concave hull image.')

    parser.add_argument('--output-edges',
                        nargs = '?',
                        default = './output/edges/trex_edges.csv',
	                help = 'Edge list path.')

    parser.add_argument('--output-image',
                        nargs = '?',
                        default = './output/plot/trex_graph.png',
	                help = 'Edge list path.')

    parser.add_argument('--node-color',
                        nargs = '?',
                        default = 'green',
	                help = 'Node color.')

    parser.add_argument('--point-number',
                        type = int,
                        default = 10000,
	                help = 'Number of data points before shaving. Default is 10,000.')

    parser.add_argument('--radius',
                        type = float,
                        default = 0.04,
	                help = 'Unit disk radius. Default is 0.04.')

    parser.add_argument('--line-width',
                        type = float,
                        default = 0.2,
	                help = 'Edge width. Default is 0.2.')

    parser.add_argument('--alpha',
                        type = float,
                        default = 0.3,
	                help = 'Color strength. Default is 0.3.')

    parser.add_argument('--node-size',
                        type = float,
                        default = 12.0,
	                help = 'Node size. Default is 12.0.')
    
    return parser.parse_args()
