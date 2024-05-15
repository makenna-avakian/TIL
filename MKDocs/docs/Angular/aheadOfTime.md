# Ahead of Time Compilation  

Ahead of Time (AOT) compilation is the opposition of Just-in-Time (JIT) compilation (which compiles the application at runtime in the browser). AOT compilation processes the application during the build phase before it reaches the browser to enhance the user experience.

## How it works
1. Angular HTML templates are compiled into JavaScript instructions that create the DOM elements directly, which eliminates the need for Angular to parse and understand template strings during runtime.

2. TypeScript is compiled into JavaScript, like in JIT compilation, but it happens earlier in the build process.

3. Tree shaking occurs during AOT so that unused JavaScript is removed. This helps in reducing the final size of application files.

## Implementation

Enable AOT compilation in Angular by setting the `--aot` option with the Angular CLI build and serve commands:
```bash
ng build --aot
ng serve --aot
```
* This will be the default for later versions on Angular.

## Benefits
**Performance Improvement**: AOT compiled applications load faster because the browser downloads pre-compiled version of the application. This eliminates the need to compile the application in the browser, reducing the application's bootstrapping time.

**Smaller Angular Framework Download Size**: Because the application is compiled ahead of time, there is no need to download the Angular compiler. This reduces the application’s overall size since the compiler is approximately half the size of Angular itself.

**Template Errors are Caught Earlier**: AOT compiles HTML templates and checks your templates during the build phase, catching errors before they affect your users.

**Better Security**: AOT compilation enables HTML templates and components to be compiled into JavaScript files before they are delivered to the client, making it much harder for others to inject harmful code.
