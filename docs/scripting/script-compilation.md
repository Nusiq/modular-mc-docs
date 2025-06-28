(script-compilation)=
# Script Compilation

ModularMC includes built-in TypeScript and JavaScript compilation using esbuild. This allows you to write modern TypeScript code and have it automatically compiled and integrated into your addon.

## Defining Scripts

Use the `SCRIPTS` export in your `_map.ts` file to specify which files should be compiled:

```typescript
export const SCRIPTS = [
    "zombie_ai.ts",
    "zombie_events.js", 
    "utils/zombie_utils.ts"
];
```

Scripts are paths relative to the module directory:

```
📂 my_entity/
    ⚙️ _map.ts
    📄 zombie.behavior.json
    📄 zombie_ai.ts          # Script file
    📄 zombie_events.js      # Script file
    📂 utils/
        📄 zombie_utils.ts   # Nested script file
```

## Compilation Process

ModularMC uses a **project-based compilation approach** that differs from some other script-compiling filters.

### How ModularMC Script Compilation Works
ModularMC compiles scripts directly from your **project directory**, not from the temporary location that Regolith creates when running filters. It performs the following steps:

1. **Collects paths to all scripts** from all modules in the temporary location
2. **Resolves script paths** to their corresponding files in the project directory
3. **Runs esbuild compilation** using files from the project
4. **Exports compiled bundle** to both the temporary location and optionally to `buildPath` (if specified)

This approach results in **faster compilation** because the `node_modules` folder is not copied to the temporary location. However, a crucial implication is that changes made to your TypeScript files by other Regolith filters will not affect the compilation; ModularMC always compiles from your original project files.

## esbuild Configuration

The detail of configuration is described in the {ref}`Installation and Configuration<installation-and-configuration>` section of the documentation.

## Script Dependencies

Since ModularMC compiles from your project directory, dependency management works just like a normal Node.js/Deno project. Scripts can import from other scripts in your project and from installed packages.
