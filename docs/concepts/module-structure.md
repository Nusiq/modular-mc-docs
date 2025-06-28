(module-structure)=
# Module Structure

## Creating Modules

Any directory within `data/modular_mc` that contains a {ref}`_map.ts<the-map-ts-file>` file becomes a module. The `_map.ts` file defines how the module's files should be processed and where they should be exported.

### Basic Module Structure

Example below creates a module called `my_entity` that contains files related to a zombie entity.

```
📂 data/modular_mc/
    📂 my_entity/
        ⚙️ _map.ts          # Required - defines the module
        📄 zombie.behavior.json
        📄 zombie.geo.json
        🖼️ zombie.entity.png
        📄 zombie_attack.animation.json
```

Modules can have any structure you want. Subdirectories are allowed for better organization.

### Nested Modules

You can put modules inside other modules. This way a big module can have smaller parts that still can be easily exported to other projects.

```
📂 data/modular_mc/
    📂 magic/                        # Parent module (module A)
        ⚙️ _map.ts
        📄 projectile.ts             # Shared script used by submodules
        📂 fireball/                 # Nested module (module B)
            ⚙️ _map.ts
            📄 fireball.entity.json
            📄 fireball.geo.json
            🖼️ fireball.entity.png
        📂 magic_missile/            # Nested module (module C)
            ⚙️ _map.ts
            📄 magic_missile.particle.json
            📄 magic_missile.ts
```

Each directory with a {ref}`_map.ts<the-map-ts-file>` file is processed as an independent module, regardless of nesting level.

## Module Processing Order

Modules are processed in alphabetical order based on their full path. With the structure above, the processing order would be:

1. `magic/`
2. `magic/fireball/`
3. `magic/magic_missile/`

This consistent ordering ensures predictable behavior when multiple modules might affect the same output files.
