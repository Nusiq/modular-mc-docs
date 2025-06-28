(the-map-ts-file)=
# The _map.ts File

The `_map.ts` file is the heart of every {ref}`ModularMC module<module-structure>`. It defines how the module's files are processed and exported to the final addon structure. It's a TypeScript file that can export two special variables `MAP` and `SCRIPTS`:

```typescript
export const MAP = [
    // Array of mapping entries
];

export const SCRIPTS = [
    // Array of script paths to compile
];
```

Both exports are optional, but most modules will at least define `MAP` to specify which files to export.

## MAP Export

The `MAP` export is an array of mapping entries that define how files in the module should be processed and where they should be exported.

**Example:**
```typescript
export const MAP = [
    {
        source: "zombie.behavior.json",
        target: "BP/entities/zombie.behavior.json"
    }
];
```

This copies `zombie.behavior.json` from the module directory to `BP/entities/zombie.behavior.json` in the output.

Each mapping entry is an object with the following properties:

```typescript
{
    source: string,              // Required - source file path
    target: string | object,     // Required - target path or configuration
    jsonTemplate?: boolean,      // Optional - enable JSON template processing
    onConflict?: string,         // Optional - conflict resolution strategy
    fileType?: string,           // Optional - override file type detection
    scope?: object               // Optional - entry-specific scope variables
}
```

### source: string
The path to the source file relative to the module directory.

### target: string | object
Defines where the file should be exported. This can be a simple string path or a configuration object. For detailed information on all mapping strategies, including auto-mapping with `:auto` and `:autoFlat`, and using target objects, see the {ref}`File Mapping<file-mapping>` documentation.

### jsonTemplate: boolean
When `true`, the source file is processed as a JSON template, allowing TypeScript expressions in strings. See {ref}`JSON Template<json-template>` for details on template syntax.

### onConflict: string
Defines how to handle conflicts when multiple modules export to the same target path. Options:

- `"stop"` (default): Stop processing and report an error
- `"skip"`: Skip this entry and continue
- `"merge"`: Attempt to merge the files (JSON only)
- `"overwrite"`: Overwrite the existing file
- `"appendStart"`: Prepend the source file content to the beginning of the existing file (text files only)
- `"appendEnd"`: Append the source file content to the end of the existing file (text files only)

See {ref}`File Merging<file-merging>` for more details.

### fileType: string
Override automatic file type detection. Useful for files with non-standard extensions. This allows you to mark a file as JSON to enable JSON template, even if it has a different extension.

### scope: object
Define variables specific to this mapping entry, available in {ref}`JSON templates<json-template>`. These override any variables from the module, config, or global scopes. See {ref}`Scope System<scope-system>` for more information.

## SCRIPTS Export

The `SCRIPTS` export defines TypeScript or JavaScript files that should be compiled with Esbuild and included in the final addon.

```typescript
export const SCRIPTS = [
    "my_module_logic.ts",
    "effects/fire_particle.ts"
];
```

For details on script compilation and Esbuild options, see {ref}`Script Compilation<script-compilation>`.