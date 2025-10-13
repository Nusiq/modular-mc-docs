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
        "whitelist": [""],
        "blacklist": [],
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
- `dropLabels`: Array of labels to drop from the output. For example, you can label your debug-only code with `DEBUG:` and then drop it from the production build by setting this to `["DEBUG"]`. (default: `[]`)

Other esbuild settings like `target` (es2020), `format` (esm), and `bundle` (true) are hardcoded by ModularMC for compatibility.

(esbuild-build-path)=
#### esbuild.buildPath: string

The `buildPath` specifies where compiled scripts should be output, relative to the project root. This is useful for development workflows where you want scripts compiled to a specific location for easier debugging.

For example, setting `"buildPath": ".modular_mc/main.js"` will compile scripts to that location for development. It will also export them to the final behavior pack to be used by Minecraft. This is useful for {ref}`debugging with the Minecraft Bedrock Debugger<debugging-with-minecraft-bedrock-debugger>`.

### whitelist: string[]

An array of strings specifying which modules to include in the processing. Each string represents a path relative to the `data/modular_mc` directory. If a module's path matches (exactly or as a subdirectory) any of the whitelist entries, it will be processed.

- Empty string `""` (default) includes all modules.
- `"subfolder"` includes modules in `data/modular_mc/subfolder/` and its subdirectories.
- Multiple entries allow including multiple specific areas.

Default: `[""]`

### blacklist: string[]

An array of strings specifying which modules to exclude from processing. Each string represents a path relative to the `data/modular_mc` directory. If a module's path matches (exactly or as a subdirectory) any of the blacklist entries, it will not be processed, even if it matches the whitelist.

- Empty array `[]` (default) excludes nothing.
- `"experimental"` excludes modules in `data/modular_mc/experimental/` and its subdirectories.
- Multiple entries allow excluding multiple specific areas.

Default: `[]`

**Note:** Blacklist takes precedence over whitelist. If a module matches both, it will be excluded.
