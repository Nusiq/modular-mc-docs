(file-mapping)=
# File Mapping

File mapping defines how files in your modules are exported to the final addon structure. ModularMC provides several ways to specify target paths, from simple string paths to automatic path generation.

## Basic String Mapping

The simplest form of mapping uses a string to specify the exact output path:

```typescript
export const MAP = [
    {
        source: "zombie.behavior.json",
        target: "BP/entities/zombie.behavior.json"
    },
    {
        source: "zombie.entity.png",
        target: "RP/textures/entity/zombie.png"
    }
];
```

This approach gives you complete control over where each file is placed in the output.

(auto-mapping)=
## Auto-Mapping

Auto-mapping automatically determines the target path based on the file's extension and a predefined mapping configuration. This saves time and ensures consistent file organization.

### :auto Keyword

The `:auto` keyword uses the file's extension to determine the appropriate output directory, **preserving any subdirectory structure from the source path**.

```typescript
export const MAP = [
    // Source in root of module
    {
        source: "zombie.behavior.json",
        target: ":auto"  // → BP/entities/zombie.behavior.json
    },
    // Source in a subfolder
    {
        source: "hostile/zombie.entity.png",
        target: ":auto"  // → RP/textures/entity/hostile/zombie.png
    }
];
```

Notice how the `hostile/` subfolder from the source is preserved in the output path.

It's also important to note that the `zombie.entity.png` file becomes `zombie.png` in the output. The `.entity` part of the extension is used by the auto-mapping system to route the file to the correct directory (`RP/textures/entity/`) and is then removed from the final filename. This powerful pattern allows you to organize files by their type and purpose within your modules. For more details on how to configure this behavior, see {ref}`Auto-Mapping Configuration<auto-mapping-configuration>`.

### :autoFlat Keyword

The `:autoFlat` keyword works like `:auto` but **ignores the directory structure of the source file**, placing the file directly in the auto-mapped root folder.

This is useful when your source files are organized into subdirectories, but you want a flat structure in the final output.

```typescript
export const MAP = [
    {
        source: "entities/hostile/zombie.behavior.json",
        target: ":autoFlat"  // → BP/entities/zombie.behavior.json
    },
    {
        source: "models/zombie.geo.json",
        target: ":autoFlat"  // → RP/models/entity/zombie.geo.json
    }
];
```

Here, the `entities/hostile/` and `models/` paths are discarded, and the files are placed directly in the directories determined by their extensions.

### Auto-Mapping Extensions

The behavior of auto-mapping is controlled by a set of rules in the `auto-map.ts` file. To learn how to view and customize these rules, see the {ref}`Auto-Mapping Configuration<auto-mapping-configuration>` documentation.

## Target Objects

For advanced scenarios, you can use target objects to have fine-grained control over the output path.

```typescript
{
    source: "entities/zombie_boss.behavior.json",
    target: {
        path: ":autoFlat",
        subpath: "bosses",
        name: "zombie_emperor.behavior.json"
    }
    // Results in: BP/entities/bosses/zombie_emperor.behavior.json
}
```


### path: string
The base directory for the output. It can be one of three value types:
- **A string path** (e.g., `"BP/entities"`): Sets the exact base directory.
- **`":auto"`**: Uses the auto-mapping directory but preserves the source's subdirectory structure.
- **`":autoFlat"`**: Uses the auto-mapping directory but discards the source's subdirectory structure.

### subpath: string (optional)
An optional string that defines an additional directory structure to be inserted between the `path` and the `name`.

### name: string
The output filename. It can be one of two value types:
- **A string name** (e.g., `"custom_zombie.behavior.json"`): Sets the exact output filename.
- **`":auto"`**: Uses the source filename and applies any extension transformations defined in your `auto-map.ts` configuration (e.g., `.entity.png` becomes `.png`). `:autoFlat` is not valid here.
