# useCallback

useCallback is a React hook which returns a callback function that only changes if one of the dependancies change. It also prevents unnecessary rerenders if the callback hasn't updated.

## Syntax
```javascript
const memoizedCallback = useCallback(() => {
    // Function here
}, [dependencies]);
```
### Example use case:

In this example, `increment` is only recreated if `count` changes, thus avoiding unnecessary re-renders if the `Counter` component renders for other reasons.

```javascript
import React, { useState, useCallback } from 'react';

function Counter() {
    const [count, setCount] = useState(0);

    const increment = useCallback(() => {
        setCount(count + 1);
    }, [count]);  // Dependency on 'count'. if count is ot changed, increment is not recreated

    return (
        <div>
            Count: {count}
            <button onClick={increment}>Increment</button>
        </div>
    );
}

export default Counter;
```