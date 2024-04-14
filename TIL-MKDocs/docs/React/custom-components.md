# React Custom Components

What everyone uses React for! In React you can create functions to generate custom components to build out your architecture. While React provides a variety of built-in components, you will often need to create your own custom components to provide specific functionality and reusability.

## Creating custom components

### Functional Components

Functional components are simple JavaScript functions that return JSX to define the UI. They are stateless by default.

```javascript
import React from 'react';

const MyComponent = (props) => {
  return (
    <div>
      <h1>{props.title}</h1>
      <p>{props.description}</p>
    </div>
  );
};

export default MyComponent;
```

### Class Components

Class components are classes that extend from React.Component. They have additional features such as state management and lifecycle methods, making them suitable for more complex components.

```javascript
import React, { Component } from 'react';

class MyComponent extends Component {
  render() {
    return (
      <div>
        <h1>{this.props.title}</h1>
        <p>{this.props.description}</p>
      </div>
    );
  }
}

export default MyComponent;
```

### Properties (Props)

Props (short for properties) are used to pass data from parent components to child components. They are immutable and are passed down through the component tree.

```javascript
// ParentComponent.js
import React from 'react';
import MyComponent from './MyComponent';

const ParentComponent = () => {
  return <MyComponent title="Hello" description="This is a custom component" />;
};

export default ParentComponent;
```

### State

State is used to manage component-specific data that may change over time. Class components have a built-in state feature, while functional components can use the useState hook.

```javascript
// MyComponent.js
import React, { useState } from 'react';

const MyComponent = () => {
  const [count, setCount] = useState(0);

  const incrementCount = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={incrementCount}>Increment</button>
    </div>
  );
};

export default MyComponent;
```