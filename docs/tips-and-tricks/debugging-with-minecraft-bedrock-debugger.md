(debugging-with-minecraft-bedrock-debugger)=
# Debugging with Minecraft Bedrock Debugger

The {ref}`buildPath<esbuild-build-path>` setting in your filter configuration allows compiled scripts to be output to a specific location in your project root for development/debugging.

Since compilation happens in the project root, source maps point to your original files, enabling breakpoints and stepping in your IDE. This allows you to use the Minecraft Bedrock Debugger VSCode extension to attach to Minecraft and debug scripts in real-time.

## Configuration
Set `buildPath` in your filter's settings (e.g., `"buildPath": "debug/script/main.js"`). This outputs the bundle to `debug/script/main.js` in your project.

## VSCode Setup for Debugging
1. Install the [Minecraft Bedrock Debugger](https://marketplace.visualstudio.com/items?itemName=mojang-studios.minecraft-debugger) extension.
2. Add these files to your `.vscode/` folder:

`.vscode/launch.json`:
```json
{
  "version": "0.3.0",
  "configurations": [
    {
      "type": "minecraft-js",
      "request": "attach",
      "name": "Debug with Minecraft",
      "mode": "listen",
      "preLaunchTask": "Build For Debugging",
      "targetModuleUuid": "COPY-THE-UUID-OF-THE-JAVASCRIPT-MODULE-FROM-YOUR-BEHAVIORPACK-HERE",
      "localRoot": "${workspaceFolder}/debug/script/",
      "sourceMapRoot": "${workspaceFolder}/debug/script/",
      "port": 19144
    }
  ]
}
```
This file configures the debugger to attach to Minecraft and use the source maps to map the compiled JavaScript back to your original TypeScript files.

```{warning}
You need to replace `COPY-THE-UUID-OF-THE-JAVASCRIPT-MODULE-FROM-YOUR-BEHAVIORPACK-HERE` with the UUID of the JavaScript module from your behaviorpack. You can find this in the behaviorpack's `manifest.json` file.
```

`.vscode/prepare_debug.bat`:
```batch
powershell CheckNetIsolation.exe LoopbackExempt -a -p=S-1-15-2-1958404141-86561845-1752920682-3514627264-368642714-62675701-733520436
powershell CheckNetIsolation.exe LoopbackExempt -a -p=S-1-15-2-424268864-5579737-879501358-346833251-474568803-887069379-4040235476
```
These commands are required to allow the debugger to access the Minecraft Bedrock server.

`.vscode/tasks.json`:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Build For Debugging",
      "command": "call .vscode/prepare_debug.bat",
      "type": "shell",
      "options": {
        "shell": {
          "executable": "cmd.exe",
          "args": ["/d", "/c"]
        }
      },
      "problemMatcher": ["$tsc"],
      "presentation": {
        "reveal": "always"
      },
      "group": "test"
    }
  ]
}
```
This file configures the "Build For Debugging" task, which prepares the environment for debugging. This allows you to set breakpoints in your TypeScript files and debug in Minecraft.

For more details on these configurations, refer to the [Minecraft Bedrock Debugger extension documentation](https://marketplace.visualstudio.com/items?itemName=mojang-studios.minecraft-debugger).

Once you've set up the files, follow these steps to start debugging:

1. Start the debugger by pressing `F5` in VSCode.
2. Run the following command in Minecraft:
   ```
   /script debugger connect
   ```


