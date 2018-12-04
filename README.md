ConcaveHullUnitDiskGraph
============================================
<p align="justify">
A generator for unit disk graphs conditioned on concave hull cover. Tex text text.
  
</p>
<div style="text-align:center"><img src ="concave.jpeg" ,width=720/></div>

### Requirements

The codebase is implemented in Python 3.5.2. package versions used for development are just below.
```
networkx          1.11
tqdm              4.28.1
numpy             1.15.4
pandas            0.23.4
texttable         1.5.0
scipy             1.1.0
argparse          1.1.0
sklearn           0.20.0
```
### Datasets

The code takes an input graph in a csv file. Every row indicates an edge between two nodes separated by a comma. The first row is a header. Nodes should be indexed starting with 0. Sample graphs for the `Twitch Brasilians` ,`Wikipedia Chameleons` and `Wikipedia Giraffes` are included in the  `input/` directory. 

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
Creating a BANE embedding of the default dataset with 128 dimensions and approximation order 1.

```
python src/main.py --dimensions 128 --order 1
```

Creating a BANE embedding of the default dataset with asymmetric mixing.

```
python src/main.py --gamma 0.1
```

Creating an embedding of an other dense structured dataset the `Wikipedia Giraffes`. Saving the output in a custom folder.

```
python src/main.py --edge-path input/giraffe_edges.csv --feature-path input/giraffe_features.csv --output-path output/giraffe_bane.csv --features dense
```
