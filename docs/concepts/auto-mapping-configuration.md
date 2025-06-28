(auto-mapping-configuration)=
# Auto-Mapping Configuration

Auto-mapping behavior is controlled by the `auto-map.ts` file, which defines how file extensions are mapped to output directories. You can customize this mapping to fit your project's specific needs.

## Default Auto-Map Configuration

When you install ModularMC using Regolith, a default `auto-map.ts` file is added to your project at `data/modular_mc/auto-map.ts`. This file contains a comprehensive set of rules for standard Minecraft addon file types and serves as a great starting point for customization.

## Auto-Map File Structure

The `auto-map.ts` file exports an `AUTO_MAP` object that maps file extensions to output configurations. The mappings can be simple strings or more complex objects, as shown below:

```typescript
export const AUTO_MAP = {
    // A simple string mapping:
    ".behavior.json": "BP/entities",

    // An object mapping (useful for changing the extension):
    ".entity.png": {
        path: "RP/textures/entity",
        extension: ".png"
    }
};
```

**Simple String Mappings**: As seen with the `.behavior.json` entry in the example, the simplest mapping format uses a string to specify the output directory. The original filename is preserved.

**Object Mappings**: For more control, you can use an object mapping, like the `.entity.png` entry. This is useful when the file extension in the output needs to be different from the source. It has two properties:
- `path`: The output directory.
- `extension`: The file extension to use in the final output file. This often removes a prefix from the source extension (e.g., `.entity.png` becomes `.png`).

## Complete Default Configuration

The full default configuration ships with ModularMC and is located at `data/modular_mc/auto-map.ts` in your project. It's available to you once you install ModularMC with Regolith. Open that file to view every mapping or use it as a starting point for your own custom version.

## File Extension Patterns

Auto-mapping works by matching the **end** of the filename against the extension patterns. This means:

- `zombie.behavior.json` matches `.behavior.json`
- `iron_sword.item.json` matches `.item.json`  
- `mob_zombie.entity.png` matches `.entity.png`

You can use this to create specific patterns:

```typescript
export const AUTO_MAP = {
    // Specific entity types
    ".boss.behavior.json": "BP/entities/bosses",
    ".pet.behavior.json": "BP/entities/pets", 
    ".behavior.json": "BP/entities", // General fallback
    
    // Specific item types
    ".weapon.item.json": "BP/items/weapons",
    ".consumable.item.json": "BP/items/consumables",
    ".item.json": "BP/items" // General fallback
};
```

The patterns are matched from top to bottom, so more specific patterns should be placed above more general ones.
