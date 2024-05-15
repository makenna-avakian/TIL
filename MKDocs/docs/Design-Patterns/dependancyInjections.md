# Dependency Injections

Dependency Injection (DI) is a design pattern used to implement IoC (Inversion of Control), allowing for better modularity and making the system easier to manage and scale. Using DI, objects receive their dependencies from an external source rather than creating them internally.

DI achieves this by decoupling the creation of an object from its usage.

## Benefits of Dependency Injection
**Modularity**: By decoupling dependencies, DI increases the modularity of the application.

**Testability**: Components that do not manage their dependencies are easier to test in isolation because they can be easily replaced with mock objects.

**Maintainability**: Reducing dependency coupling makes the system easier to understand and modify.

**Flexibility**: Components can be replaced with alternative implementations without changing the components themselves.

## Examples:
1. **Constructor Injection**, where dependencies are provided through the class constructor.
```typescript
interface Logger {
    log(message: string): void;
}

class ConsoleLogger implements Logger {
    log(message: string) {
        console.log(message);
    }
}

class AppService {
    constructor(private logger: Logger) {}

    doWork() {
        this.logger.log('Doing work');
    }
}

const logger = new ConsoleLogger();
const appService = new AppService(logger);
appService.doWork();
```
2. **Property Injection**, where the property injection injects dependencies by setting a properties on the class.
```typescript
class AppService {
    private _logger: Logger;

    set logger(logger: Logger) {
        this._logger = logger;
    }

    doWork() {
        this._logger.log('Doing work');
    }
}

const appService = new AppService();
appService.logger = new ConsoleLogger();
appService.doWork();
```
* Note this can expose public setters which can lead to dependencies being changed after initialization.

3. **Interface Injection**, where the component is required to provide and injection method.
```javascript
interface LoggerInjector {
    injectLogger(logger: Logger): void;
}

class AppService implements LoggerInjector {
    private logger: Logger;

    injectLogger(logger: Logger): void {
        this.logger = logger;
    }

    doWork() {
        this.logger.log('Doing work');
    }
}

const appService = new AppService();
appService.injectLogger(new ConsoleLogger());
appService.doWork();
```