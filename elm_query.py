import sublime
import sublime_plugin
import webbrowser
import urllib.request
import urllib.parse
import json


class ElmPackageCommandCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel(
            "Elm Packages", "", elm_package, None, None
        )


def elm_package(input):
    def on_done(index):
        if index > 0:
            webbrowser.open(homepage, 2)

    url = "https://package.elm-lang.org/search.json"
    text = urllib.request.urlopen(url).read().decode()
    data = json.loads(text)
    results = [x for x in data if input in x["name"] or input in x["summary"]]

    package_list = []

    if results:
        for x in results:
            package = x["name"]
            summary = x["summary"]
            version = x["version"]
            description = "<em>%s</em>" % sublime.html_format_command(summary)
            homepage = (
                "https://package.elm-lang.org/packages/{}/latest/".format(
                    package
                )
            )
            final_line = 'version: {}; <a href="{}">{}</a>'.format(
                version, homepage, homepage
            )
            package_entry = sublime.QuickPanelItem(
                package, [description, final_line]
            )
            package_list.append(package_entry)
    else:
        package_list.append(
            "No results found for the keyword '{}'".format(input)
        )

    sublime.active_window().show_quick_panel(package_list, on_done)


# this would be nice, but the elm packages site doesn't work that way....
# class ElmPackageSelectionCommand(sublime_plugin.TextCommand):
#     def run(self, _):
#         # query
#         selection = self.view.sel()[0]
#         if len(selection) == 0:
#             selection = self.view.word(selection)
#         query = self.view.substr(selection)

#         elm_package(query)


class ElmSearchCommandCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Elm Search", "", elm_search, None, None)


class ElmSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, _):

        # query
        selection = self.view.sel()[0]
        if len(selection) == 0:
            selection = self.view.word(selection)
        query = self.view.substr(selection)

        elm_search(query)


def elm_search(input):
    global results

    query = urllib.parse.quote_plus(input)
    url = "https://klaftertief.github.io/elm-search/?q=" + query
    data = urllib.request.urlopen(url).read().decode()
    results = json.loads(data)
