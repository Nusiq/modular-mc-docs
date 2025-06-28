# Introduction

[ModularMC](https://github.com/Nusiq/regolith-filters/tree/master/modular_mc) is a TypeScript-based Regolith filter and successor to [System Template](https://github.com/Nusiq/regolith-filters/tree/master/system_template). Instead of scattering files across directories by type (entities/, textures/, scripts/, etc.), ModularMC lets you organize files into logical modules based on functionality. A single module can contain an entity's behavior file, textures, animations, scripts, and any other related assets.

## Key Benefits

- **Module organization**: Group files by purpose, making projects easier to understand and maintain
- **JSON templating**: Dynamic content generation using TypeScript expressions inside JSON files
- **Script compilation**: Built-in Esbuild support for TypeScript/JavaScript compilation
- **Familiar syntax**: Uses familiar for most addon developers TypeScript syntax for configuration and templating
- **Easy sharing**: Modules can be copied between projects or shared with other developers
