"""Render arcyd status file as meaningful html to present to users."""
# =============================================================================
# CONTENTS
# -----------------------------------------------------------------------------
# abdcmd_arcydstatushtml
#
# Public Functions:
#   getFromfilePrefixChars
#   setupParser
#   process
#   render_content
#
# -----------------------------------------------------------------------------
# (this contents block is generated, edits will be lost)
# =============================================================================

from __future__ import absolute_import

import json

import phlsys_fs

import abdweb_arcydcontent
import abdweb_htmlformatter
import abdweb_page


def getFromfilePrefixChars():
    return None


def setupParser(parser):
    parser.add_argument(
        'report_file',
        metavar="REPORTFILE",
        type=str,
        help="path to the file to render")
    parser.add_argument(
        'base_url',
        metavar="URL",
        type=str,
        help="base url to construct links from")


def _read_json_file(filename):
    result = None
    text = phlsys_fs.read_text_file(filename)
    if text:
        result = json.loads(text)
    return result


def process(args):
    content = render_content(
        args.report_file, args.base_url)
    print content


def render_content(report_file, base_url):

    formatter = abdweb_htmlformatter.HtmlFormatter()
    report = _read_json_file(report_file)
    abdweb_arcydcontent.render(
        formatter,
        base_url,
        report)
    content = formatter.get_content()

    formatter = abdweb_htmlformatter.HtmlFormatter()
    abdweb_page.render(formatter, content)
    return formatter.get_content()


# -----------------------------------------------------------------------------
# Copyright (C) 2013-2014 Bloomberg Finance L.P.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# ------------------------------ END-OF-FILE ----------------------------------
