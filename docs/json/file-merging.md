(file-merging)=
# File Merging

File merging occurs when multiple modules attempt to export files to the same target path. ModularMC provides several conflict resolution strategies to handle these situations gracefully.

## When File Merging Happens

File conflicts occur when:
- Multiple modules export to the same target path
- A module exports to a path that already exists from a previous module

```typescript
// Module A
export const MAP = [
    {
        source: "zombie_sounds.json",
        target: "RP/sounds/sound_definitions.json"
    }
];

// Module B  
export const MAP = [
    {
        source: "skeleton_sounds.json", 
        target: "RP/sounds/sound_definitions.json"  // Conflict!
    }
];
```

## Conflict Resolution Strategies

Configure how conflicts are handled using the `onConflict` property:

### stop (Default)
Stops processing and reports an error when a conflict is detected.

```typescript
{
    source: "sounds.json",
    target: "RP/sounds/sound_definitions.json",
    onConflict: "stop"  // Default behavior
}
```

### skip
Skips the conflicting entry and continues processing other files.

```typescript
{
    source: "backup_sounds.json",
    target: "RP/sounds/sound_definitions.json", 
    onConflict: "skip"  // Skip if file already exists
}
```

### overwrite
Overwrites the existing file with the new one.

```typescript
{
    source: "final_sounds.json",
    target: "RP/sounds/sound_definitions.json",
    onConflict: "overwrite"  // Replace existing file
}
```

### merge
Intelligently merges JSON and material files by combining their structure.

```typescript
{
    source: "additional_sounds.json",
    target: "RP/sounds/sound_definitions.json",
    onConflict: "merge"  // Merge with existing JSON content
}
```

### appendStart
Prepends the source file content to the beginning of the existing file (text files only).

```typescript
{
    source: "header.mcfunction",
    target: "BP/functions/setup.mcfunction",
    onConflict: "appendStart"  // Add to beginning of existing file
}
```

### appendEnd
Appends the source file content to the end of the existing file (text files only).

```typescript
{
    source: "footer.mcfunction", 
    target: "BP/functions/setup.mcfunction",
    onConflict: "appendEnd"  // Add to end of existing file
}
```

## JSON Merging

The `merge` strategy works only with JSON files and uses deep merging:

Objects are merged by combining their properties:

```json
// File A
{
    "sound_definitions": {
        "zombie.hurt": {
            "category": "hostile",
            "sounds": ["sounds/mob/zombie/hurt1"]
        }
    }
}

// File B
{
    "sound_definitions": {
        "skeleton.hurt": {
            "category": "hostile", 
            "sounds": ["sounds/mob/skeleton/hurt1"]
        }
    }
}

// Merged Result
{
    "sound_definitions": {
        "zombie.hurt": {
            "category": "hostile",
            "sounds": ["sounds/mob/zombie/hurt1"]
        },
        "skeleton.hurt": {
            "category": "hostile",
            "sounds": ["sounds/mob/skeleton/hurt1"]
        }
    }
}
```

Arrays are merged by appending elements:

```json
// File A
{
    "tags": ["undead", "hostile"]
}

// File B  
{
    "tags": ["mob", "spawnable"]
}

// Merged Result
{
    "tags": ["undead", "hostile", "mob", "spawnable"]
}
```
