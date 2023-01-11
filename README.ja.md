# Itol helper

[Itol](https://itol.embl.de)へのデータのアップロードと、よく使用されるデータセットの生成を簡易に行えるようにするツールです。

## Install

`poetry`をpackage managerとして利用しているため必要であれば`pip install poetry`を実行してください。

```bash
poetry install
```

## Run

### Upload

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

`fasta/phy`からitolのalignment styleに変換

```
usage: ih alignment [-h] -i INPUT [-l LABEL]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        file contained multple alignment. fasta and phy are supported
  -l LABEL, --label LABEL
```
