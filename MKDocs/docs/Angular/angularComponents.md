# Angular Components

Components are the building blocks of Angular applications. Much like in React, a component in Angular controls a section of the screen and is a combo of Typescript and HTML. The template defines the view, and the class defines the logic and data.

## Structure of an Angular Component
1. **Template**: An HTML template which declares what is rendered on the bade. It can bind data from the Typescript class to the component using Angular's binding syntax.
2. **Class**: he TypeScript class associated with the template. It contains properties and methods needed by the view.
3. **Metadata**: Defined by decorators that attach to the class. The most common is the `@Component` decorator, which includes properties such as:

- `selector`: Specifies a CSS selector for an HTML element that represents the component.
- `templateUrl`: Points to an external file that defines the view.
- `styleUrls`: Points to one or more files that define the CSS styles for the view.


## Example
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-hello-world',
  templateUrl: './hello-world.component.html',
  styleUrls: ['./hello-world.component.css']
})
export class HelloWorldComponent {
  title = 'Hello, World!';
}
```
Corresponding HTML Template:
```typescript
<h1>{{ title }}</h1>
```
The component now can be used anywhere in the application by using its selector `<app-hello-world></app-hello-world>`.