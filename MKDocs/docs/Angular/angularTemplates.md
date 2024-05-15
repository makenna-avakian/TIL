# Angular Templates

Angular templates are HTML views enhanced with Angular markup. They connect the application's data and logic to the DOM (Document Object Model).

## Features of Angular Templates
1. **Interpolation**: Uses double curly braces {{ }} to display component properties. Angular replaces these placeholders with the corresponding values during runtime, updating the DOM as these property values change.

2. **Property Binding**: Allows properties of DOM elements to be set based on data values from the component. This is done using square brackets, `[src]="user.imageUrl"`.

3. **Event Binding**: Does the listening for and responding to user actions such as keystrokes, mouse movements, clicks, and touches. Event binding is done using parentheses, `(click)="handleClick()"`.

4. **Two-Way Binding**: Combines property and event binding in a single notation using [( )] syntax. It is used with forms, `[(ngModel)]="user.name"`.

5. **Directives**: Angular extends HTML with directives that add functionality to templates. They can be structural or attribute directives.

6. **Pipes**: Transform displayed values within templates. Pipes are functions that accept an input value and return a transformed value. Common examples include date, uppercase, and lowercase.

## Example
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  template: `
    <div>
      <h1>Welcome, {{ userName }}!</h1>
      <img [src]="userImage" alt="User image">
      <button (click)="logout()">Logout</button>
    </div>
  `,
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {
  userName: string = 'Jane Doe';
  userImage: string = 'path/to/image.jpg';

  logout() {
    console.log('User logged out');
  }
}
```