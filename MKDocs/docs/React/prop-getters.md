# Props Getter and Setter Pattern

The React Prop Getter and Collector strategy is a design pattern used primarily in React applications to manage and simplify the handling of  props within components. Prop Getters are functions that return props based on certain inputs, while Prop Collectors gather props from multiple sources and pass them to child components. 

### Prop Getter Example
```javascript
function useInputProps(name) {
  return {
    id: `id_${name}`,
    name: name,
    type: 'text',
    placeholder: `Enter ${name}`,
  };
}

function Form() {
  return (
    <form>
      <input {...useInputProps('username')} autoComplete="username" />
      <input {...useInputProps('password')} type="password" autoComplete="current-password" />
    </form>
  );
}
```

### Prop Collector Example
```javascript
function useFormProps(initialValues) {
  const [values, setValues] = React.useState(initialValues);

  const handleChange = (event) => {
    setValues({...values, [event.target.name]: event.target.value});
  };

  return { values, handleChange };
}

function ComplexForm() {
  const formProps = useFormProps({username: '', password: ''});

  return (
    <form>
      <input {...useInputProps('username')} {...formProps} onChange={formProps.handleChange} />
      <input {...useInputProps('password')} {...formProps} type="password" onChange={formProps.handleChange} />
    </form>
  );
}
```