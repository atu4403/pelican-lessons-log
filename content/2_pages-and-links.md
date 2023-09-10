Title: 2 静的ページとリンク
Date: 2023-09-07 12:23
Category: Lesson
sortorder: 2

## 注意事項

ページの追加は`pelican content`を再度実行することで反映される。開発サーバーの起動に`--autoreload` をしていても即時反映はされない。

## 静的ページの作成

ブログ等の日々更新するものではなく、`about`や`contact`等の静的ページは`contact/pages`ディレクトリに配置する。これはナビゲーションメニューに表示される。

##　リンク

```md
[a link relative to the current file]({filename}1_my-first-article.md)  
[a link relative to the content root]({filename}/1_my-first-article.md)  
```

[a link relative to the current file]({filename}1_my-first-article.md)  
[a link relative to the content root]({filename}/1_my-first-article.md)  

ここではmdファイルへのリンクになっているが、pelicanのビルドにより生成されたhtmlへのリンクに自動修正される。

この条件として、単純に`{filename}`が変換されるのではなく、markdown記法でのlinkであることをチェックして変換していると思われる。

`{filename}/1_my-first-article.md`
{filename}/1_my-first-article.md (変換されない)

`({filename}/1_my-first-article.md)`
({filename}/1_my-first-article.md) (変換されない)

`[link]({filename}/1_my-first-article.md)`
[link]({filename}/1_my-first-article.md) (リンク先がhtmlに変換されている)

また、リンク先のファイルが存在しない場合は変換が行われない。

`[link]({filename}/unknown.md)`
[link]({filename}/unknown.md) (リンク先がmdのまま)

## 静的ファイルへのリンク

`content/images/onepiece06_chopper.png`を表示する場合。

```md
![いらすとやさんのチョッパー]({static}/images/onepiece06_chopper.png)
```

![いらすとやさんのチョッパー]({static}/images/onepiece06_chopper.png)

## {filename}や{static}について

`{static}`はそのままのファイル名を配置するのに対して、`{filename}`はmdやrstファイルから生成されたhtmlのパスに変換する。

