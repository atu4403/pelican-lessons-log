Title: 8 GitHubPagesへデプロイする
Date: 2023-09-10 14:00
Category: Lesson
sortorder: 8

ここではgithub pagesへデプロイする方法を解説します。

1. 'publishconf.py'のSITEURLを設定
2. `make publish`
3. git add & commit
4. githubリポジトリの作成とpush(`gh repo create`が便利)
5. `make github`(`ghp-import`のインストールが必要)

## 1. 'publishconf.py'のSITEURLを設定

'publishconf.py'の`SITEURL`を設定することで、リンクが本番環境用のものになります。

GitHubPagesのURLは`https://{アカウント名}.github.io/{リポジトリ名}`となります。

## 2. `make publish`

このコマンドにより`publishconf.py`の設定からビルドが行われます。デフォルトでは一旦`output`ディレクトリを削除してからビルドするようになっているので、`make clean`を実行する必要はありません。

## 3. git add & commit

ここまで問題がなければcommiしておきます。

## 4. githubリポジトリの作成とpush

githubにpushします。github側にリポジトリを作っていないのなら、`gh repo create`が便利です。(ghコマンドは別途インストールが必要です)

## 5. `make github`(`ghp-import`のインストールが必要)

`make github`を行うことで面倒な設定を飛ばしてGitHubPagesのデプロイができます。ただし、内部的には`ghp-import`というコマンドを実行しているので、このインストールが必要になります。

```bash
rye add ghp-import
rye sync
make github
```

`https://{アカウント名}.github.io/{リポジトリ名}`にアクセスしてサイトが表示されるか確認してください。
