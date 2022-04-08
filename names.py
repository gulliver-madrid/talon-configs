from talon import Context, Module

mod = Module()
mod.list("name", desc="Common names")
ctx = Context()
ctx.lists["user.name"] = """
abbreviate
cursor
git
mode
short
self
splice sites
toggle
user
word
""".split("\n")