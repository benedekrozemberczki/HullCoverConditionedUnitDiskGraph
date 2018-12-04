import random
import imageio
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

class ConncaveHullUnitDiskGraphGenerator(object):


    def __init__(self, args):
        self.args = args
        self.image = imageio.imread(self.args.input_path)
        self.points = {i: (random.uniform(0, 1), random.uniform(0, 1)) for i in range(self.args.point_number)}
    

    def keep_point(self, point):
    
        x = int(point[0]*self.image.shape[1])
        y = int((1-point[1])*self.image.shape[0])
        if self.image[y,x,0] == 0:
            keep = True
        else:
            keep = False
        return keep

    def create_graph(self):
        self.points = {node: point for node, point in self.points.items() if self.keep_point(point)}
        self.remaining_nodes = list(self.points.keys())
        self.reindexed_nodes = {node:index for index, node in enumerate(self.remaining_nodes)}
        self.points = {self.reindexed_nodes[k]:v for k, v in self.points.items()}
        self.graph = nx.random_geometric_graph(len(self.points.keys()), self.args.radius, pos=self.points)

    def plot_graph(self):

        nx.draw(self.graph,
                self.points,
                with_labels=False,
                linewidths=self.args.line_width,
                alpha=self.args.alpha,
                node_size=self.args.node_size,
                width=self.args.line_width,
                edge_color="gray",
                node_color=self.args.node_color)
        plt.savefig(self.args.output_image, format='PNG', dpi=self.args.dpi)
        plt.close()

    def save_graph(self):
        pd.DataFrame(self.graph.edges(),columns = ["node_1","node_2"], index = None).to_csv(self.args.output_edges)
