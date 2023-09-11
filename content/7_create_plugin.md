Title: 7 プラグインの作成
Date: 2023-09-10 12:39
Category: Lesson
sortorder: 7

ここではプラグインを作成する例を解説します。同時に、動的にコンテンツを作成する方法も紹介します。

## プラグインとは

Pelicanはプラグインをサポートしており、利用すると以下のようなことができます。

- 新しいコンテンツタイプの追加
- カスタムフィルターやテンプレートの統合
- 外部データの取り込み
- SEO対策の自動生成
- カスタムURLの生成
- サイトのパフォーマンス向上
- カスタムメタデータや設定の追加

これらの機能をプラグインを作成して追加できます。プラグインはPythonで記述され、特定のシグナルにフックしてカスタム処理を実行します。詳細な情報はPelicanの公式ドキュメントを参照してください。

## コード例

今回は動的にコンテンツを作成する例を紹介します。

`__init__.py`を作成します。

```python
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from pelican import signals
from pelican.settings import read_settings
from unidecode import unidecode

unique_prefix = "_auto_gen_"
content_dir = read_settings("pelicanconf.py")["PATH"]


def get_api_mock():
    return {
        "diarys": [
            {
                "title": "日記(1日目)",
                "dt": "2023-09-01",
                "categorie": "diary",
                "content_title": "content 1",
                "contents": [
                    {"time": "9:00", "body": "起床"},
                    {"time": "23:00", "body": "就寝"},
                ],
            },
            {
                "title": "日記(2日目)",
                "dt": "2023-09-02",
                "categorie": "diary",
                "content_title": "content 2",
                "contents": [
                    {"time": "5:00", "body": "起床"},
                    {"time": "22:00", "body": "就寝"},
                ],
            },
        ]
    }


def to_valid_filename(input_string, fmt=None):
    # Unicode文字列をASCIIに変換
    valid_filename = unidecode(input_string)
    # 空白をアンダースコアに置換
    valid_filename = valid_filename.replace(" ", "_")

    # 拡張子が指定されている場合、拡張子を付与
    if fmt:
        valid_filename = f"{valid_filename}.{fmt}"

    return unique_prefix + valid_filename


def generate_md(generator):
    data = get_api_mock()
    env = Environment(loader=FileSystemLoader("plugins/sample-generator/templates"))
    template = env.get_template("sample01.md")
    for i, diary in enumerate(data["diarys"]):
        # print("diary: ", content_dir)
        diary["sortorder"] = (i + 1) * 10
        filename = to_valid_filename(diary["title"], "md")
        rendered_template = template.render(**diary)
        save_path = Path(content_dir) / filename
        save_path.write_text(rendered_template)


def delete_md(generator):
    # Create a Path object for the content directory
    content_path = Path(content_dir)

    # Check if the content directory exists
    if not content_path.exists():
        print(f"Content directory {content_dir} does not exist.")
        return

    # Iterate through all the files in the content directory
    for file_path in content_path.glob("*"):
        if file_path.name.startswith(unique_prefix):
            try:
                file_path.unlink()
                print(f"Deleted {file_path}")
            except Exception as e:
                print(f"An error occurred while deleting {file_path}: {e}")


# Pelicanのシグナルにフックしてプラグインを実行
def register():
    signals.initialized.connect(generate_md)
    signals.finalized.connect(delete_md)

```

色々と書いていますが、重要なのはregister関数です。

```python
# Pelicanのシグナルにフックしてプラグインを実行
def register():
    signals.initialized.connect(generate_md)
    signals.finalized.connect(delete_md)
```

initialized、つまりpelicanによりビルドが行われる前に`generate_md`関数が呼ばれます。  
finalized、つまりビルドが行われた後に`delete_md`関数が呼ばれます。

この例では動的にmarkdownファイルを生成して`content`ディレクトリに配置しています。pelicanによるビルドが完了した後で、生成したmarkdownファイルを削除しています。

## 配置例

プロジェクト直下(contentディレクトリと同じ階層)に`plugins`というディレクトリを作成し、その中に`sample-generator`ディレクトリを作成しています。`sample-generator`がプラグイン名になります。

```bash
plugins/
└── sample-generator
    ├── __init__.py
    └── templates
        └── sample01.md
```

`pelicanconf.py`に以下の記述を追加すると、pelicanのビルド時に実行されるようになります。

```python
# プラグインが存在するディレクトリのパスを指定
PLUGIN_PATHS = ["plugins"]

# 使用するプラグインの名前をリストに追加
PLUGINS = ["sample-generator"]

```
