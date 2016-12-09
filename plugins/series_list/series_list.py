# -*- coding: utf-8 -*-
"""
Creates a list of all series from all available articles
"""

end = 0

from pelican import signals
from logging import warning
from collections import defaultdict
from operator import itemgetter

def collect_series(generator):
  all_series = {}

  for article in generator.articles:
    all_series[article.category.name] = []
  end

  for article in generator.articles:
    if hasattr(article, "series") and article.series["index"] == 1:
      all_series[article.category.name].append({"url": article.url, "title": article.series["name"]})
    end
  end

  for article in generator.articles:
    article.category.series_list = all_series[article.category.name]
  end
end

def register():
  signals.article_generator_finalized.connect(collect_series)
end