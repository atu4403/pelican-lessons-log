Title: 6 テーマの作成(3)
Date: 2023-09-09 13:26
Category: Lesson
sortorder: 6

ここでは実際にテーマを作成する方法を解説します。今回は実際にこのチュートリアルでも使用されているような`bootstrap5`を使ったテーマを作成します。

## テンプレートを用意する

前の項でも解説しましたが、テーマの作成には以下のファイルが必要です。

<pre><span></span>├── static
│   ├── css
│   └── images
└── templates
    ├── archives.html         // to display archives
    ├── article.html          // processed for each article
    ├── author.html           // processed for each author
    ├── authors.html          // must list all the authors
    ├── categories.html       // must list all the categories
    ├── category.html         // processed for each category
    ├── index.html            // the index (list all the articles)
    ├── page.html             // processed for each page
    ├── period_archives.html  // to display time-period archives
    ├── tag.html              // processed for each tag
    └── tags.html             // must list all the tags. Can be a tag cloud.
</pre>

これを実際に用意するのは大変なので、今回は公式の`simple`テーマをコピーして修正する方法を取ります。
`Pelican`をインストールした場所に`simple`テーマが入っています。私の場合は仮想環境にインストールしているので以下の場所にあります。

`.venv/lib/python3.11/site-packages/pelican/themes/simple`

これをプロジェクトにコピーします。今回は`theme`というディレクトリを作成し、その中にコピーしました。

`theme`ディレクトリの直下には`templates`ディレクトリがあり、その中にテンプレートの`html`ファイルが入っていればOKです。

## テーマのインストール

以下のコマンドで`theme`ディレクトリがインストールできます。`-l`コマンドでインストールされているテーマが一覧できます。

```bash
> pelican-themes -i theme
> pelican-themes -l
BT3-Flat
simple
theme
notmyidea
```

`pelicanconf.py`でテーマを指定すると下準備は完了です。

```bash
THEME = "theme"
```

## テーマの修正

用意したテーマを`bootstrap5`に対応したものに修正します。今回はChatGPTにお願いしました。

ChatGPT plusに加入している方は`Advanced Data Analytics(旧Code Interprete)`を使うと楽ですが、加入していない方もなんとかなると思います。

### ChatGPT plusの場合

ChatGPTで`dvanced Data Analytics`を選択し、`base.html`をアップロードして以下のようなプロンプトを入力します。

```bash
これはPelicanのThemeテンプレートです。bootstrap5にフィットするように書き換えてください。
以下のCDNを使用してください。

CSS	https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css
JS	https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js

以下の条件を考慮してください
- ヘッダーバー
- サイドバー
- レスポンシブデザイン(PC,スマートフォンに対応)
- ヘッダーやサイドバーの内容は簡単なもので構いません。

完成したものをダウンロードできるようにしてください。
```

ダウンロードしたものを`base.html`と差し替えると完成です。他のファイルも同じようにすると終了です。

### ChatGPT plusが使えない場合

以下のようなプロンプトにより修正ができます。

```bash
[ここにbase.htmlの内容をコピーする]

これはPelicanのThemeテンプレートです。bootstrap5にフィットするように書き換えてください。
以下のCDNを使用してください。

CSS	https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css
JS	https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js

以下の条件を考慮してください
- ヘッダーバー
- サイドバー
- レスポンシブデザイン(PC,スマートフォンに対応)
- ヘッダーやサイドバーの内容は簡単なもので構いません。

完成したものをコピーできるようにしてください。
```

ただし、修正したコードの量により省略されてしまうので、分割する必要があります。　　
他のファイルも同じようにすると終了です。

### CSSファイルの追加

bootstrap5によりCSSは追加されていますが、独自のCSSを反映したい場合には以下を参考にしてください。

まず`base.html`を修正します。　　
`bootstrap.min.css`を指定したlinkタグが作成済だと思いますので、その後に追加します。

```base.html
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link
      href="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/css/{{ CSS_FILE }}"
      rel="stylesheet"
    />
```

これにより環境に応じたパスにレンダリングされます。  
`CSS_FILE`はデフォルトで`main.css`となっていますが、`pelicanconf.py`で変更できます。

次に`theme/static/css/main.css`を作成します。

```main.css
@import url('https://fonts.googleapis.com/css2?family=M+PLUS+1+Code:wght@300&family=Noto+Sans+JP:wght@300&display=swap');
body {
  font-family: 'Noto Sans JP', sans-serif;
}
code{
  font-family: 'M PLUS 1 Code', monospace;
}
pre{
  padding:1em; /*内側の余白*/
  margin:001.5em; /*外側の余白*/
  border:solid1px#eaedf2; /*枠線*/
  background:#f3f6fc; /*背景色*/
  color:#54687c; /*文字色*/
}
```

以上で追加したCSSが反映されます。
