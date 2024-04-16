# useImperativeHandle

useImperativeHandle customizes the instance value that is exposed to parent components when using `ref`. This hook should be together with `forwardRef`. This is a pretty specific hook with limited use cases.

## Syntax
```javascript
useImperativeHandle(ref, createHandle, [deps])
```
`ref`: The ref passed from the parent component.

`createHandle`: A function that returns an object containing the values or functions to be exposed.

`deps`: (Optional) An array of dependencies that triggers re-creation of the handle if they change.
