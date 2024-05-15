# Angular Modules

A NG module is defined by `@NgModule`. It takes a single metadata object whose properties describe the module. The most important properties are:
1. `declarations`: Components, directives, and pipes that belong to the module.
2. `imports`: Other modules whose exported classes are needed by component templates declared in this module.
3. `exports`: The subset of declarations that should be visible and usable in the component templates of other modules.
4. `providers`: Creators of services that this module contributes to the global collection of services; they become accessible in all parts of the app.
5. `bootstrap`: The main application view, called the root component, which hosts all other app views. Only the root NgModule should set the bootstrap property.

## Example
```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { HomeComponent } from './home.component';
import { UserService } from './user.service';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [
    UserService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
```
Here, `AppModule` is the root module that uses `BrowserModule`, declares `AppComponent` and `HomeComponent`, provides the `UserService`, and boots using the `AppComponent`.