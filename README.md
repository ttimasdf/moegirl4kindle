# moegirl4kindle

Kindle screensaver generator, R18. Custom sized screensavers available for all species(KT/PW/PW2/KT2/KV/PW3/KOA/KT3)

这是一个为Kindle Touch／Kindle PaperWhite／Kindle Oasis／Kindle Voyage全机种生成萌娘壁纸的小程序！

# Installation

```shell
pip install -r requirements.py
```

# Usage

e.g. Use Image source from Konachan with tag 'uncensored' and output images metadata into konachan.json, with images stored at images/ directory.


下例中使用Konachan的uncensored标签作为图源并保存输出到 konachan.json 。原始图片将保存到 `images/full` 目录下， `images/thumbs` 下根据设备类型分不同文件夹存放转换后的壁纸。

```shell
# source venv/bin/activate  # If you use virtualenv of any kind
scrapy crawl konachan -a category=uncensored -o konachan.json
```

TODO: download the biggest size picture available.

vola!
