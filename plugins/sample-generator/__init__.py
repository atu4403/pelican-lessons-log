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
