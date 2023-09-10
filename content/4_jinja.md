Title: 4 テーマの作成(1)
Date: 2023-09-08 14:57
Category: Lesson
sortorder: 4

## はじめに

このチュートリアルでは、Pelicanのテーマ作成において重要な役割を果たすJinja2について解説します。Jinja2はHTMLテンプレートエンジンであり、HTMLを効率よく生成するための土台となります。また、このページはChatGPTにより作成しています。

---

## PelicanのテーマとJinja2

Pelicanのテーマ作成にはJinja2が広く使われています。Jinja2はHTMLテンプレートエンジンであり、静的なHTMLを動的に生成するための強力なツールです。

---

## Jinja2の基本概念

### `extends`と`block`

`extends`はテンプレートの継承を行うための構文です。`block`はその中でコンテンツをオーバーライドできる領域を定義します。これらはテンプレートの基本部分を作成し、その上で特定の部分だけを変更するといった用途に適しています。

### `include`

`include`は特定のテンプレートをインポートするための構文です。これは「パーツとして複数箇所で使い回すのに適している」と言えます。例えば、ヘッダーやフッターなど、複数のページで共通の要素を持つ場合に便利です。

---

## 実例を通しての解説

以下のコードブロックを例に取ります。

### base.html

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <title>{{ page_title }}</title>
  </head>
  <body>
    {% include "header.html" %}
    <div id="content">{% block content %}{% endblock %}</div>
    {% include "footer.html" %}
  </body>
</html>
```

### header.html

```html
<header>これはヘッダーです</header>
```

### footer.html

```html
<footer>これはフッターです</footer>
```

### page1.html

```html
{% extends "base.html" %}
{% block content %}
<h2>ページのコンテンツ</h2>
<p>ここにページの内容が表示されます。</p>
{% endblock %}
```

## page1.htmlのレンダリング過程

`page1.html`は`base.html`を継承しています。この継承は`{% extends "base.html" %}`というJinja2の構文によって行われます。この構文があることで、`base.html`の内容が`page1.html`に取り込まれるわけです。

### `extends`と`block`

`{% block content %}`と`{% endblock %}`の間に書かれた内容は、`base.html`内の同名の`block`（この場合は`content`）をオーバーライド（上書き）します。具体的には、`base.html`の`{% block content %}{% endblock %}`が`page1.html`の`{% block content %} ... {% endblock %}`で指定された内容に置き換わります。

### `include`

`{% include "header.html" %}`と`{% include "footer.html" %}`は、それぞれ`header.html`と`footer.html`の内容をその位置に挿入します。これによって、ヘッダーとフッターが各ページで一貫したものになります。

## レンダリング済のcontent.html

テンプレートのレンダリングを行った後の`content.html`は以下のようになります。

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <title>（ここに実際のページタイトルが入ります）</title>
  </head>
  <body>
    <header>これはヘッダーです</header>
    <div id="content">
        <h2>ページのコンテンツ</h2>
        <p>ここにページの内容が表示されます。</p>
    </div>
    <footer>これはフッターです</footer>
  </body>
</html>
```

この`content.html`は、`base.html`の骨格に`page1.html`で指定された内容が埋め込まれ、さらに`header.html`と`footer.html`がそれぞれ適切な位置に挿入された結果です。

以上が`page1.html`のレンダリング過程とその結果になります。このようにJinja2は非常に強力で、テンプレートの再利用や部品化を容易にしてくれます。

---

## テンプレートと純粋なHTMLの違い

Jinja2テンプレートと純粋なHTMLファイルは、拡張子が`.html`である点では同じですが、内容と用途が異なります。この違いが初めての方には混乱を招く可能性がありますので、以下で詳しく解説します。

### Jinja2テンプレート（base.html, header.html, page1.html）

- **拡張子**: `.html`
- **内容**: HTMLに加え、Jinja2の構文（`{% ... %}`, `{{ ... }}`など）が含まれる。
- **用途**: レンダリングを通じて最終的なHTMLを生成するための「設計図」。

例えば、`base.html`や`header.html`はJinja2の構文を含んでおり、これらは「テンプレート」として機能します。

### 純粋なHTML（content.html）

- **拡張子**: `.html`
- **内容**: 純粋なHTMLのみ。
- **用途**: ブラウザで直接表示される最終的なページ。

`content.html`はレンダリング後の最終的なHTMLであり、Jinja2の構文は一切含まれていません。

## まとめ

- Jinja2テンプレートは、レンダリングの元となる「設計図」です。
- 純粋なHTMLは、レンダリング後にブラウザで表示される「完成品」です。

このように理解することで、Jinja2テンプレートと純粋なHTMLの違いと、それぞれの役割が明確になります。

---
以上がJinja2の基本と、それをPelicanのテーマ作成でどのように活用するかの解説です。この知識を基に、効率的なテーマ作成を行ってください。
