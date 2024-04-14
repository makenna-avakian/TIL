# React refs

Refs are unique to React. React provides refs as a way to acess DOM/React elements created in the render method.

## When to Use Refs

Refs should not be used often since manipulating DOM directly can lead to issues with React's rendering cycle. However, there are certain scenarios where refs are useful:

### Accessing DOM Elements: 
When you need to interact with a DOM element directly, such as focusing an input field or measuring its dimensions.

### Managing Focus, Text Selection, or Media Playback: 
Refs can be used to manage focus, select text, or control media playback.

### Integrating with Third-party DOM Libraries: 
When integrating React with third-party DOM libraries that require direct access to DOM elements.

## Creating Refs

Refs in React are created using the React.createRef() method. You can create a ref and attach it to a React element by using the ref attribute.

```javascript
import React from 'react';

class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.myRef = React.createRef();
  }

  render() {
    return <div ref={this.myRef}>Example</div>;
  }
}
```