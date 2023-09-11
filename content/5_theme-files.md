Title: 5 テーマの作成(2)
Date: 2023-09-08 17:05
Category: Lesson
sortorder: 5

## themeディレクトリの構造について

[公式のドキュメント](https://docs.getpelican.com/en/latest/themes.html#structure)では、以下の説明が書かれています。

```bash
├── static
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

```

> staticにはすべての静的アセットが含まれ、出力テーマのフォルダにコピーされます。上記のファイルシステム・レイアウトにはCSSと画像のフォルダが含まれていますが、これらは単なる例です。必要なものをここに入れてください。
>
>templatesには、コンテンツの生成に使用されるすべてのテンプレートが含まれます。上記のテンプレートファイルは必須です。テーマ作成中に整理整頓がしやすくなるのであれば、独自のテンプレートを追加することもできます。

---

ここで混乱してしまうポイントがあります。

- これらのhtmlファイルの役割
- 生成されるhtmlファイルとの関係

まず勘違いしてしまうのは、レンダリング時にこれらと同名のhtmlファイルが作成されるのではないかということです。半分正解で半分間違いです。

例えば`index.html`は、このテンプレートから`index.html`が生成されます。`tags.html`や`categories.html`も生成されます。  
一方で`article.html`は生成されません。このテンプレートはmarkdown等で用意した記事をレンダリングするために使われて、`記事名.html`などのファイルが作成されます。

さらに、`tag.html`等の、他のページからincludeされる役割のテンプレートもあります。

よって上図のhtmlファイルは、**必要なファイル**と**場合によっては不要なファイル**に分別できます。

### 必須のテンプレート

以下は、Pelicanのテンプレート作成において必要となる、各テンプレート（`.html`ファイル）の説明を抽出したものです。

#### index.html
- これはブログのホームページまたはインデックスで、`index.html`で生成されます。
- ページネーションが有効な場合、次のページは`index{number}.html`に配置されます。

#### author.html
- このテンプレートは存在する各著者ごとに処理され、`AUTHOR_SAVE_AS`設定（デフォルト：`author/{slug}.html`）に従って出力が生成されます。
- ページネーションが有効な場合、次のページはデフォルトで`author/{slug}{number}.html`に配置されます。

#### category.html
- このテンプレートは存在する各カテゴリごとに処理され、`CATEGORY_SAVE_AS`設定（デフォルト：`category/{slug}.html`）に従って出力が生成されます。
- ページネーションが有効な場合、次のページはデフォルトで`category/{slug}{number}.html`に配置されます。

#### article.html
- このテンプレートは各記事ごとに処理され、`ARTICLE_SAVE_AS`設定（デフォルト：`{slug}.html`）に従って出力が生成されます。

#### page.html
- このテンプレートは各ページごとに処理され、`PAGE_SAVE_AS`設定（デフォルト：`pages/{slug}.html`）に従って出力が生成されます。

#### tag.html
- このテンプレートは各タグごとに処理され、`TAG_SAVE_AS`設定（デフォルト：`tag/{slug}.html`）に従って出力が生成されます。
- ページネーションが有効な場合、次のページはデフォルトで`tag/{slug}{number}.html`に配置されます。

#### period_archives.html
- このテンプレートは、`YEAR_ARCHIVE_SAVE_AS`、`MONTH_ARCHIVE_SAVE_AS`、`DAY_ARCHIVE_SAVE_AS`が定義されている場合、それぞれの年、月、日の投稿に対して処理されます。

> この情報は、Pelicanの公式ドキュメントから翻訳、抽出されたものです。
