Series List plugin
------------------

The series plugin gathers information about all series in a category. You can then use the `category.series_list` variable to get a list of all series in that category. Each item of the `series_list` is a Python dictionary with a URL and title that you can use to display the list of series. You can turn the list on or off by using the new `DISPLAY_ALL_SERIES_ON_SIDEBAR` configuration option in `pelicanconf.py`.

For example:

`pelicanconf.py`

    :::python
    DISPLAY_ALL_SERIES_ON_SIDEBAR = True

`sidebar.html` (Jinja template)

    :::python
    {% if article.category.series_list %}
        <h4 class="panel-title"><i class="fa fa-tags fa-list-ul"></i><span class="icon-label">All series in {{article.category}}</span></h4>
        <ul>
            {% for i in article.category.series_list %}
            <li>
                <a href="{{ SITEURL }}/{{ i.url }}">{{i.title}}</a>
            </li>
            {% endfor %}
        </ul>
    {% endif %}
