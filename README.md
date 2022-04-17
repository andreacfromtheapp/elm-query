# Elm Query #

Search the official [Elm Packages](https://package.elm-lang.org/) website by keyword.

## Install ##

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette
2. Select **Package Control: Install Package**
3. Select **Elm Query**

## Usage ##

### Settings ###

You can set a valid alternative URL (e.g: [https://elm.dmy.fr](https://elm.dmy.fr)) if you really want to.

### Commands ###

#### Search Elm Packages ####

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette
2. Select **Elm Query: Search Packages**
3. Type a keyword in the Input Panel and press `Enter`
4. Select the desired result from the list presented in the Quick Panel
5. Press `Enter` to open a browser window for the selected Elm package

#### Search Elm Modules ####

This package intends to add the functionality to search the [Elm Search website](https://klaftertief.github.io/elm-search/) to look up Elm modules by function name or type signature.

However, this is not presently possible, because of how the Elm Search website is structured. To implement this feature, it would require either of these scenarios:

- Elm Search to offer a JSON file for the results so that it could be parsed (like Elm Packages does)
- Elm official website to implement modules search functionality and make it available via JSON (like they do for Elm Packages already).

To provide said functionality, I'd like to contribute to the the solution, but my Elm skills are still basic. Don't hold your breath.

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

Contributions are more than welcome :) Should you like to help out, please bear in mind that contribution should follow the guidelines specified in the [pyproject.toml](./pyproject.toml) file. (**flake8**, **black**).
