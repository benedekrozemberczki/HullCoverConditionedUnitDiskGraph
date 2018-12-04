Hull Cover Conditioned Unit Disk Graph Generator
==================================================
<p align="justify">
A generator for unit disk graphs conditioned on hull cover. The model first generates uniformly distributed points in 2 dimensions. Based on the input image does pointw which are not covered with black are deleted from the initial set of points. Using the remaining point a fixed r-radius unit disk graph is grown. Finally, the edge list of the graph is saved with a large resolution plot of the graph.
  
</p>
<div style="text-align:center"><img src ="mi.jpg" ,width=720/></div>

### Requirements

The codebase is implemented in Python 3.5.2. package versions used for development are just below.
```
networkx          1.11
pandas            0.23.4
argparse          1.1.0
```
### Datasets

The code takes an input black and white jpeg file. Every pixel indicates whether the data point generated randomly is covered by the image or not. Not covered points are dropped. The `/input/` folder contains a Mickey Mouse head, a T-rex and a flower as an example input image.

### Options

Learning of the embedding is handled by the `src/main.py` script which provides the following command line arguments.

#### Input and output options

```
  --edge-path    STR     Input graph path.           Default is `input/ptbr_edges.csv`.
  --feature-path STR     Input Features path.        Default is `input/ptbr_features.json`.
  --output-path  STR     Embedding path.             Default is `output/ptbr_bane.csv`.
```

#### Model options

```
  --features               STR         Structure of the feature matrix.       Default is `sparse`. 
  --dimensions             INT         Number of embeding dimensions.         Default is 48.
  --order                  INT         Order of adjacency matrix powers.      Default is 1.
  --binarization-rounds    INT         Number of power interations.           Default is 10.
  --approximation-rounds   INT         Number of CDC interations.             Default is 5.
  --alpha                  FLOAT       Regularization parameter.              Default is 0.7.
  --gamma                  FLOAT       Weisfeiler-Lehman mixing parameter.    Default is 0.1.  
```

### Examples

The following commands learn a graph embedding and write the embedding to disk. The node representations are ordered by the ID.

Creating a BANE embedding of the default dataset with the default hyperparameter settings. Saving the embedding at the default path.

```
python src/main.py
```

Creating an embedding of an other dense structured dataset the `Wikipedia Giraffes`. Saving the output in a custom folder.

```
python src/main.py --input-path input/flower.jpeg --output-image output/plot/flower.png --output-edges output/edges/flower.edges --node-color "red" --radius 0.07 --alpha 0.5
```
