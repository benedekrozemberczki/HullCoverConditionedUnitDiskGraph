import random
import imageio
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def ranp(x, y):
    """
    Coordinate generation.
    """
    return random.uniform(x, y)

class HullCoverConditionedUnitDiskGraphGenerator(object):
    """
    Unit disk graph generation condition on image pixels.
    """
    def __init__(self, args):
        """
        Setting up the graph generator.
        :param args: Arguments object.
        """
        self.args = args
        self.image = imageio.imread(self.args.input_path)
        self.points = {i: (ranp(0, 1), ranp(0, 1)) for i in range(self.args.point_number)}

    def keep_point(self, point):
        """
        Checking whether a point is covered in the image.
        """
        y = int((1-point[1])*self.image.shape[0])
        x = int(point[0]*self.image.shape[1])
        if self.image[y, x, 0] == 0:
            keep = True
        else:
            keep = False
        return keep

    def create_graph(self):
        """
        Creating a graph by first dropping the points.
        """
        self.points = {n: p for n, p in self.points.items() if self.keep_point(p)}
        self.remaining_nodes = list(self.points.keys())
        self.reindexed_nodes = {n: i for i, n in enumerate(self.remaining_nodes)}
        self.points = {self.reindexed_nodes[k]: v for k, v in self.points.items()}
        self.graph = nx.random_geometric_graph(len(self.points.keys()),
                                               self.args.radius,
                                               pos=self.points)

    def plot_graph(self):
        """
        Plotting the graph and saving the plot.
        """
        nx.draw(self.graph,
                self.points,
                with_labels=False,
                linewidths=self.args.line_width,
                alpha=self.args.alpha,
                node_size=self.args.node_size,
                width=self.args.line_width,
                edge_color="gray",
                node_color=self.args.node_color)
        plt.savefig(self.args.output_image, format="PNG", dpi=self.args.dpi)
        plt.close()

    def save_graph(self):
        """
        Saving the graph in an edge list format.
        """
        cols = ["node_1", "node_2"]
        edges = [edge for edge in self.graph.edges()]
        pd.DataFrame(edges, columns=cols, index=None).to_csv(self.args.output_edges)
