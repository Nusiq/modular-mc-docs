(installation-and-configuration)=
# Installation and Configuration

## Installation

To make the ModularMC filter available in your [Regolith](https://regolith-docs.readthedocs.io/en/stable/) project, run the following command:

```text
regolith install modular_mc
```

To enable the filter, add the following configuration to the filters list in the `config.json` file of your Regolith project. Adjust the settings properties as needed (explained in the next section):

```json
{
    "filter": "modular_mc",
    "settings": {
        "esbuild": {
            "buildPath": ".modular_mc/main.js",
            "settings": {
                "sourcemap": true
            }
        }
    }
}
```

## Configuration Settings

Configuration settings should be placed in the `settings` property of the filter in the `config.json` file of your Regolith project. All settings are optional and have default behavior if not set.

(esbuild-configuration)=
### esbuild: object

The `esbuild` property configures TypeScript and JavaScript compilation. It has two sub-properties:

#### esbuild.settings: object

Contains compilation options for TypeScript/JavaScript processing. Note that ModularMC only supports specific settings, not arbitrary Esbuild options. Supported settings:

- `sourcemap`: Whether to generate source maps for debugging (true/false, default: false)
- `minify`: Whether to minify the output (true/false, default: false)
- `external`: Array of packages to mark as external (default: ["@minecraft/server"])
- `outfile`: Output file path relative to filter working directory (default: "BP/scripts/main.js")

Other esbuild settings like `target` (es2020), `format` (esm), and `bundle` (true) are hardcoded by ModularMC for compatibility.

#### esbuild.buildPath: string

The `buildPath` specifies where compiled scripts should be output, relative to the project root. This is useful for development workflows where you want scripts compiled to a specific location for easier debugging.

For example, setting `"buildPath": ".modular_mc/main.js"` will compile scripts to that location for development. It will also export them to the final behavior pack to be used by Minecraft.
