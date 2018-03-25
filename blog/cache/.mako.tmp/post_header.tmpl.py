# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521994362.508674
_enable_loop = True
_template_filename = u'themes/ariel17/templates/post_header.tmpl'
_template_uri = u'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_post_header', 'html_title', 'html_translations', 'html_sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        def html_title():
            return render_html_title(context)
        messages = context.get('messages', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        comments = _mako_get_namespace(context, 'comments')
        def html_translations(post):
            return render_html_translations(context,post)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <header>\n        ')
        __M_writer(unicode(html_title()))
        __M_writer(u'\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">')
        __M_writer(unicode(post.author()))
        __M_writer(u'</span></p>\n            <p class="dateline"><a href="')
        __M_writer(unicode(post.permalink()))
        __M_writer(u'" rel="bookmark"><time class="published dt-published" datetime="')
        __M_writer(unicode(post.formatted_date('webiso')))
        __M_writer(u'" itemprop="datePublished" title="')
        __M_writer(unicode(post.formatted_date(date_format)))
        __M_writer(u'">')
        __M_writer(unicode(post.formatted_date(date_format)))
        __M_writer(u'</time></a></p>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer(u'                <p class="commentline">')
            __M_writer(unicode(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer(u'\n')
        __M_writer(u'            ')
        __M_writer(unicode(html_sourcelink()))
        __M_writer(u'\n')
        if post.meta('link'):
            __M_writer(u'                    <p class="linkline"><a href=\'')
            __M_writer(unicode(post.meta('link')))
            __M_writer(u"'>")
            __M_writer(unicode(messages("Original site")))
            __M_writer(u'</a></p>\n')
        if post.description():
            __M_writer(u'                <meta name="description" itemprop="description" content="')
            __M_writer(unicode(post.description()))
            __M_writer(u'">\n')
        __M_writer(u'        </div>\n        ')
        __M_writer(unicode(html_translations(post)))
        __M_writer(u'\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if title and not post.meta('hidetitle'):
            __M_writer(u'    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" class="u-url">')
            __M_writer(filters.html_escape(unicode(post.title())))
            __M_writer(u'</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(post.translated_to) > 1:
            __M_writer(u'        <div class="metadata posttranslations translations">\n            <h3 class="posttranslations-intro">')
            __M_writer(unicode(messages("Also available in:")))
            __M_writer(u'</h3>\n')
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer(u'                <p><a href="')
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'" rel="alternate" hreflang="')
                    __M_writer(unicode(langname))
                    __M_writer(u'">')
                    __M_writer(unicode(messages("LANGUAGE", langname)))
                    __M_writer(u'</a></p>\n')
            __M_writer(u'        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if show_sourcelink:
            __M_writer(u'        <p class="sourceline"><a href="')
            __M_writer(unicode(post.source_link()))
            __M_writer(u'" id="sourcelink">')
            __M_writer(unicode(messages("Source")))
            __M_writer(u'</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 14, "129": 14, "130": 15, "131": 16, "132": 17, "133": 17, "134": 17, "135": 17, "136": 17, "137": 17, "138": 17, "139": 20, "145": 24, "164": 158, "154": 26, "23": 3, "152": 24, "153": 25, "26": 2, "155": 26, "156": 26, "29": 0, "158": 26, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 49, "45": 30, "157": 26, "60": 30, "61": 32, "62": 32, "63": 34, "64": 34, "65": 35, "66": 35, "67": 35, "68": 35, "69": 35, "70": 35, "71": 35, "72": 35, "73": 36, "74": 37, "75": 37, "76": 37, "77": 39, "78": 39, "79": 39, "80": 40, "81": 41, "82": 41, "83": 41, "84": 41, "85": 41, "86": 43, "87": 44, "88": 44, "89": 44, "90": 46, "91": 47, "92": 47, "98": 5, "104": 5, "105": 6, "106": 7, "107": 7, "108": 7, "109": 7, "110": 7, "116": 11, "125": 11, "126": 12, "127": 13}, "uri": "post_header.tmpl", "filename": "themes/ariel17/templates/post_header.tmpl"}
__M_END_METADATA
"""
