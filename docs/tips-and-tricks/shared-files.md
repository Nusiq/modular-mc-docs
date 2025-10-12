# Shared Files

In order to avoid duplicating files across multiple modules, you can create folders for shared resources. A good way to do this is to create one TypeScript file that exports all of the paths to the shared files and then just import it in your modules.

## Example

*File structure:*
```
📂 data/modular_mc/
    📂 shared/
        📄 _shared_resources.ts          # You can name it whatever you want
        🖼️ shared_texture_1.entity.png
        🖼️ shared_texture_2.entity.png
    📂 my_entity/
        ⚙️ _map.ts
```

*📄 _shared_resources.ts:*
```typescript
import { fromFileUrl } from "jsr:@std/path";

export default {
    sharedTexture1: fromFileUrl(
        new URL("shared/shared_texture_1.entity.png", import.meta.url)
    ),
    sharedTexture2: fromFileUrl(
        new URL("shared/shared_texture_2.entity.png", import.meta.url)
    ),
}
```

The `fromFileUrl(new URL(..., import.meta.url))` is used to get the absolute path to the file. This is important because the path is relative to the `_map.ts` file, not the `_shared_resources.ts` file.

*⚙️ _map.ts:*
```typescript
// You can export and import the variables however you want. I prefer using default
// export and than just destructure the object.
import _shared_resources from "../shared/_shared_resources";
const { sharedTexture1, sharedTexture2 } = _shared_resources;

export const MAP = [
    {
        source: sharedTexture1,
        onConflict: "skip",  // Skip if other systems already exported this
        target: ":autoFlat"  // Note that :auto is not allowed here
    },
    {
        source: sharedTexture1,
        target: {
            path: ":autoFlat",  // Note that :auto is not allowed here
            subpath: "my_subpath",
            name: ":auto"  // Using :auto here is fine
        }
    },
]
```
The `sharedTexture1` and `sharedTexture2` variables are absolute paths generated in the `_shared_resources.ts` file.

```{note}
The `../shared/_shared_resources` import could also be accessed using import aliases defined in `deno.json` in the project's root instead of relative paths.

This is made possible through custom mechanisms that make `deno.json` imports available in both the mapping context (for evaluating `_map.ts` files) and the compilation context (for compiling scripts). While effective, these mechanisms are not without limitations, so it's recommended to understand how they work. For more details, see the {ref}`Execution Contexts<execution-contexts>` section.
```