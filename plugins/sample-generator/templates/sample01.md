Title: {{ title }}
Date: {{ dt }}
Category: {{ categorie }}
sortorder: {{ sortorder }}

## {{ content_title }}

{% for content in contents %}
{{ content.time }}: {{ content.body }}
{% endfor %}

このページは、動的に生成されたサンプルページです。
