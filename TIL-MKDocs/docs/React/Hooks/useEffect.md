# useEffect

In React's functional components, managing side effects—operations that affect something outside the scope of the function being executed—is crucial for handling data fetching, subscriptions, manually changing the DOM, etc. The useEffect hook performs side effects in functional components.

## Syntax

```javascript
useEffect(() => {
  // logic here
}, [dependencies]);
```

The first argument is a function that will run after every render by default.

The second argument is an optional array of dependencies that triggers the effect only when any of them changes.

### Dependancy Arrays

The dependency array is a feature of useEffect that controls when the effect function runs. Here are the types:

- **No dependency ([])**: The effect runs only once after the initial render, similar to componentDidMount.
- **With dependencies ([deps])**: The effect runs whenever any value in the dependencies array changes, in addition to after the initial render.
- **No array provided**: The effect runs after every render.

### Cleanup functions
`useEffect` allows you to return a function from the effect to prevent memory leaks:

```javascript 
useEffect(() => {
  // Setup logic
  return () => {
    // Cleanup logic
  };
}, [dependencies]);
```

## Common uses

- **Fetching Data**: Perform API calls and update the component state with the fetched data.
- **Listening to Events**: Attach and detach event listeners for user actions or global events.
- **Manually Manipulating the DOM**: Directly manipulate the DOM when necessary, though React encourages avoiding direct DOM manipulations. 