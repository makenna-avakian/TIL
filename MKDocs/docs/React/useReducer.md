# useReducer

useReducer is a hook in React which handles states that have sub-values. It is essentially used to return an updated state from an intital one.

## Syntax
```javascript
const [state, dispatch] = useReducer(reducer, initialState);
```

`reducer`: A function that determines the changes to an application's state. It uses the current state and an action object to compute the next state.

`initialState`: The initial state value of the reducer.

### useReducer Use Example:

```javascript
function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
}
```