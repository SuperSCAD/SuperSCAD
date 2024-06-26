class ScadCodeStore:
    """
    Class for storing and formatting OpensSCAD code.
    """
    C_INDENTATION: int = 3

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object contructor.
        """
        self.lines: list[str] = list()
        """
        The stored code.
        """

        self.indent_level: int = 0
        """
        The current indentation level.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def add_line(self, line: str):
        """
        Adds a line to the code.

        :param line: The line.
        """
        if line == '{':
            self.lines.append(' ' * (ScadCodeStore.C_INDENTATION * self.indent_level) + line)
            self.indent_level += 1
        elif line == '}':
            self.indent_level = max(0, self.indent_level - 1)
            self.lines.append(' ' * (ScadCodeStore.C_INDENTATION * self.indent_level) + line)
        else:
            self.lines.append(' ' * (ScadCodeStore.C_INDENTATION * self.indent_level) + line)

        return self

    # ------------------------------------------------------------------------------------------------------------------
    def append_to_last_line(self, part: str) -> None:
        """
        Appends a part of code to the last line.

        :param part: The part of code.
        """
        self.lines[-1] += part

    # ------------------------------------------------------------------------------------------------------------------
    def get_code(self) -> str:
        """
        Returns the code as a string.
        """
        return '\n'.join(self.lines)

# ----------------------------------------------------------------------------------------------------------------------
