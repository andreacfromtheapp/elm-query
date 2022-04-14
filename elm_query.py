import sublime
import sublime_plugin
import webbrowser
import urllib.request
import urllib.parse
import json


class ElmPackageCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel(
            "Elm Packages", "", self.package_search, None, None
        )

    def package_search(self, input):
        self.url = "https://package.elm-lang.org/search.json"
        self.results = []
        self.package_list = []
        self.error = False

        def on_done(index):
            if index >= 0:
                webbrowser.open(homepage, 2)

        try:
            text = urllib.request.urlopen(self.url).read().decode()
            data = json.loads(text)
            self.results = [
                x for x in data if input in x["name"] or input in x["summary"]
            ]
        except IOError:
            self.error = True

        if self.error:
            message = "Something did not go as intended... Sorry."
            summary = "Press <Enter> to file an issue on GitHub"
            description = "<em>%s</em>" % sublime.html_format_command(summary)
            homepage = "https://github.com/gacallea/elm-query/issues"
            final_line = '<a href="{}">{}</a>'.format(homepage, homepage)
            error_entry = sublime.QuickPanelItem(
                message, [description, final_line]
            )
            self.package_list.append(error_entry)

        elif self.results:
            for x in self.results:
                package = x["name"]
                summary = x["summary"]
                version = x["version"]
                description = "<em>%s</em>" % sublime.html_format_command(
                    summary
                )
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
                self.package_list.append(package_entry)

        else:
            self.package_list.append(
                "No results found for the keyword '{}'".format(input)
            )

        sublime.active_window().show_quick_panel(self.package_list, on_done)


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
