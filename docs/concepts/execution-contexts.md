(execution-contexts)=
# Execution Contexts

ModularMC operates in two distinct **execution contexts** during the build process: the **mapping context** and the **compilation context**. Understanding these contexts is crucial for effective scripting, as they affect how scripts are compiled, how imports are resolved, and how debugging works.

The **mapping context** is used for evaluating `_map.ts` files in [Regolith's temporary working directory](https://regolith-docs.readthedocs.io/en/1.5.2/developing-filters/filter-development-introduction/#the-working-directory-of-filters). The **compilation context** is used for compiling script files listed in the {ref}`SCRIPTS<the-map-ts-file>` export using Esbuild in the project root. Compiling scripts directly in the project root allows {ref}`debugging with the Minecraft Bedrock Debugger<debugging-with-minecraft-bedrock-debugger>` VSCode extension.

```{note}
`%ROOT_DIR%` and `%FILTER_DIR%` on this page refer to environment variables set by Regolith that point to the project root and the filter's cache directory, respectively. See [Regolith's documentation](https://regolith-docs.readthedocs.io/en/1.5.2/developing-filters/filter-development-introduction/#accessing-files-outside-the-temporary-directory-using-environment-variables) for more information.
```

(mapping-context)=
## Mapping Context

The mapping context occurs in Regolith's temporary working directory, where ModularMC evaluates `_map.ts` files. It uses the `deno.json` from `%FILTER_DIR%`, which is not directly user-configurable. However, the filter automatically copies import mappings from your project's `%ROOT_DIR%/deno.json` to `%FILTER_DIR%/deno.json`, resolving relative paths to absolute `file://` URLs.

Additionally, paths that point to locations within your project's [dataPath](https://regolith-docs.readthedocs.io/en/1.5.2/project-configuration/project-config-file/#datapath) are redirected to the corresponding locations in the temporary data directory. This is particularly useful for import shortcuts in your `deno.json`, such as `"#shared/": "./filters_data/modular_mc/shared/"`, which reference project files conveniently without relative paths. The redirection ensures these shortcuts work correctly in the temp environment.

## Compilation Context

The compilation context occurs in the project root (`%ROOT_DIR%`), where ModularMC runs Esbuild to compile your TypeScript/JavaScript scripts into a bundled JavaScript file.

Scripts are compiled from the original files in your project directory (not from Regolith's temporary location), ensuring faster compilation by avoiding copying large `node_modules` folders into the temporary location. Import resolution uses your project's `deno.json`. This means that you get exactly what you see in your editor. The downside of this approach is that you cannot programmatically modify the script files before their compilation. The scripts from the Regolith's temporary location aren't used during compilation.

For tips setting up the debugging environment for compiled scripts, see {ref}`debugging with the Minecraft Bedrock Debugger<debugging-with-minecraft-bedrock-debugger>`.
