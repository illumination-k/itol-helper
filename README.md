# Itol helper

A tool that simplifies uploading data to Itol and generating commonly used datasets.

## Install

Since poetry is used as the package manager, run pip install poetry if necessary.

```bash
poetry install
```

## Run

### Upload

Upload a directory containing a phylogenetic tree and Itol style files. Make sure the directory does not contain anything other than the tree and style files.

```
usage: ih upload [-h] [--api-key API_KEY] -p PROJECT_NAME [--tree-name TREE_NAME] [--tree-description TREE_DESCRIPTION] -d DIR

options:
  -h, --help            show this help message and exit
  --api-key API_KEY     Using ITOL_APIKEY environment variable for default
  -p PROJECT_NAME, --project-name PROJECT_NAME
  --tree-name TREE_NAME
  --tree-description TREE_DESCRIPTION
  -d DIR, --dir DIR
```

#### Example

```bash
poetry run ih upload -d /path/to/upload_dir --api-key $your_api_key --project-name $your_project_name
```

### text

Add aliases to Labels based on a config file.

```
usage: ih text [-h] -i IDS -c CONFIG [-l LABEL]

options:
  -h, --help            show this help message and exit
  -i IDS, --ids IDS     file contained ID (nwk, fasta, phy or txt)
  -c CONFIG, --config CONFIG
                        config file
  -l LABEL, --label LABEL
```

### style

Change the color of Labels based on a config file.

```
usage: ih style [-h] -i IDS -c CONFIG [-l LABEL]

options:
  -h, --help            show this help message and exit
  -i IDS, --ids IDS     file contained ID (nwk, fasta, phy or txt)
  -c CONFIG, --config CONFIG
                        config file
  -l LABEL, --label LABEL
```

### branch-symbols

Generate branch symbols based on a config file.

```
usage: ih branch-symbols [-h] -i IDS -c CONFIG [-l LABEL]

options:
  -h, --help            show this help message and exit
  -i IDS, --ids IDS     file contained ID (nwk, fasta, phy or txt)
  -c CONFIG, --config CONFIG
                        config file
  -l LABEL, --label LABEL
```

### alignment

Convert fasta or phy format to itol alignment style.

```
usage: ih alignment [-h] -i INPUT [-l LABEL]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        file contained multple alignment. fasta and phy are supported
  -l LABEL, --label LABEL
```

## Config

A JSON-formatted file required to generate Itol style files.

### Colormap

Specify an object with regular expressions as Keys and color codes as Values in the colormap field. This corresponds to the colors of Labels and branch-symbols.

### Id to Name

Specify an object with node values as Keys and the desired display names as Values in the id_to_name field. This is used when creating aliases.

### Example

```json
{
  "colormap": {
    "^Mp": "#4b0082",
    "^Pp": "#32cd32",
    "^Apun": "#800000",
    "^Smoe": "#00bfff",
    "^Azfi|^Sacu": "#2f4f4f",
    "^MA": "#66cdaa",
    "^Nycol|^evm": "#adff2f",
    "^LOC": "#ffb6c1",
    "^AT": "#daa520",
    "^jgi": "#696969",
    "^Cre|^Ol": "#000000"
  },
  "id_to_name": {
    "AT1G29160.1": "AtCOG1",
    "AT1G26790.1": "AtCDF6",
    "AT1G69570.1": "AtCDF5",
    "AT2G46590.1": "AtDAG2",
    "AT2G34140.1": "AtCDF4",
    "AT3G47500.1": "AtCDF3",
    "AT5G39660.1": "AtCDF2",
    "AT5G62430.1": "AtCDF1"
  }
}
```
