# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521994362.205831
_enable_loop = True
_template_filename = u'themes/ariel17/templates/tagindex.tmpl'
_template_uri = u'tagindex.tmpl'
_source_encoding = 'utf-8'
_exports = [u'extra_head', u'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'index.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        kind = context.get('kind', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        kind = context.get('kind', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if len(translations) > 1 and generate_atom:
            for language in sorted(translations):
                __M_writer(u'            <link rel="alternate" type="application/atom+xml" title="Atom for the ')
                __M_writer(unicode(tag))
                __M_writer(u' section (')
                __M_writer(unicode(language))
                __M_writer(u')" href="')
                __M_writer(unicode(_link(kind + "_atom", tag, language)))
                __M_writer(u'">\n')
        elif generate_atom:
            __M_writer(u'        <link rel="alternate" type="application/atom+xml" title="Atom for the ')
            __M_writer(unicode(tag))
            __M_writer(u' section" href="')
            __M_writer(unicode(_link("tag" + "_atom", tag)))
            __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        messages = context.get('messages', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if subcategories:
            __M_writer(u'    ')
            __M_writer(unicode(messages('Subcategories:')))
            __M_writer(u'\n    <ul>\n')
            for name, link in subcategories:
                __M_writer(u'        <li><a href="')
                __M_writer(unicode(link))
                __M_writer(u'">')
                __M_writer(unicode(name))
                __M_writer(u'</a></li>\n')
            __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "46": 2, "51": 13, "56": 24, "62": 15, "76": 15, "77": 16, "78": 16, "79": 17, "80": 18, "81": 19, "82": 19, "83": 19, "84": 19, "85": 19, "86": 19, "87": 19, "88": 21, "89": 22, "90": 22, "91": 22, "92": 22, "93": 22, "99": 4, "107": 4, "108": 5, "109": 6, "110": 6, "111": 6, "112": 8, "113": 9, "114": 9, "115": 9, "116": 9, "117": 9, "118": 11, "124": 118}, "uri": "tagindex.tmpl", "filename": "themes/ariel17/templates/tagindex.tmpl"}
__M_END_METADATA
"""
