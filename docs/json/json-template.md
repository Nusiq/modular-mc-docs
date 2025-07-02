(json-template)=
# JSON Template

ModularMC features a powerful JSON templating system that allows you to embed TypeScript expressions directly within your JSON files. This enables dynamic and reusable code, reducing duplication and making your modules more powerful.

## Basic Syntax: Backticks

JSON Template expressions are TypeScript code enclosed in backticks (`` ` ``). These expressions can be used for both keys and values in your JSON objects.

*Input JSON:*
```json
{
    "foo": "`2 + 2`",
    "`'key_' + (5+5)`": "baz"
}
```

*Output JSON:*
```json
{
    "foo": 4,
    "key_10": "baz"
}
```
Note that keys must always evaluate to a string.

## Using Variables from Scope

Your expressions can access variables from the {ref}`scope<scope-system>`.

*Scope:*
```json
{
    "entity_id": "custom:robot"
}
```

*Input JSON:*
```json
{
    "minecraft:entity": {
        "description": {
            "identifier": "`entity_id`"
        }
    }
}
```

*Output JSON:*
```json
{
    "minecraft:entity": {
        "description": {
            "identifier": "custom:robot"
        }
    }
}
```

## Dynamic Keys

You can use expressions to generate multiple keys at once. If an expression used as a key evaluates to an array of strings, the value will be duplicated for each key.

*Input JSON:*
```json
{ 
    "`['foo', 'bar', 'baz']`": { "enabled": true }
}
```

*Output JSON:*
```json
{
    "foo": { "enabled": true },
    "bar": { "enabled": true },
    "baz": { "enabled": true }
}
```

## The `K` Object

For more advanced scenarios, the `K` helper object allows you to pass a custom scope to the value of each generated key. This is especially useful when creating keys in a loop and needing per-item variables.

The `K` object constructor is `K(keyName, scopeObject)`.

*Input JSON:*
```json
{
    "`[0, 1, 2].map(i => K('event_' + i, { index: i }))`": {
        "action": "`'log_event_' + index`"
    }
}
```
*Output JSON:*
```json
{
    "event_0": {
        "action": "log_event_0"
    },
    "event_1": {
        "action": "log_event_1"
    },
    "event_2": {
        "action": "log_event_2"
    }
}
```

## Array Unpacking with `__unpack__`

The `__unpack__` key provides a powerful way to generate objects within an array. When an object with an `__unpack__` key is found inside an array, it is treated as a template.

The value of `__unpack__` must be an array of objects, where each object provides a scope for one iteration of the template.

*Input JSON:*
```json
[
    { "item": "minecraft:stone" },
    {
        "__unpack__": "[{ 'color': 'red' }, { 'color': 'green' }]",
        "item": "`'wool:' + color`"
    },
    { "item": "minecraft:dirt" }
]
```

*Output JSON:*
```json
[
    { "item": "minecraft:stone" },
    { "item": "wool:red" },
    { "item": "wool:green" },
    { "item": "minecraft:dirt" }
]
```

If you need to generate a list of simple values instead of objects, you can add a `__value__` key to the template object.

*Input JSON:*
```json
[
    "minecraft:stone",
    {
        "__unpack__": "`['red', 'green', 'blue']`",
        "__value__": "`'wool:' + item`"
    }
]
```
In this simpler form, the `__unpack__` array contains the values directly, which are available in the `__value__` expression via the `item` variable.

*Output JSON:*
```json
[
    "minecraft:stone",
    "wool:red",
    "wool:green",
    "wool:blue"
]
```

## Joining String Arrays with `joinStr`

The `joinStr` helper object can be used to join a list of strings into a single string. When an array's first element is a `joinStr` object, the remaining elements are joined together using the specified separator.

*Input JSON:*
```json
[
    "`joinStr('; ')`",
    "statement 1",
    "statement 2",
    "statement 3"
]
```

*Output JSON:*
```json
"statement 1; statement 2; statement 3"
```

## Removing Properties with `undefined`

If any expression evaluates to `undefined`, the key-value pair (or array item) is removed entirely from the output. This way you can conditionally include or exclude parts of your JSON structure.

*Input JSON:*
```json
{
    "always_included": true,
    "sometimes_included": "`some_condition ? 'hello' : undefined`",
    "an_array": [
        "a",
        "`another_condition ? 'b' : undefined`",
        "c"
    ]
}
```

If `some_condition` and `another_condition` are both false, the output will be:

*Output JSON:*
```json
{
    "always_included": true,
    "an_array": [
        "a",
        "c"
    ]
}
```
