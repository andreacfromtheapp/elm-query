# Elm Query #

Search the official [Elm Packages](https://package.elm-lang.org/) website by keyword.

## Install ##

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette
2. Select **Package Control: Install Package**
3. Select **Elm Query**

## Usage ##

This package doesn't need any settings at the moment (this may change in the future).

### Commands ###

#### Search Elm Packages ####

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette
2. Select **Elm Query: Search Packages**
3. Type a keyword in the Input Panel and press `Enter`
4. Select the desired result from the list presented in the Quick Panel
5. Press `Enter` to open a browser window for the selected Elm package

#### Search Elm Modules ####

This package was initially intended to also have the functionality to search the [Elm Search website](https://klaftertief.github.io/elm-search/) to look up Elm modules by function name or type signature.

Unfortunately this is not presently possible, because of how the Elm Search website is structured. Which would require unavailable scenarios for this to work:

- Elm Search to offer a JSON file for the results so that it could be parsed (like `Elm Query: Search Packages` works)
- Elm official website to re-implement Elm Search with JSON and updated/improved code
- Sublime Text to allow third party Python modules so that it could be possible to use tools to obviate the above

It is my intention to offer Elm Search functionality one day soon. I can't promise, and my Elm skills are still basic, but I may contribute to the Elm-related side of the solution. Don't hold your breath though...

### Key Bindings ###

Should you need key bindings, these are the currently implemented commands:

```json
[
    {
        "caption": "Elm Query: Search Packages",
        "command": "elm_search_package"
    }
] 
```

## Contributing ##

If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
2. Hack on a separate topic branch created from the latest `master`.
3. Commit and push the topic branch.
4. Make a pull request.

Contributions should follow the guidelines specified in the [pyproject.toml](./pyproject.toml) file. (**flake8**, **black**).
