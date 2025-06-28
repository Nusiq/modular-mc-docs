(scope-system)=
# Scope System

The scope system in ModularMC allows you to define variables that can be used in JSON templates and shared across your project. Scope is a collection of variables and data that can be accessed by JSON templates during processing. Scope variables enable dynamic content generation and module configuration.

Unlike System Template, ModularMC doesn't have a special `_scope.json` file in every module. ModularMC manages scope directly in `_map.ts` files and through configuration. If you still want to use `_scope.json` you can simply import it in your `_map.ts` file.

## Scope Sources

ModularMC combines scope from multiple sources. When variables are defined in more than one place, the highest precedence source is used. The order is:

1. **Entry-Specific Scope** (highest priority)
2. **Module Scope** (from `_map.ts` variables)
3. **Global Scope** (from `scopePath` file) 
4. **Config Scope** (from `config.json`)

**1. Entry-Specific Scope**
Define scope directly inside a mapping entry for granular control. This scope has the highest priority.

```typescript
export const MAP = [{
    source: "template.json",
    target: "BP/entities/zombie.json",
    jsonTemplate: true,
    scope: { entityId: "zombie", health: 20 }
}];
```

**2. Module Scope**
Define variables and reusable scope objects within your `_map.ts` file.

```typescript
const zombieData = {
    name: "zombie",
    health: 20,
    speed: 0.25
};

export const MAP = [{
    source: "template.json",
    target: `BP/entities/${zombieData.name}.json`,
    jsonTemplate: true,
    scope: zombieData
}];
```

**3. Global Scope (via `scopePath`)**
Create a shared JSON file with global variables and reference it in your `config.json`. This scope is available to all modules.

*config.json:*
```json
{
    "filter": "modular_mc",
    "settings": {
        "scopePath": "data/project_scope.json"
    }
}
```

*data/project_scope.json:*
```json
{
    "namespace": "mypack",
    "author": "MyName"
}
```

**4. Config Scope**
Define scope directly in the filter settings in `config.json`. This is the lowest priority scope.

```json
{
    "filter": "modular_mc",
    "settings": {
        "scope": {
            "version": "1.0.0",
            "difficulty": "hard"
        }
    }
}
```

These variables are available in all modules unless overridden by a higher-priority scope.

## Scope Merging

When multiple scope sources define the same variable, higher precedence sources override lower ones. The scopes are merged using the same principles as the file merging system for
JSON files. See {ref}`File Merging<file-merging>` for more details.
