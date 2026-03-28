(scope-system)=
# Scope System

The scope system in ModularMC allows you to define variables that can be used in {ref}`JSON templates<json-template>` and {ref}`text templates<text-template>` and shared across your project. Scope is a collection of variables and data that can be accessed by templates during processing. Scope variables enable dynamic content generation and module configuration.

Unlike the System Template, ModularMC doesn't have a special `_scope.json` file in every module. ModularMC manages scope directly in `_map.ts` files and through configuration. If you still want to use `_scope.json` you can simply import it in your `_map.ts` file.

Variables used in templates must be passed explicitly to the template using the `scope` property. ModularMC doesn't have a complex system of merging scopes for higher to lower precedence. Since `_map.ts` is a regular TypeScript file, you have a lot of freedom to define variables and you can easily import them from scope files when needed.

```typescript
export const MAP = [{
    source: "template.json",
    target: "BP/entities/zombie.json",
    jsonTemplate: true,
    scope: { entityId: "zombie", health: 20 }
}];
```
