Title: 3 テーマの設定
Date: 2023-09-07 14:15
Category: Lesson
sortorder: 3

## テーマの設定

`pelican-themes`コマンドが用意されている。

### 使用可能なテーマの確認

```bash
> pelican-themes -l
simple
notmyidea
```

### テーマのインストール

テーマを使用するためにはインストール、もしくはテーマを置いているパスを指定する必要がある。
また、インストールするためにも、テーマを置いているパスを指定する必要がある。

どちらにしてもシステム内にテーマを保存する必要があるので、試しに以下のリポジトリを丸ごとcloneした。

[GitHub - getpelican/pelican-themes: Themes for Pelican](https://github.com/getpelican/pelican-themes)

上記のリポジトリからインストールしたいテーマのパスを指定して以下を実行。

```bash
> pelican-themes --install ~/ghq/github.com/getpelican/pelican-themes/BT3-Flat
> pelican-themes -l
BT3-Flat
simple
notmyidea
```

### テーマを使用する

`pelicanconf.py`に設定を追加すると、テーマが反映される。

```pelicanconf.py
THEME = "BT3-Flat"
```
