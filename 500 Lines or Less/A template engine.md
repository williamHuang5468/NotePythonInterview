# [A template engine](http://aosabook.org/en/500L/a-template-engine.html)

- [ ] [Introduction]()
- [ ] [Templates]()
- [ ] [Supported Syntax]()

## Introduction

Most programs contain a lot of logic, and a little bit of literal textual data. Programming languages are designed to be good for this sort of programming. But some programming tasks involve only a little bit of logic, and a great deal of textual data. For these tasks, we'd like to have a tool better suited to these text-heavy problems. A template engine is such a tool. In this chapter, we build a simple template engine.

    Programs contain logic and textual data. PL are designed to be good for this sort of programming . But tasks involve logic and texttual data. we like to have a tool better suited to these text-heavy problems. A template engine is a tool.

    Build a tool for these tasks.

The most common example of one of these text-heavy tasks is in web applications. An important phase in any web application is generating HTML to be served to the browser. Very few HTML pages are completely static: they involve at least a small amount of dynamic data, such as the user's name. Usually, they contain a great deal of dynamic data: product listings, friends' news updates, and so on.

    common example of one of these text-heavy tasks is (in web application).

    example is application.

    important phase (in any web application) is generating HTML (to be served) (to the browser).

    HTML pages are static.

    they involve data, such as user's name.


At the same time, every HTML page contains large swaths of static text. And these pages are large, containing tens of thousands of bytes of text. The web application developer has a problem to solve: how best to generate a large string containing a mix of static and dynamic data? To add to the problem, the static text is actually HTML markup that is authored by another member of the team, the front-end designer, who wants to be able to work with it in familiar ways.

    page contains large text. pages are large. developer has problem.

    How best to generate a large string containing a mix of static and dynamic data?

Here, the user's name will be dynamic, as will the names and prices of the products. Even the number of products isn't fixed: at another moment, there could be more or fewer products to display.

One way to make this HTML would be to have string constants in our code, and join them together to produce the page. Dynamic data would be inserted with string substitution of some sort. Some of our dynamic data is repetitive, like our lists of products. This means we'll have chunks of HTML that repeat, so those will have to be handled separately and combined with the rest of the page.

Producing our toy page in this way might look like this:

## 筆記

模版引擎是在解決，當網站的動態資料數量比較多或大的情況下，為了讓這些資料可以動態的顯示。

不動態就需要一個一個顯示。數量大，維護會有困難，像是重複的程式碼，維護多版本的扣會很麻煩。

舉例:
```HTML

<p>Welcome, Charlie!</p>
<p>Products:</p>
<ul>
    <li>Apple: $1.00</li>
    <li>Fig: $1.50</li>
    <li>Pomegranate: $3.25</li>
</ul>
```

以這個例子來說，`使用者的名稱`和`產品`是可以動態的。

```Python
# The main HTML for the whole page.
PAGE_HTML = """
<p>Welcome, {name}!</p>
<p>Products:</p>
<ul>
{products}
</ul>
"""

# The HTML for each product displayed.
PRODUCT_HTML = "<li>{prodname}: {price}</li>\n"

def make_page(username, products):
    product_html = ""
    for prodname, price in products:
        product_html += PRODUCT_HTML.format(
            prodname=prodname, price=format_price(price))
    html = PAGE_HTML.format(name=username, products=product_html)
    return html
```



## Question

- What is tempalte engine?
- Why i need template engine?
- 有什麼好處跟壞處?
- 最初的問題是什麼?
    - How best to generate a large string containing a mix of static and dynamic data?

## Advice after read it.

Little Parser to get the title of each part.
