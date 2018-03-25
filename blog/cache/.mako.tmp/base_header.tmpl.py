# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521994361.625878
_enable_loop = True
_template_filename = u'themes/ariel17/templates/base_header.tmpl'
_template_uri = u'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_navigation_links', 'html_header', 'html_site_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n  <nav class="navbar navbar-inverse navbar-fixed-top">\n    <div class="container-fluid">\n      <div class="navbar-header">\n        <button type="button" class="collapsed navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse" aria-expanded="false">\n          <span class="sr-only">Toggle navigation</span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n        </button>\n        <a href="#" class="navbar-brand">')
        __M_writer(unicode(blog_title))
        __M_writer(u'</a>\n      </div>\n      <div class="collapse navbar-collapse" id="navbar-collapse">\n        <ul class="nav navbar-nav navbar-right">\n          <li id="home-link"><a href="/">Home</a></li>\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer(u'              <li> ')
                __M_writer(unicode(text))
                __M_writer(u'\n              <ul>\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer(u'                      <li class="active"><a href="')
                        __M_writer(unicode(permalink))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u' <span class="sr-only">')
                        __M_writer(unicode(messages("(active)", lang)))
                        __M_writer(u'</span></a></li>\n')
                    else:
                        __M_writer(u'                      <li><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a></li>\n')
                __M_writer(u'              </ul>\n')
            else:
                if rel_link(permalink, url) == "":
                    __M_writer(u'                <li class="active"><a href="#">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a></li>\n')
                else:
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a></li>\n')
        __M_writer(u'          ')
        __M_writer(unicode(template_hooks['menu']()))
        __M_writer(u'\n          ')
        __M_writer(unicode(template_hooks['menu_alt']()))
        __M_writer(u'\n        </ul>\n      </div>\n    </div>\n  </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <header id="header">\n        ')
        __M_writer(unicode(html_navigation_links()))
        __M_writer(u'\n')
        if search_form:
            __M_writer(u'            <div class="searchform" role="search">\n                ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n            </div>\n')
        __M_writer(u'    </header>\n    ')
        __M_writer(unicode(template_hooks['page_header']()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <h1 id="brand"><a href="')
        __M_writer(unicode(abs_link(_link("root", None, lang))))
        __M_writer(u'" title="" rel="home">\n')
        if logo_url:
            __M_writer(u'        <img src="')
            __M_writer(unicode(logo_url))
            __M_writer(u'" alt="')
            __M_writer(unicode(blog_title))
            __M_writer(u'" id="logo">\n')
        __M_writer(u'\n')
        if show_blog_title:
            __M_writer(u'        <span id="blog-title">')
            __M_writer(unicode(blog_title))
            __M_writer(u'</span>\n')
        __M_writer(u'    </a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"139": 16, "140": 17, "141": 17, "142": 18, "143": 19, "144": 19, "145": 19, "146": 19, "147": 19, "148": 21, "149": 22, "150": 23, "23": 2, "152": 23, "153": 25, "26": 0, "159": 153, "33": 2, "34": 14, "35": 26, "36": 69, "42": 28, "151": 23, "57": 28, "58": 38, "59": 38, "60": 43, "61": 44, "62": 45, "63": 45, "64": 45, "65": 47, "66": 48, "67": 49, "68": 49, "69": 49, "70": 49, "71": 49, "72": 49, "73": 49, "74": 50, "75": 51, "76": 51, "77": 51, "78": 51, "79": 51, "80": 54, "81": 55, "82": 56, "83": 57, "84": 57, "85": 57, "86": 58, "87": 59, "88": 59, "89": 59, "90": 59, "91": 59, "92": 63, "93": 63, "94": 63, "95": 64, "96": 64, "102": 4, "112": 4, "113": 6, "114": 6, "115": 7, "116": 8, "117": 9, "118": 9, "119": 12, "120": 13, "121": 13, "127": 16}, "uri": "base_header.tmpl", "filename": "themes/ariel17/templates/base_header.tmpl"}
__M_END_METADATA
"""
