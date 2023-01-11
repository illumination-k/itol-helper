# Itol helper

[Itol](https://itol.embl.de)へのデータのアップロードと、よく使用されるデータセットの生成を簡易に行えるようにするツールです。

## Install

`poetry`をpackage managerとして利用しているため必要であれば`pip install poetry`を実行してください。

```bash
poetry install
```

## Run

### Upload

系統樹とItolのスタイルファイルを含んだディレクトリをアップロードします。
ディレクトリには系統樹とItolのスタイルファイル以外を含まないようにしてください。

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

configファイルをもとに、LabelにAliasを追加します。

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

configファイルをもとに、Labelの色を変更します。

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

configファイルをもとに、branch symbolを生成します。

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

## Config

itolのスタイルファイルを生成するときに必要なJSON形式のファイルです。

### Colormap

`colormap`フィールドに正規表現をKey、カラーコードをValueとするオブジェクトを指定します。Label、barnch-symbolsの色に対応します。

### Id to Name

`id_to_name`フィールドにノードの値をKey, 表示したい名前をValueとするオブジェクトを指定します。Aliasを作成する時に使用します。

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
