from talon import Context, Module

mod = Module()
mod.list("name", desc="Common names")
ctx = Context()
ctx.lists["user.name"] = """
abbreviate
config
cursor
cursorless
git
list
mode
path
rust
short
self
toggle
tree
user
word
""".split("\n")

@mod.capture(rule="{self.name}")
def name(m) -> str:
    """Common words that are often interpreted wrongly"""
    return m.name