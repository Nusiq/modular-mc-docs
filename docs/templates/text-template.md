(text-template)=
# Text Template

ModularMC features a text templating system that allows you to embed TypeScript expressions directly within any text file using `{ts: ... :}` syntax. This enables dynamic content generation in text-based files (like for example `.mcfunction` and `.lang` files). Text templates can be used with any text file except JSON files (for that use {ref}`JSON Template<json-template>`).


```{note}
**Difference from JSON Template**: While JSON Template uses the `::` prefix syntax for expressions within JSON files, Text Template uses `{ts: ... :}` markers for any text file format.

This feature is designed for text files that are not JSON, providing similar dynamic capabilities for text-based content.
```

## Basic Syntax: `{ts: ... :}` Markers

Text Template expressions are TypeScript code enclosed between `{ts:` and `:}`. These expressions can be used anywhere in your text files and will be replaced with the result of the last expression.

*Input text:*
```markdown
# My Project

The answer is {ts: 2 + 2 :}.

Current time: {ts: new Date().toISOString() :}

{ts:
const items = ['apple', 'banana', 'orange'];
const count = items.length;
return `Total items: ${count}`;
:}
```

*Output text:*
```markdown
# My Project

The answer is 4.

Current time: 2025-07-17T19:24:43.605Z

Total items: 3
```

Note that if you have multiple expressions, you must explicitly write a `return` statement.

## Integration with _map.ts

To use Text Template, add `textTemplate: true` to a mapping entry in your `_map.ts` file:

Your expressions can access variables from the {ref}`scope<scope-system>` defined in your mapping entry.

*_map.ts entry:*
```typescript
export const MAP = [
  {
    source: "README.template.md",
    target: "README.md",
    textTemplate: true,
    scope: {
      projectName: "My Awesome Project",
      version: "1.0.0",
      author: "John Doe"
    }
  }
];
```

*Input text:*
```markdown
# {ts: projectName :}

Version: {ts: version :}
Author: {ts: author :}

This project was created by {ts: author :} and is currently at version {ts: version :}.
```

*Output text:*
```markdown
# My Awesome Project

Version: 1.0.0
Author: John Doe

This project was created by John Doe and is currently at version 1.0.0.
```
