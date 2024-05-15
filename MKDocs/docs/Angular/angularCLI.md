# Guide to Angular's Command Line Interface

The Angular CLI is a command-line utility that helps you to initialize, develop, and maintain Angular applications.

## Setup:
1. You will need to have Node.js and npm. To install Angular CLI, run: 
```bash
npm install -g @angular/cli
```
2. Either CD to your Angular project or start a new one with:
```bash
ng new my-angular-app
```

## Commands:
- `ng generate component my-component`: Create a new component with all related files (TypeScript, HTML, CSS) and update the module declarations.
- `ng serve`: Builds the application, starts the development server, watches for file changes, and reloads the application automatically in the browser.
- `ng build --prod`: Performs ahead-of-time (AOT) compilation, optimization, and minification of the app's files for production deployment.
- `ng test`: Run unit tests.
- `ng lint`: Perform linting.
