from talon import Context, Module

mod = Module()
mod.list("name", desc="Common names")
ctx = Context()
ctx.lists["user.name"] = """
abbreviate
config
cursor
git
list
mode
path
short
self
splice sites
toggle
user
word
""".split("\n")