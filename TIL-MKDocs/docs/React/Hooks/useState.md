# useState

`useState` in React is how you manage states. States refer to data or properties that need to be tracked in an application. These data points can change over time and affect the behavior and appearance of a component.

## `useState`

 Initializing `useState` returns an array containing two elements: the current state value and a function that allows you to update it. This mechanism provides a way to declare state variables in functional components.

### Syntax
```javascript
const [state, setState] = useState(initialState);
```

`initialState`: The initial value of the state variable. This argument is only used during the first render.

`state`: The current state value.

`setState`: A function that updates the state value.

### Example
Here is a simple example demonstrating how to use useState to manage a counter within a functional component:

```javascript

import React, { useState } from 'react';

function Counter() {
  // Declare a new state variable called "count"
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

Here, `useState` sets a `count` initialized to 0. You would then call `setCount` to update `count` when the button is clicked.

*** Treat state as immutable. Always use the setter function to update state variables instead of modifying them directly.