# useLayoutEffect

useLayoutEffect is a version of the React hook useEffect that fires before a broswer repaints a screen.

## Syntax
```javscript
useLayoutEffect(setup, dependencies?)
```


useLayoutEffect runs synchronously after all DOM changes but before the browser paints. This makes it useful for reading layout from the DOM and then synchronously re-rendering, ensuring the updates are invisible to the user.

### Common Use Cases 
- Measuring and changing the DOM
- Performing animations

Note that it should be used sparingly because it blocks visual updates until the callback is completed. It can cause noticeable delays in the UI rendering.