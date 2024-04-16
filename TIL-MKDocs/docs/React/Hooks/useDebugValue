# useDebugValue

useDebugValue is a custom hook that allows you to display a label for custom hooks in React DevTools. This can be useful for debugging custom hooks. You can only use useDebugValue inside custom hooks.

# Syntax
```javascript
import { useDebugValue } from 'react';

function useOnlineStatus() {
  // ...
  useDebugValue(isOnline ? 'Online' : 'Offline');
  // ...
}
```

useDebugValue should be used with caution, and don’t add debug values to every custom Hook. It’s most valuable for custom Hooks that are part of shared libraries and that have a complex internal data structure that’s difficult to inspect.