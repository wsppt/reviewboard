from django.utils import six
from django.utils.six.moves.urllib.parse import quote as urlquote
        file_info.data = self.lines[linenum] + b"\n"
        # Check to make sure we haven't reached the end of the diff.
        if linenum >= len(self.lines):
            return linenum, None

            file_info.data += self.lines[linenum] + b"\n"
            file_info.data += self.lines[linenum] + b"\n"
            file_info.data += self.lines[linenum] + b"\n"
            file_info.data += self.lines[linenum + 1] + b"\n"
            file_info.data += self.lines[linenum] + b"\n"
            file_info.data += self.lines[linenum + 1] + b"\n"
            file_info.data += self.lines[linenum + 2] + b"\n"
            file_info.data += self.lines[linenum] + b"\n"
                file_info.data += self.lines[linenum] + b"\n"
                file_info.data += self.lines[linenum] + b'\n'
                file_info.data += self.lines[linenum + 1] + b'\n'
        return self.lines[linenum].startswith(b"new file mode")
        return self.lines[linenum].startswith(b"deleted file mode")
        return (self.lines[linenum].startswith(b"old mode")
                and self.lines[linenum + 1].startswith(b"new mode"))
        return (self.lines[linenum].startswith(b"similarity index") and
                self.lines[linenum + 1].startswith(b"rename from") and
                self.lines[linenum + 2].startswith(b"rename to"))
                self.lines[linenum].startswith(b"index "))
        return self.lines[linenum].startswith(b'diff --git')
        return (line.startswith(b"Binary file") or
                line.startswith(b"GIT binary patch"))
                (self.lines[linenum].startswith(b'--- ') and
                    self.lines[linenum + 1].startswith(b'+++ ')))