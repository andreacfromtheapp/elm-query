import sublime
import sublime_plugin
import webbrowser
import urllib.request
import urllib.parse
import json

# not using requests just yet because
# https://package.elm-lang.org cert fails SSL checks
# cert is valid but it's Grade B for using old TLS 1.0
# will use requests when that's fixed upstream...
# import requests
# text = requests.get(cls.url)
# text.json()


class ElmSearchPackageCommand(sublime_plugin.WindowCommand):
    package_list = []

    def run(self):
        self.window.show_input_panel(
            "Elm Packages", "", self.package_search, None, None
        )

    @classmethod
    def package_search(cls, input):
        cls.url = "https://package.elm-lang.org/search.json"
        cls.package_list.clear()
        cls.results = []
        cls.error = False

        try:
            text = urllib.request.urlopen(cls.url).read().decode()
            data = json.loads(text)
            cls.results = [
                x for x in data if input in x["name"] or input in x["summary"]
            ]
        except IOError:
            cls.error = True

        if cls.error:
            message = "Something did not go as intended... Sorry."
            summary = "Press <Enter> to file an issue on GitHub"
            description = "<em>%s</em>" % sublime.html_format_command(summary)
            homepage = "https://github.com/gacallea/elm-query/issues"
            final_line = '<a href="{}">{}</a>'.format(homepage, homepage)
            error_entry = sublime.QuickPanelItem(
                message, [description, final_line]
            )
            cls.package_list.append(error_entry)

        elif cls.results:
            for x in cls.results:
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
                cls.package_list.append(package_entry)

        else:
            cls.package_list.append(
                "No results found for the keyword '{}'".format(input)
            )

        sublime.active_window().show_quick_panel(cls.package_list, cls.on_done)

    @classmethod
    def on_done(cls, index):
        if index >= 0:
            if cls.error:
                link_to_open = "https://github.com/gacallea/elm-query/issues"
            else:
                link_to_open = (
                    "https://package.elm-lang.org/packages/{}/latest/".format(
                        cls.package_list[index].trigger
                    )
                )
            webbrowser.open(link_to_open, 2)


# class ElmSearchModuleCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         self.window.show_input_panel("Elm Search", "", elm_search, None, None)


# class ElmSearchSelectionCommand(sublime_plugin.TextCommand):
#     def run(self, _):
#         # get a query text from selected text or word under the mouse
#         selection = self.view.sel()[0]
#         if len(selection) == 0:
#             selection = self.view.word(selection)
#         query = self.view.substr(selection)
#         # call elm search with said query
#         elm_search(query)


# def elm_search(input):
#     query = urllib.parse.quote_plus(input)
#     url = "https://klaftertief.github.io/elm-search/?q=" + query
#     html = urllib.request.urlopen(url).read().decode("utf-8")
#     print(html)
