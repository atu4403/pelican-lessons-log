Title: 8 GitHubPagesへデプロイする
Date: 2023-09-10 14:00
Category: Lesson
sortorder: 8

ここではgithub pagesへデプロイする方法を解説します。

## 基本的な手順

### 1. `publishconf.py`のSITEURLを設定

'publishconf.py'の`SITEURL`を設定することで、リンクが本番環境用のものになります。

GitHubPagesのURLは`https://{アカウント名}.github.io/{リポジトリ名}`となります。

### 2. `make publish`

`make publish`コマンドの実行により`publishconf.py`の設定からビルドが行われます。デフォルトでは一旦`output`ディレクトリを削除してからビルドするようになっているので、`make clean`を実行する必要はありません。

### 3. git add & commit

ここまで問題がなければcommitしておきます。

### 4. githubリポジトリの作成とpush

githubにpushします。github側にリポジトリを作っていないのなら、`gh repo create`が便利です。(ghコマンドは別途インストールが必要です)

### 5. `make github`(`ghp-import`のインストールが必要)

`make github`の実行により、面倒な設定を飛ばしてGitHubPagesのデプロイができます。ただし、内部的には`ghp-import`というコマンドを実行しているので、このインストールが必要になります。

```bash
rye add ghp-import
rye sync
make github
```

`https://{アカウント名}.github.io/{リポジトリ名}`にアクセスしてサイトが表示されるか確認してください。

## 個人的なベストプラクティス

上記で解説した方法は更新時に若干の手間がかかります。

1. `make publish`
2. git add & commit & push
3. `make github`

makeコマンドを2回行うのが冗長に感じます。また、再度ローカルでの確認を行うには`make clean`と`make devserver`を実行する必要があり、これも若干面倒です。

GitHubPagesにサイトを構築する具体的な方法は、`gh-pages`ブランチにコンテンツを配置することです。  
しかし`main`ブランチの`docs`ディレクトリからコンテンツを読み込む設定もあります。
この設定を行えば、上記3の工程は不要になります。

### 設定方法

```bash
#　修正前
publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)
```

```bash
#　修正後
publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(BASEDIR)/docs" -s "$(PUBLISHCONF)" $(PELICANOPTS)
```

1. `Makefile`を上記のように書き換える
1. `.gitignore`に`output/`を追加
1. GitHubの設定を変更します。`settings` -> `pages` -> `Build and deployment`の`Branch`を`main`,`/docs`に変更してsaveすると完了です。

これで`make publish`すると`docs`ディレクトリにコンテンツがビルドされます。
そのままcommit & pushするだけで自動的にGitHubPagesも更新されます。

`make devserver`では`output`ディレクトリにコンテンツがビルドされるので、開発用として使えます。  
`output`ディレクトリをgit管理する必要は無いので外しています。

注意点

- キャッシュの問題で`docs`ディレクトリが作成されない時は`pelican --ignore-cache`として実行すると反映される。
- `make publish`したものをpushしてからGitHubPagesに反映されるまで数分かかる。
