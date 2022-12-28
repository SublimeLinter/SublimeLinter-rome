import re
from SublimeLinter.lint import NodeLinter, util


class Rome(NodeLinter):
    cmd = 'rome check --colors=off ${file}'
    regex = (
        r'^.*:(?P<line>\d+):(?P<col>\d+)\s*'
        r'\w+/\w+/(?P<code>\w+)\s*'
        r'(FIXABLE\s*)?'
        r'━*\s*'
        r'((?P<warning>⚠|!)|(?P<error>×))\s+'
        r'(?P<message>.*)\n'
    )
    multiline = True
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'source.js, source.ts, source.jsx, source.tsx'
    }
