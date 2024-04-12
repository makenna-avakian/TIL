# Lifting React States  

### Introduction
In React, lifting a state up means lifting a shared state up to the closest common ancestor so that multiple components can access and modify the same state.

## Example:

The App.js file will be responsible for managing the shared username state and passing it down to both the UsernameInput and DisplayUsername components.

```javascript
app.jsx:

import React, { useState } from 'react';
import UsernameInput from './UsernameInput';
import DisplayUsername from './DisplayUsername';

function App() {
  const [username, setUsername] = useState('');

  // Function to update username
  const handleUsernameChange = (newUsername) => {
    setUsername(newUsername);
  };

  return (
    <div>
      <h1>User Profile</h1>
      <UsernameInput username={username} onUsernameChange={handleUsernameChange} />
      <DisplayUsername username={username} />
    </div>
  );
}

export default App;

```

The UsernameInput.js file provides an input field for users to type their username. It receives the current username and a function to update it from its parent.

```javascript
import React from 'react';

function UsernameInput({ username, onUsernameChange }) {
  return (
    <div>
      <label htmlFor="username">Username: </label>
      <input
        id="username"
        type="text"
        value={username}
        onChange={(e) => onUsernameChange(e.target.value)}
      />
    </div>
  );
}

export default UsernameInput;
```

The DisplayUsername.js component simply displays the current username. It receives the username as a prop from its parent component.

```javascript
import React from 'react';

function DisplayUsername({ username }) {
  return (
    <div>
      <h2>Current Username: {username}</h2>
    </div>
  );
}

export default DisplayUsername;
```

App.tsx acts as the common ancestor for usernameinput.js and displayusername.js. The state being passed is `username`, which gets passed to both child components, and is the "lifted up" state.