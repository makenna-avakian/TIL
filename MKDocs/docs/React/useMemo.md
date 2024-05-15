# useMemo in React

useMemo is a React hook that optimizes performance by memoizing values. React will store the result of a function and only recalculate it when one of its dependencies changes, rather than on every render. 

## Syntax
```
const memoizedValue = useMemo(() => computationalExpensiveValue(a, b), [a, b]);
```

`memoizedValue` takes `a` and `b` as arguements, and React will only rerun the function of the values of `a` or `b` changes between renders. Otherwise, it will use a memoized version of `a` and `b` from the previous render to avoid any unnecessary recalculations.

## Use Cases:

**Performance Optimization**: For heavy computations that depend on specific props or state and don't need to be recalculated unless these dependencies change.
**Referential Equality**: Ensuring that objects, arrays, or functions maintain referential equality across renders if their contents have not changed, which can be crucial for optimizing child components that rely on object equality to prevent unnecessary re-renders.

Don't use useMemo everwhere. Memoized values need to be stored in memory, and can cause lag if overused. React’s team suggests using it as an optimization, not a default approach for every function or value.