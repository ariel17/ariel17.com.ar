# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521994361.708923
_enable_loop = True
_template_filename = u'themes/ariel17/templates/list.tmpl'
_template_uri = 'list.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


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
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<article class="listpage">\n')
        if items:
            __M_writer(u'    <ul class="postlist">\n')
            for text, link in items:
                __M_writer(u'        <li><a href="')
                __M_writer(unicode(link))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a>\n')
            __M_writer(u'    </ul>\n')
        else:
            __M_writer(u'    <p>')
            __M_writer(unicode(messages("Nothing found.")))
            __M_writer(u'</p>\n')
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"64": 11, "65": 12, "66": 13, "59": 9, "36": 2, "69": 15, "68": 13, "41": 16, "75": 69, "47": 4, "67": 13, "55": 4, "56": 6, "57": 7, "58": 8, "27": 0, "60": 9, "61": 9, "62": 9, "63": 9}, "uri": "list.tmpl", "filename": "themes/ariel17/templates/list.tmpl"}
__M_END_METADATA
"""
