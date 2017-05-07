"""

cjrh_template
=============


"""
import string


__version__ = '2017.5.2'


class Template(string.Template):
    """
    Very thin subclass of ``string.Template``.
    """
    def placeholders(self, allow_repeats=False):
        """
        Return the names of the template variables in the template. Note that
        this returns a generator.

        The ``allow_repeats`` argument will cause the iteration to skip any
        repeated variable names.

        :type allow_repeats: bool
        :return: A generator of all the named vars
        :rtype: generator
        """
        seen = set()
        for match in self.pattern.finditer(self.template):
            named = match.group('named')
            if not allow_repeats:
                if named in seen:
                    continue
                else:
                    # Structured like this so that we don't incur the memory
                    # cost of storing previously-seen items when repeats are
                    # allowed.
                    seen.add(named)
            yield named
