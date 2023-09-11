AUTHOR = "atu4403"
SITENAME = "pelican-lessons-log"
SITEURL = "http://localhost:8200"
PORT = 8200


PATH = "content"
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "ja"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = "/Users/atu/ghq/github.com/getpelican/pelican-themes/pelican-bootstrap3"
THEME = "theme"
# THEME = "simple-bootstrap5"
# THEME = "BT3-Flat"
ARTICLE_ORDER_BY = "sortorder"
PAGE_ORDER_BY = "sortorder"

# プラグインが存在するディレクトリのパスを指定
PLUGIN_PATHS = ["plugins"]

# 使用するプラグインの名前をリストに追加
PLUGINS = ["sample-generator"]
