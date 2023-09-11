Title: 1 My First Article
Date: 2023-09-07 11:25
Category: Lesson
sortorder: 1

## ryeの導入

```bash
# プロジェクトディレクトリの作成と移動をしておく
rye init
rye add "pelican[markdown]"
rye sync
```

## 初期化

```bash
> pelican-quickstart
Welcome to pelican-quickstart vunknown.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.

    
> Where do you want to create your new web site? [.] 
> What will be the title of this web site? pelican-lessons-log
> Who will be the author of this web site? atu4403
> What will be the default language of this web site? [ja] 
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10] 
> What is your time zone? [Europe/Rome] Asia/Tokyo
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) N
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
> Do you want to upload your website using Rackspace Cloud Files? (y/N) N
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) N
Done. Your new project is available at /Users/atu/ghq/github.com/atu4403/pelican-lessons-log
```

## 記事の作成

```bash
# 最初の記事の作成
vi content/my-first-article.md
```

## サイトの生成とサーバーの起動

```bash
pelican content
pelican --listen
# port指定
# pelican -p=8200 --listen
# 保存時に自動でビルド
# pelican -p=8200 --autoreload --listen
```

[localhost](http://localhost:8000/)で確認できます。

`pelican-quickstart`の際にmakefileを作成しておけば`pelican`コマンドに加えて`make`も使うことができます。

```bash
# 開発用htmlの生成
make html

# ビルドしたファイルの削除
make clean

# 本番用htmlの生成
make publish

# 保存時に自動でビルド
make regenerate

# 開発サーバーの起動
make serve

# 開発サーバーの起動と保存時に自動でビルド
make devserver

# GitHubPagesへデプロイする(ghp-importのインストールが必要)
make github
```

## pelicanconf.pyとpublishconf.py

`pelican-quickstart`を実行すると`pelicanconf.py`は自動で作成されますが、以下の記述を追加しました。

```python
PORT = 8200
SITEURL = "http://localhost:8200"
```

`pelicanconf.py`は開発環境用の設定になります。

デフォルトでは`PORT = 8000`ですが、他の開発サーバーと被りそうなので変更しています。また、それに合わせて`SITEURL`も設定しています。これにより適切なリンクがレンダリングされます。

`publishconf.py`は本番環境用の設定になります。とはいえ、開発環境用の設定と異なる項目は多くないので、`publishconf.py`は`pelicanconf.py`を読み込み、それを上書きする仕様になっているようです。

本番環境用の`SITEURL`はこちらに書きます。
