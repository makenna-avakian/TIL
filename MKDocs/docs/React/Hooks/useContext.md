# useContext

useContext is a React hook that allows components to access the value of a React context, meaning you can pass informatioon through a component tree without having to manually pass props at every level.

## Usage

**1. Creating Context**
Use `React.createContext()` to create a new context. It returns an object with two components: `Provider` and `Consumer`, but with hooks, you generally use only the `Provider` and `useContext`.
```javascript
const MyContext = React.createContext(defaultValue);
```

**2. Provide a Context Value**
Use the `Provider` component at a higher level in your component tree and pass the context value via the `value` prop.

```javascript
<MyContext.Provider value={someValue}>
  <MyComponent />
</MyContext.Provider>
```
**3. Consume the Context**
Inside any functional component, call `useContext` and pass in the context object you created. It will return the current context value.
```javascript
function MyComponent() {
  const value = useContext(MyContext);
  return <div>{value}</div>;
}
```

### Best Practices
**Scope Context Properly**: Use context for global states that are accessed by many components (e.g., theme, user authentication). Avoid overuse which can lead to maintainability issues.

**Combine with Other Hooks**: useContext can be combined with other hooks like useReducer or useState to manage and distribute state.