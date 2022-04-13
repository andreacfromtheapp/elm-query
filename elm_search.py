# Elm Search plugin for Sublime Text

import sublime
import sublime_plugin
import webbrowser
import urllib.request
import urllib.parse
import json
import re
from html.parser import HTMLParser


# Global varz
results = []


class ElmSearchCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Elm Search", "", search, None, None)


class ElmPackageCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Elm Packages", "", search, None, None)


class ElmSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, _):

        # query
        selection = self.view.sel()[0]
        if len(selection) == 0:
            selection = self.view.word(selection)
        query = self.view.substr(selection)

        search(query)


class ElmPackageSelectionCommand(sublime_plugin.TextCommand):
    def run(self, _):

        # query
        selection = self.view.sel()[0]
        if len(selection) == 0:
            selection = self.view.word(selection)
        query = self.view.substr(selection)

        search(query)


def search(input):
    global results

    query = urllib.parse.quote_plus(input)
    url = "https://klaftertief.github.io/elm-search/?q=" + query
    data = urllib.request.urlopen(url).read().decode()
    results = json.loads(data)

    formatedResult = []

    if results:
        for result in results:
            formatted = format(result)
            if formatted != "":
                formatedResult.append(formatted)
    else:
        formatedResult.append("No results")

    sublime.active_window().show_quick_panel(formatedResult, on_done)


def on_done(index):
    if index != -1:
        webbrowser.open(results[index]["url"], 2)


def format(result):
    if result.get("module") is None:  # Get module name if it exists
        return ""
    else:
        modname = result.get("module").get("name")
        if modname is None:
            return ""

    if result.get("item") is None:  # Get type signature
        return ""
    else:
        # split type siganture into name and type
        res = result["item"].split("::")
        name = re.sub("<[^<]+?>", "", res[0])  # remove all html tags
        if len(res) == 1:  # the type might not be included
            ret = modname + " " + name
        else:
            ret = modname + " " + name + "::" + res[1]

    return HTMLParser().unescape(ret)  # decode html entities
